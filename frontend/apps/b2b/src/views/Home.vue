<template>
	<BaseLayout>
		<template #body>
			<ion-content>
				<div class="page-content bg-gray-50/30 pb-24">
					<!-- Custom Header for Home -->
					<div class="px-5 pt-8 pb-4 flex justify-between items-center sticky top-0 bg-gray-50/80 backdrop-blur-xl z-50">
						<div class="flex flex-col">
							<span class="text-[10px] font-black uppercase tracking-[0.2em] text-gray-400 leading-none mb-1">Welcome back</span>
							<h1 class="text-2xl font-black text-gray-900 leading-none">Healthy Living</h1>
						</div>
						<button 
							@click="$router.push('/notifications')"
							class="relative p-2.5 bg-white rounded-2xl shadow-xl shadow-gray-200 border border-gray-100 active:scale-90 transition-all"
						>
							<Bell class="w-5 h-5 text-gray-700" />
							<span class="absolute top-2.5 right-2.5 w-2 h-2 bg-red-500 rounded-full border-2 border-white"></span>
						</button>
					</div>

					<!-- Search bar (Sticky below header if desired) -->
					<div class="px-5 mb-6">
						<div class="relative group" @click="$router.push('/products')">
							<Search class="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400 group-hover:text-indigo-600 transition-colors" />
							<div class="w-full pl-12 pr-4 py-4 bg-white border border-gray-100 rounded-2xl text-sm font-semibold text-gray-400 shadow-xl shadow-gray-100/50 flex items-center">
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

import { useRouter } from 'vue-router'
import { createResource } from 'frappe-ui'

const router = useRouter()

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
