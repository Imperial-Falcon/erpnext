<template>
	<BaseLayout :pageTitle="__('Offer Detail')" :showHeader="false">
		<template #body>
			<div class="flex flex-col h-full overflow-hidden relative" style="background: var(--app-bg);">
				<!-- Navigation Bar -->
				<AppHeader :title="offer.title" :showBack="true" customClass="absolute w-full z-50 bg-black/20 dark:bg-black/50 backdrop-blur-md pb-4 pt-12 border-b border-white/10" titleClass="text-white drop-shadow-md text-lg truncate max-w-[200px]">
					<template #actions>
						<button class="p-2 bg-white/20 backdrop-blur-md border border-white/20 !rounded-full text-white shadow-[0_4px_30px_rgba(0,0,0,0.05)] active:scale-90 transition-all">
							<Share2 class="w-5 h-5" />
						</button>
					</template>
				</AppHeader>

				<ion-content class="transparent-content pb-24">
					<!-- Promotional Banner -->
					<div class="relative w-full aspect-video overflow-hidden">
						<img :src="offer.banner" alt="Offer Banner" class="w-full h-full object-cover mix-blend-multiply dark:mix-blend-normal" />
						<div class="absolute inset-0 bg-gradient-to-t from-black via-black/40 to-transparent flex flex-col justify-end p-6 pb-8">
							<div class="flex items-center gap-2 mb-2 animate-fade-in-up">
								<span class="px-3 py-1 bg-gradient-to-r from-red-500 to-orange-500 text-white text-[10px] font-black rounded-xl uppercase tracking-wider shadow-neon">
									Limited Offer
								</span>
								<span class="text-white font-bold text-xs flex items-center gap-1">
									<Clock class="w-4 h-4 text-brand-accent" /> {{ offer.timeLeft }}
								</span>
							</div>
							<h1 class="text-2xl font-black text-white leading-tight mb-1 animate-fade-in-up" style="animation-delay: 100ms">{{ offer.title }}</h1>
							<p class="text-white/80 text-sm font-medium animate-fade-in-up" style="animation-delay: 150ms">{{ offer.subtitle }}</p>
						</div>
					</div>

					<!-- Offer Highlights/Badges -->
					<div class="p-4 flex gap-3 overflow-x-auto no-scrollbar -mt-6 relative z-10 animate-fade-in-up" style="animation-delay: 200ms">
						<div class="flex-shrink-0 px-4 py-3 app-card rounded-[1.5rem] shadow-glass flex items-center gap-3">
							<div class="w-10 h-10 bg-brand-primary/10 rounded-xl flex items-center justify-center border border-brand-primary/20">
								<Zap class="w-5 h-5 text-brand-primary fill-brand-primary" />
							</div>
							<div class="flex flex-col">
								<span class="text-[10px] text-gray-500 font-bold uppercase leading-none mb-1 tracking-wider">Discount</span>
								<span class="text-sm font-black text-brand-primary leading-none">Up to {{ offer.maxDiscount }}% Off</span>
							</div>
						</div>
						<div class="flex-shrink-0 px-4 py-3 app-card rounded-[1.5rem] shadow-glass flex items-center gap-3">
							<div class="w-10 h-10 bg-orange-500/10 rounded-xl flex items-center justify-center border border-orange-500/20">
								<Truck class="w-5 h-5 text-orange-500" />
							</div>
							<div class="flex flex-col">
								<span class="text-[10px] text-gray-500 font-bold uppercase leading-none mb-1 tracking-wider">Delivery</span>
								<span class="text-sm font-black text-orange-500 leading-none">Free Delivery</span>
							</div>
						</div>
					</div>

					<!-- Description -->
					<div class="px-4 mb-8">
						<div class="app-card p-5 rounded-[2rem] border border-white/40 shadow-sm">
							<h3 class="text-xs font-black text-gray-900 dark:text-gray-100 mb-2 uppercase tracking-widest">About this offer</h3>
							<p class="text-sm text-gray-500 dark:text-gray-400 font-medium leading-relaxed">{{ offer.description }}</p>
						</div>
					</div>

					<!-- Products Section -->
					<div class="px-5 pb-32">
						<div class="flex items-center justify-between mb-5">
							<h2 class="text-lg font-black text-gray-900 dark:text-gray-100">Offer Items</h2>
							<span class="px-2.5 py-1 bg-brand-primary/10 text-brand-primary text-[10px] font-black rounded-lg uppercase tracking-wider">{{ offerItems.length }} Products</span>
						</div>
						<div class="grid grid-cols-2 gap-4">
							<ProductThumb
								v-for="product in offerItems"
								:key="product.id"
								:product="product"
								variant="vertical"
							/>
						</div>
					</div>
				</ion-content>

				<!-- Fixed CTA for the whole offer -->
				<div class="fixed bottom-0 left-0 right-0 p-5 app-card rounded-t-[2rem] backdrop-blur-3xl shadow-[0_-15px_40px_rgba(0,0,0,0.05)] border-t border-white/40 flex items-center justify-between z-20">
					<div class="flex flex-col px-2">
						<span class="text-[10px] text-gray-500 font-black uppercase tracking-[0.2em] leading-none mb-1">Promo Code</span>
						<span class="text-lg font-black bg-clip-text text-transparent bg-gradient-to-r from-brand-primary to-brand-secondary leading-none">DOCKTO25</span>
					</div>
					<button class="px-8 py-3.5 bg-gradient-to-tr from-brand-primary to-brand-secondary text-white font-black rounded-[1.2rem] shadow-neon active:scale-95 transition-all outline-none border-none">
						Copy Code
					</button>
				</div>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { ref, inject } from "vue"
import { IonContent } from "@ionic/vue"
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import AppHeader from "@/components/AppHeader.vue"
import ProductThumb from "@/components/ProductThumb.vue"
import { Share2, Clock, Zap, Truck } from "lucide-vue-next"

const __ = inject("$translate")

// Mock data
const offer = ref({
	title: "Winter Health Essentials",
	subtitle: "Stay safe and healthy this season",
	banner: "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?q=80&w=1000&auto=format&fit=crop",
	description: "Get exclusive discounts on top-rated healthcare products, vitamins, and supplements to keep you and your family protected through the cold months.",
	timeLeft: "2d 14h left",
	maxDiscount: 25,
})

const offerItems = ref([
	{ id: 1, name: "Napa Extra (Paracetamol)", manufacturer: "Beximco Pharma", price: 25.0, category: "Medicines", image: "https://via.placeholder.com/150?text=Napa", oldPrice: 30, discount_percent: 15 },
	{ id: 2, name: "Vitamin C 500mg", manufacturer: "Square Pharma", price: 150.0, category: "Wellness", image: "https://via.placeholder.com/150?text=VitC", oldPrice: 200, discount_percent: 25 },
	{ id: 6, name: "Sergel 20mg", manufacturer: "Healthcare Pharma", price: 70.0, category: "Medicines", image: "https://via.placeholder.com/150?text=Sergel", oldPrice: 85, discount_percent: 18 },
	{ id: 7, name: "Ceevit 250mg", manufacturer: "Square Pharma", price: 45.0, category: "Wellness", image: "https://via.placeholder.com/150?text=Ceevit", oldPrice: 60, discount_percent: 25 },
])
</script>

<style scoped>
.no-scrollbar::-webkit-scrollbar {
	display: none;
}
.no-scrollbar {
	-ms-overflow-style: none;
	scrollbar-width: none;
}
.transparent-content {
	--background: transparent;
}
</style>
