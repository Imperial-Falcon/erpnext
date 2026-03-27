<template>
	<BaseLayout :showBackButton="false" :showHeader="false">
		<template #body>
			<ion-content :scroll-events="true" @ionScroll="onScroll">
				<div class="page-content bg-transparent pb-28 relative">
					<!-- Ambient Backdrop Orbs -->
					<div class="absolute inset-0 overflow-hidden pointer-events-none z-[-1]">
						<div class="absolute top-[-80px] left-[-60px] w-[320px] h-[320px] bg-brand-primary/15 blur-[100px] rounded-full animate-pulse-subtle"></div>
						<div class="absolute top-[25%] right-[-80px] w-[280px] h-[280px] bg-brand-secondary/15 blur-[100px] rounded-full"></div>
						<div class="absolute bottom-[30%] left-[10%] w-[200px] h-[200px] bg-brand-accent/10 blur-[80px] rounded-full animate-float"></div>
					</div>

					<!-- Sticky Header -->
					<AppHeader
						:isScrolled="isScrolled"
						subtitle="Welcome back"
						title="Healthy Living"
						:showBack="false"
					>
						<template #actions>
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
								<span class="absolute top-1.5 right-1.5 w-2.5 h-2.5 bg-brand-accent rounded-full border-2 border-white dark:border-gray-900 animate-pulse"></span>
							</button>
						</template>
					</AppHeader>

					<!-- Collapsible Search Bar -->
					<div
						class="px-5 animate-fade-in-up overflow-hidden transition-all duration-500 ease-[cubic-bezier(0.16,1,0.3,1)]"
						:class="isScrolled ? 'max-h-0 opacity-0 mb-0 pointer-events-none' : 'max-h-[80px] opacity-100 mb-5'"
						style="animation-delay: 0.1s"
					>
						<div class="relative group" @click="$router.push('/products')">
							<Search class="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400 group-hover:text-brand-primary transition-colors z-10" />
							<div class="w-full pl-12 pr-4 py-3.5 app-card text-sm font-semibold text-gray-400 flex items-center relative overflow-hidden group-hover:shadow-glass transition-all duration-300 border border-white/50 dark:border-gray-800/50">
								<div class="absolute inset-0 bg-gradient-to-r from-brand-primary/5 to-brand-secondary/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"></div>
								Search for medicines, vitamins...
							</div>
						</div>
					</div>

					<!-- Hero Banner Carousel -->
					<div class="animate-fade-in-up" style="animation-delay: 0.15s">
						<HeroBanner />
					</div>

					<!-- Quick Actions Strip -->
					<section class="mt-7 animate-fade-in-up" style="animation-delay: 0.2s">
						<div class="flex gap-3 overflow-x-auto no-scrollbar px-5">
							<button
								v-for="(action, i) in quickActions"
								:key="i"
								@click="action.handler"
								class="flex items-center gap-2 px-4 py-2.5 app-card rounded-full border border-white/50 dark:border-gray-800/50 flex-shrink-0 active:scale-95 transition-all group hover:shadow-glass"
							>
								<component :is="action.icon" class="w-4 h-4 text-brand-primary group-hover:scale-110 transition-transform" />
								<span class="text-[11px] font-black text-gray-700 dark:text-gray-300 whitespace-nowrap tracking-tight">{{ action.label }}</span>
							</button>
						</div>
					</section>

					<!-- Categories -->
					<section class="mt-8 animate-fade-in-up" style="animation-delay: 0.25s">
						<SectionHeader title="Categories" subtitle="Everything you need" :showSeeAll="false" />
						<div class="flex gap-5 overflow-x-auto no-scrollbar px-5 py-1">
							<CategoryCard
								v-for="cat in mockCategories"
								:key="cat.name"
								:category="cat"
								@select="handleCategorySelect"
							/>
						</div>
					</section>

					<!-- Trending / Hot Picks (Horizontal scroll) -->
					<section class="mt-8 animate-fade-in-up" style="animation-delay: 0.3s">
						<SectionHeader title="Trending Now" subtitle="People's choice" @see-all="$router.push('/products')" />
						<div class="flex gap-4 overflow-x-auto no-scrollbar px-5 pb-2">
							<ProductThumb
								v-for="product in products.data?.slice(0, 6)"
								:key="product.name"
								:product="product"
								variant="minimal"
							/>
						</div>
					</section>

					<!-- Flash Deals Banner -->
					<section class="mt-8 px-5 animate-fade-in-up" style="animation-delay: 0.35s">
						<div class="relative overflow-hidden rounded-[1.5rem] p-5 bg-gradient-to-br from-brand-accent/90 via-rose-500/90 to-orange-500/90 shadow-lg">
							<div class="absolute inset-0 bg-[radial-gradient(circle_at_80%_20%,rgba(255,255,255,0.15)_0%,transparent_50%)]"></div>
							<div class="absolute -bottom-8 -right-8 w-32 h-32 bg-white/10 rounded-full blur-2xl"></div>
							<div class="relative z-10 flex items-center justify-between">
								<div>
									<div class="flex items-center gap-2 mb-2">
										<Zap class="w-4 h-4 text-yellow-300" />
										<span class="text-[10px] font-black text-white/80 uppercase tracking-[0.2em]">Flash Deals</span>
									</div>
									<h3 class="text-xl font-black text-white leading-tight mb-1">Up to 40% OFF</h3>
									<p class="text-[11px] text-white/70 font-bold">Limited time offers on select items</p>
								</div>
								<button
									@click="$router.push('/offers')"
									class="px-5 py-2.5 bg-white text-gray-900 text-[10px] font-black rounded-full uppercase tracking-widest shadow-md active:scale-95 transition-all flex-shrink-0"
								>
									View All
								</button>
							</div>
						</div>
					</section>

					<!-- Special Deals Grid -->
					<section class="mt-8 px-5 animate-fade-in-up" style="animation-delay: 0.4s">
						<SectionHeader title="Special Deals" subtitle="Limited time offers" :showSeeAll="true" @see-all="$router.push('/offers')" />
						<div class="grid grid-cols-2 gap-4">
							<ProductThumb
								v-for="product in products.data?.slice(6, 12)"
								:key="product.name"
								:product="product"
								variant="vertical"
							/>
						</div>
					</section>

					<!-- Featured Brands -->
					<section class="mt-8 mb-4 animate-fade-in-up" style="animation-delay: 0.45s">
						<SectionHeader title="Top Brands" subtitle="Trusted by many" :showSeeAll="false" />
						<div class="flex gap-4 overflow-x-auto no-scrollbar px-5 py-1">
							<div
								v-for="i in 5"
								:key="i"
								class="min-w-[100px] h-[72px] app-card flex items-center justify-center p-4 active:scale-95 transition-all group hover:shadow-glass border border-white/50 dark:border-gray-800/50"
							>
								<img
									:src="`https://via.placeholder.com/100x40?text=Brand+${i}`"
									class="max-w-full grayscale opacity-40 group-hover:grayscale-0 group-hover:opacity-100 transition-all duration-500"
								/>
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
import { Bell, Search, Pill, HeartPulse, Baby, Apple, SprayCan, Zap, Repeat, FileText, Crown } from 'lucide-vue-next'
import HeroBanner from '@/components/HeroBanner.vue'
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import ProductThumb from "@/components/ProductThumb.vue"
import SectionHeader from '@/components/SectionHeader.vue'
import CategoryCard from "@/components/CategoryCard.vue"
import AppHeader from "@/components/AppHeader.vue"

import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { createResource } from 'frappe-ui'

const router = useRouter()
const isScrolled = ref(false)

const onScroll = (ev) => {
	isScrolled.value = ev.detail.scrollTop > 30
}

const mockCategories = [
	{ name: "Medicines", icon: Pill, bgClass: "bg-violet-100 dark:bg-violet-900/30", iconClass: "text-violet-600 dark:text-violet-400 group-hover:text-white" },
	{ name: "Wellness", icon: HeartPulse, bgClass: "bg-rose-100 dark:bg-rose-900/30", iconClass: "text-rose-600 dark:text-rose-400 group-hover:text-white" },
	{ name: "Personal Care", icon: SprayCan, bgClass: "bg-sky-100 dark:bg-sky-900/30", iconClass: "text-sky-600 dark:text-sky-400 group-hover:text-white" },
	{ name: "Baby Care", icon: Baby, bgClass: "bg-amber-100 dark:bg-amber-900/30", iconClass: "text-amber-600 dark:text-amber-400 group-hover:text-white" },
	{ name: "Nutrition", icon: Apple, bgClass: "bg-emerald-100 dark:bg-emerald-900/30", iconClass: "text-emerald-600 dark:text-emerald-400 group-hover:text-white" }
]

const quickActions = [
	{ label: "Reorder", icon: Repeat, handler: () => router.push('/reorder') },
	{ label: "Prescriptions", icon: FileText, handler: () => router.push('/request-medicine') },
	{ label: "Offers", icon: Zap, handler: () => router.push('/offers') },
	{ label: "Leaderboard", icon: Crown, handler: () => router.push('/leaderboard') },
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
/* All styling via Tailwind utility classes and global design tokens */
</style>
