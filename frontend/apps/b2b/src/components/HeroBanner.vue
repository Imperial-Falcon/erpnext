<template>
	<div class="relative overflow-hidden px-5">
		<!-- Carousel Container -->
		<div
			ref="carouselRef"
			class="flex gap-4 overflow-x-auto no-scrollbar snap-x snap-mandatory scroll-smooth"
			@scroll="onCarouselScroll"
			@touchstart="pauseAutoScroll"
			@touchend="resumeAutoScroll"
		>
			<div
				v-for="(banner, index) in banners"
				:key="index"
				class="min-w-full snap-center relative h-[190px] rounded-[1.75rem] overflow-hidden group cursor-pointer"
				@click="handleBannerClick(banner)"
			>
				<!-- Mesh Gradient Background -->
				<div class="absolute inset-0" :class="banner.bgGradient"></div>
				<div class="absolute inset-0 bg-[radial-gradient(circle_at_20%_80%,rgba(255,255,255,0.15)_0%,transparent_60%)]"></div>
				<div class="absolute inset-0 bg-[radial-gradient(circle_at_80%_20%,rgba(255,255,255,0.1)_0%,transparent_50%)]"></div>

				<!-- Animated Orbs -->
				<div class="absolute -top-12 -right-12 w-44 h-44 bg-white/10 rounded-full blur-3xl group-hover:scale-[1.4] transition-transform duration-700"></div>
				<div class="absolute -bottom-12 -left-12 w-36 h-36 bg-white/10 rounded-full blur-3xl animate-pulse-subtle"></div>

				<!-- Content -->
				<div class="relative h-full flex items-center p-7 text-white z-10">
					<div class="flex-1 pr-4">
						<span class="inline-block px-3 py-1 bg-white/20 backdrop-blur-md rounded-full text-[10px] font-black uppercase tracking-[0.15em] mb-3 border border-white/20 shadow-sm">
							{{ banner.tag }}
						</span>
						<h2
							class="text-[1.6rem] font-black leading-[1.15] mb-4 drop-shadow-sm"
							v-html="banner.title"
						></h2>
						<button class="px-5 py-2 bg-white/95 backdrop-blur-sm text-gray-900 text-[11px] font-black rounded-full hover:shadow-lg active:scale-95 transition-all tracking-wide uppercase shadow-md">
							{{ banner.cta }}
						</button>
					</div>

					<!-- Featured Image -->
					<div class="w-[120px] h-[120px] relative flex items-center justify-center flex-shrink-0">
						<div class="absolute inset-0 bg-white/10 rounded-full blur-2xl scale-125"></div>
						<img
							:src="banner.image"
							:alt="banner.tag"
							class="w-full h-full object-contain relative z-10 group-hover:scale-110 group-hover:rotate-3 transition-transform duration-500 drop-shadow-2xl"
						/>
					</div>
				</div>
			</div>
		</div>

		<!-- Pagination Dots -->
		<div class="flex justify-center gap-2 mt-4">
			<button
				v-for="(_, i) in banners"
				:key="i"
				@click="scrollToSlide(i)"
				class="h-[5px] rounded-full transition-all duration-500 ease-out"
				:class="currentSlide === i
					? 'w-7 bg-gradient-to-r from-brand-primary to-brand-secondary shadow-neon'
					: 'w-[5px] bg-gray-300 dark:bg-gray-600 hover:bg-gray-400'"
			></button>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const carouselRef = ref(null)
const currentSlide = ref(0)
let autoScrollInterval = null

const banners = [
	{
		tag: "Summer Offer",
		title: "25% OFF<br/>on All Vitamins",
		cta: "Shop Now",
		bgGradient: "bg-gradient-to-br from-violet-600 via-brand-primary to-indigo-700",
		image: "https://via.placeholder.com/200?text=Vitamins"
	},
	{
		tag: "New Arrival",
		title: "Pure Organic<br/>Honey Series",
		cta: "Explore",
		bgGradient: "bg-gradient-to-br from-emerald-500 via-teal-600 to-cyan-700",
		image: "https://via.placeholder.com/200?text=Honey"
	},
	{
		tag: "Special Deal",
		title: "Premium<br/>Personal Care",
		cta: "Get Deals",
		bgGradient: "bg-gradient-to-br from-orange-500 via-rose-500 to-pink-600",
		image: "https://via.placeholder.com/200?text=Care"
	}
]

const onCarouselScroll = () => {
	if (!carouselRef.value) return
	const scrollLeft = carouselRef.value.scrollLeft
	const width = carouselRef.value.offsetWidth
	currentSlide.value = Math.round(scrollLeft / width)
}

const scrollToSlide = (index) => {
	if (!carouselRef.value) return
	const width = carouselRef.value.offsetWidth
	carouselRef.value.scrollTo({ left: width * index, behavior: 'smooth' })
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
	// Navigate to offer/category
}

onMounted(() => {
	startAutoScroll()
})

onUnmounted(() => {
	pauseAutoScroll()
})
</script>
