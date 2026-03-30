<template>
	<div class="relative w-full overflow-hidden">
		<!-- Carousel Container -->
		<div
			ref="carouselRef"
			class="flex gap-4 overflow-x-auto snap-x snap-mandatory px-5 pb-4 hide-scrollbar"
			@scroll="onCarouselScroll"
			@touchstart="pauseAutoScroll"
			@touchend="resumeAutoScroll"
			style="scroll-behavior: smooth;"
		>
			<template v-if="bannerResource.list.loading || !banners.length && bannerResource.list.loading">
				<div class="min-w-full sm:min-w-[calc(100%-2rem)] snap-center relative h-[210px] rounded-[28px] overflow-hidden shadow-md animate-pulse bg-gray-200 dark:bg-gray-800">
					<div class="absolute inset-0 bg-gradient-to-br from-gray-200 to-gray-300 dark:from-gray-800 dark:to-gray-900"></div>
					<div class="relative w-full h-full p-6 flex flex-row items-center justify-between">
						<div class="flex flex-col items-start justify-center flex-1 h-full pr-4 space-y-3">
							<div class="w-16 h-5 bg-white/30 rounded-full"></div>
							<div class="w-3/4 h-6 bg-white/30 rounded-lg"></div>
							<div class="w-1/2 h-6 bg-white/30 rounded-lg mb-2"></div>
							<div class="mt-auto w-24 h-10 bg-white/50 rounded-full"></div>
						</div>
						<div class="w-28 h-28 bg-white/30 rounded-[2rem]"></div>
					</div>
				</div>
			</template>

			<template v-else>
				<div
					v-for="(banner, index) in banners"
					:key="banner.name"
					class="min-w-full sm:min-w-[calc(100%-2rem)] snap-center relative h-[210px] rounded-[28px] overflow-hidden group cursor-pointer shadow-md"
					@click="handleBannerClick(banner)"
				>
					<!-- Material Design 3 Style Background Gradients -->
					<div 
						class="absolute inset-0 bg-gradient-to-br" 
						:style="{
							'--tw-gradient-from': banner.background_gradient_from || '#059669',
							'--tw-gradient-to': banner.background_gradient_to || '#0891b2',
							'--tw-gradient-stops': 'var(--tw-gradient-from), var(--tw-gradient-to)'
						}"
					></div>
					<!-- Soft glowing element in the corner -->
					<div class="absolute -top-10 -right-10 w-48 h-48 bg-white/10 rounded-full blur-2xl group-hover:scale-110 transition-transform duration-700 ease-out"></div>
					<div class="absolute -bottom-8 -left-8 w-32 h-32 bg-black/5 rounded-full blur-2xl"></div>

					<!-- Content Container -->
					<div class="relative w-full h-full p-6 flex flex-row items-center justify-between z-10">
						<!-- Text Section -->
						<div class="flex flex-col items-start justify-center flex-1 h-full pr-4">
							<!-- Tag / Label -->
							<div 
								v-if="banner.tag_text"
								class="inline-flex items-center px-3 py-1 backdrop-blur-sm rounded-full text-[10px] font-bold uppercase tracking-widest mb-3 border border-white/30"
								:style="{ backgroundColor: banner.tag_bg_color || 'rgba(255,255,255,0.2)', color: banner.tag_text_color || '#ffffff' }"
							>
								{{ banner.tag_text }}
							</div>
							
							<!-- Headline -->
							<h2 
								class="text-[22px] font-black leading-[1.2] drop-shadow-sm mb-4"
								:style="{ color: banner.title_text_color || '#ffffff' }"
								v-html="banner.title_html"
							></h2>
							
							<!-- MD3 Filled Button -->
							<button 
								v-if="banner.cta_text"
								class="mt-auto inline-flex items-center justify-center px-6 py-2.5 text-xs font-bold rounded-full shadow-lg hover:opacity-90 active:scale-95 transition-all duration-200"
								:style="{ backgroundColor: banner.cta_bg_color || '#ffffff', color: banner.cta_text_color || '#111827' }"
							>
								{{ banner.cta_text }}
							</button>
						</div>

						<!-- Image Section -->
						<div class="relative w-28 h-28 flex-shrink-0 flex items-center justify-center group-hover:-translate-y-1 group-hover:scale-105 transition-all duration-500 ease-out">
							<!-- Soft drop shadow under image instead of bright orb -->
							<div class="absolute inset-x-0 -bottom-4 h-8 bg-black/20 blur-xl rounded-full scale-75"></div>
							<img
								v-if="banner.banner_image"
								:src="banner.banner_image"
								:alt="banner.tag_text || 'Banner'"
								class="w-full h-full object-contain relative z-10"
								loading="lazy"
							/>
						</div>
					</div>
				</div>
			</template>
		</div>

		<!-- Pagination Indicators (MD3 styling) -->
		<div class="flex justify-center items-center gap-2 mt-1">
			<button
				v-for="(_, i) in banners"
				:key="i"
				@click="scrollToSlide(i)"
				class="h-2 rounded-full transition-all duration-300 ease-out"
				:class="currentSlide === i
					? 'w-6 bg-brand-primary'
					: 'w-2 bg-gray-300 dark:bg-gray-600 hover:bg-gray-400'"
				:aria-label="`Go to slide ${i + 1}`"
			></button>
		</div>
	</div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { createListResource } from 'frappe-ui'
import dayjs from 'dayjs'

const router = useRouter()
const carouselRef = ref(null)
const currentSlide = ref(0)
let autoScrollInterval = null

// Real-world dynamic content fetching
const bannerResource = createListResource({
	doctype: 'Hero Banner',
	fields: ['*'],
	filters: {
		is_published: 1,
		app_name: 'B2B'
	},
	orderBy: 'sort_order asc',
	auto: true
})

const banners = computed(() => {
	if (!bannerResource.data) return []
	
	const now = dayjs()
	return bannerResource.data.filter(b => {
		const started = !b.start_date || now.isAfter(dayjs(b.start_date))
		const ended = b.end_date && now.isAfter(dayjs(b.end_date))
		return started && !ended
	})
})

const onCarouselScroll = () => {
	if (!carouselRef.value) return
	const scrollLeft = carouselRef.value.scrollLeft
	// Account for the padding-left (20px or 1.25rem from px-5) when calculating active slide
	// A simpler robust way for snap carousels:
	const width = carouselRef.value.offsetWidth
	const center = scrollLeft + (width / 2)
	const cards = Array.from(carouselRef.value.children)
	
	let closestIndex = 0
	let minDistance = Infinity
	
	cards.forEach((card, index) => {
		const cardCenter = card.offsetLeft + (card.offsetWidth / 2)
		const distance = Math.abs(center - cardCenter)
		if (distance < minDistance) {
			minDistance = distance
			closestIndex = index
		}
	})
	
	currentSlide.value = closestIndex
}

const scrollToSlide = (index) => {
	if (!carouselRef.value) return
	const cards = Array.from(carouselRef.value.children)
	if (cards[index]) {
		// Calculate precise scroll position
		const card = cards[index]
		const scrollTarget = card.offsetLeft - 20 // 20px corresponds to px-5
		carouselRef.value.scrollTo({ left: scrollTarget, behavior: 'smooth' })
	}
	currentSlide.value = index
}

const startAutoScroll = () => {
	autoScrollInterval = setInterval(() => {
		const next = (currentSlide.value + 1) % banners.length
		scrollToSlide(next)
	}, 4000)
}

const pauseAutoScroll = () => {
	if (autoScrollInterval) clearInterval(autoScrollInterval)
}

const resumeAutoScroll = () => {
	pauseAutoScroll()
	startAutoScroll()
}

const handleBannerClick = (banner) => {
	if (banner.target_route) {
		router.push(banner.target_route)
	}
}

onMounted(() => {
	startAutoScroll()
})

onUnmounted(() => {
	pauseAutoScroll()
})
</script>

<style scoped>
.hide-scrollbar {
	-ms-overflow-style: none; /* IE and Edge */
	scrollbar-width: none; /* Firefox */
}
.hide-scrollbar::-webkit-scrollbar {
	display: none; /* Chrome, Safari and Opera */
}
</style>
