<template>
	<BaseLayout :showBackButton="false" :showHeader="false">
		<template #body>
			<ion-content :scroll-events="true" @ionScroll="onScroll">
				<div class="page-content bg-transparent pb-24 relative">
					<!-- Ambient Backdrop Effects Wrapper -->
					<div class="absolute inset-0 overflow-hidden pointer-events-none z-[-1]">
						<div class="absolute top-[-100px] left-[-50px] w-[300px] h-[300px] bg-brand-primary/20 blur-[80px] rounded-full"></div>
						<div class="absolute top-[20%] right-[-100px] w-[250px] h-[250px] bg-brand-secondary/20 blur-[80px] rounded-full"></div>
					</div>

					<!-- Custom Header for Home -->
					<div 
						class="px-5 flex justify-between items-center sticky top-0 z-50 transition-all duration-500 ease-out"
						:class="isScrolled ? 'bg-white/70 dark:bg-black/70 backdrop-blur-xl shadow-glass py-4' : 'bg-transparent pt-8 pb-4'"
					>
						<div class="flex flex-col animate-fade-in-up">
							<span class="text-[10px] font-black uppercase tracking-[0.2em] text-brand-primary leading-none mb-1">Welcome back</span>
							<h1 class="text-2xl font-black text-transparent bg-clip-text bg-gradient-to-r from-brand-primary to-brand-secondary leading-none">Healthy Living</h1>
						</div>
						<div class="flex items-center gap-2">
							<button 
								v-if="isScrolled"
								@click="$router.push('/products')"
								class="relative p-2.5 app-card active:scale-90 transition-all hover:shadow-neon"
							>
								<Search class="w-5 h-5 text-gray-700 dark:text-gray-300" />
							</button>
							<button 
								@click="$router.push('/notifications')"
								class="relative p-2.5 app-card active:scale-90 transition-all hover:shadow-neon"
							>
								<Bell class="w-5 h-5 text-gray-700 dark:text-gray-300" />
								<span class="absolute top-2 right-2 w-2 h-2 bg-brand-accent rounded-full border-2 border-white dark:border-gray-800 animate-pulse"></span>
							</button>
						</div>
					</div>

					<!-- Search bar (Collapses on Scroll) -->
					<div 
						class="px-5 animate-fade-in-up overflow-hidden transition-all duration-500 ease-in-out" 
						:class="isScrolled ? 'max-h-0 opacity-0 mb-0' : 'max-h-[100px] opacity-100 mb-6'"
						style="animation-delay: 0.1s"
					>
						<div class="relative group" @click="$router.push('/products')">
							<Search class="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400 group-hover:text-brand-primary transition-colors z-10" />
							<div class="w-full pl-12 pr-4 py-4 app-card text-sm font-semibold text-gray-400 flex items-center relative overflow-hidden group-hover:shadow-glass transition-all">
								<div class="absolute inset-0 bg-gradient-to-r from-brand-primary/5 to-brand-secondary/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"></div>
								Search for medicines, vitamins...
							</div>
						</div>
					</div>

					<!-- Hero banner -->
					<HeroBanner />

					<!-- Shop by Category -->
					<section class="mt-8">
						<SectionHeader title="Categories" subtitle="Everything you need" />
						<div class="flex gap-6 overflow-x-auto no-scrollbar px-6 py-2">
							<CategoryCard
								v-for="cat in mockCategories"
								:key="cat.name"
								:category="cat"
								@select="handleCategorySelect"
							/>
						</div>
					</section>

					<!-- Trending Products (Horizontal) -->
					<section class="mt-8">
						<SectionHeader title="Trending Now" subtitle="People's choice" />
						<div class="flex gap-4 overflow-x-auto no-scrollbar px-4 pb-4">
							<ProductThumb
								v-for="product in products.data?.slice(0, 5)"
								:key="product.name"
								:product="product"
								variant="minimal"
							/>
						</div>
					</section>

					<!-- Deals of the Day (Vertical Grid) -->
					<section class="mt-8 px-4">
						<SectionHeader title="Special Deals" subtitle="Limited time offers" :showSeeAll="true" @see-all="$router.push('/offers')" />

						<div class="grid grid-cols-2 gap-4">
							<ProductThumb
								v-for="product in products.data?.slice(5, 11)"
								:key="product.name"
								:product="product"
								variant="vertical"
							/>
						</div>
					</section>

					<!-- Featured Brands -->
					<section class="mt-8 mb-4">
						<SectionHeader title="Featured Brands" :showSeeAll="false" />
						<div class="flex gap-4 overflow-x-auto no-scrollbar px-6 py-2">
							<div v-for="i in 5" :key="i" class="min-w-[100px] h-20 bg-white rounded-2xl flex items-center justify-center p-4 shadow-sm border border-gray-50 active:scale-95 transition-all">
								<img :src="`https://via.placeholder.com/100x40?text=Brand+${i}`" class="max-w-full grayscale opacity-50 hover:grayscale-0 hover:opacity-100 transition-all duration-300" />
							</div>
						</div>
					</section>
				</div>
			</ion-content>
		</template>
	</BaseLayout>
</template>

<script setup>
import { IonContent } from '@ionic/vue'
import { Bell, Search, Pill, HeartPulse, Baby, Apple, SprayCan } from 'lucide-vue-next'
import HeroBanner from '@/components/HeroBanner.vue'
import BaseLayout from '@/components/layouts/BaseLayout.vue'
import ProductThumb from '@/components/ProductThumb.vue'
import SectionHeader from '@/components/SectionHeader.vue'
import CategoryCard from '@/components/CategoryCard.vue'

import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { createResource } from 'frappe-ui'

const router = useRouter()
const isScrolled = ref(false)

const onScroll = (ev) => {
	isScrolled.value = ev.detail.scrollTop > 30
}

const mockCategories = [
	{ name: "Medicines", icon: Pill },
	{ name: "Wellness", icon: HeartPulse },
	{ name: "Personal Care", icon: SprayCan },
	{ name: "Baby Care", icon: Baby },
	{ name: "Nutrition", icon: Apple }
]

const products = createResource({
    url: 'erpnext.api.item_api.get_items',
    params: {
        limit: 30
    },
    auto: true
})

const handleCategorySelect = (cat) => {
	router.push(`/category/${cat.name}`)
}
</script>

<style scoped>
/* Scoped styles if needed, but mostly using global classes now */
</style>
