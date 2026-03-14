<template>
	<BaseLayout pageTitle="Offer Detail">
		<template #body>
			<div class="flex flex-col h-full bg-gray-50 overflow-hidden">
				<!-- Navigation Bar -->
				<div class="bg-white p-4 shadow-sm z-10 flex items-center justify-between">
					<button @click="$router.back()" class="p-2 hover:bg-gray-100 rounded-full transition-colors">
						<ChevronLeft class="w-6 h-6 text-gray-700" />
					</button>
					<button class="p-2 hover:bg-gray-100 rounded-full transition-colors">
						<Share2 class="w-5 h-5 text-gray-600" />
					</button>
				</div>

				<ion-content>
					<!-- Promotional Banner -->
					<div class="relative w-full aspect-video overflow-hidden">
						<img :src="offer.banner" alt="Offer Banner" class="w-full h-full object-cover" />
						<div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent flex flex-col justify-end p-6">
							<div class="flex items-center gap-2 mb-2">
								<span class="px-3 py-1 bg-red-500 text-white text-[10px] font-black rounded-lg uppercase tracking-wider">
									Limited Offer
								</span>
								<span class="text-white/80 text-xs font-bold flex items-center gap-1">
									<Clock class="w-3.5 h-3.5" /> {{ offer.timeLeft }}
								</span>
							</div>
							<h1 class="text-2xl font-black text-white leading-tight mb-1">{{ offer.title }}</h1>
							<p class="text-white/90 text-sm font-medium">{{ offer.subtitle }}</p>
						</div>
					</div>

					<!-- Offer Highlights/Badges -->
					<div class="p-4 flex gap-3 overflow-x-auto no-scrollbar">
						<div class="flex-shrink-0 px-4 py-3 bg-white rounded-2xl border border-gray-100 shadow-sm flex items-center gap-3">
							<div class="w-10 h-10 bg-indigo-50 rounded-xl flex items-center justify-center">
								<Zap class="w-5 h-5 text-indigo-500 fill-indigo-500" />
							</div>
							<div class="flex flex-col">
								<span class="text-[10px] text-gray-400 font-bold uppercase leading-none mb-1 tracking-wider">Discount</span>
								<span class="text-sm font-black text-indigo-600 leading-none">Up to {{ offer.maxDiscount }}% Off</span>
							</div>
						</div>
						<div class="flex-shrink-0 px-4 py-3 bg-white rounded-2xl border border-gray-100 shadow-sm flex items-center gap-3">
							<div class="w-10 h-10 bg-orange-50 rounded-xl flex items-center justify-center">
								<Truck class="w-5 h-5 text-orange-500" />
							</div>
							<div class="flex flex-col">
								<span class="text-[10px] text-gray-400 font-bold uppercase leading-none mb-1 tracking-wider">Delivery</span>
								<span class="text-sm font-black text-orange-600 leading-none">Free Delivery</span>
							</div>
						</div>
					</div>

					<!-- Description -->
					<div class="px-4 mb-6">
						<div class="bg-white p-4 rounded-2xl border border-gray-100 shadow-sm">
							<h3 class="text-sm font-black text-gray-900 mb-2">About this offer</h3>
							<p class="text-xs text-gray-500 leading-relaxed">{{ offer.description }}</p>
						</div>
					</div>

					<!-- Products Section -->
					<div class="px-4 pb-24">
						<div class="flex items-center justify-between mb-4">
							<h2 class="text-lg font-black text-gray-900">Offer Items</h2>
							<span class="text-xs font-bold text-gray-400">{{ offerItems.length }} Products</span>
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
				<div class="fixed bottom-0 left-0 right-0 p-4 bg-white/80 backdrop-blur-md border-t border-gray-100 flex items-center justify-between z-20">
					<div class="flex flex-col">
						<span class="text-[10px] text-gray-400 font-bold uppercase tracking-widest leading-none mb-1">Promo Code</span>
						<span class="text-base font-black text-indigo-600 leading-none">DOCKTO25</span>
					</div>
					<button class="px-8 py-3.5 bg-indigo-600 text-white font-black rounded-2xl shadow-lg shadow-indigo-100 active:scale-95 transition-all">
						Copy Code
					</button>
				</div>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { ref } from "vue"
import { IonContent } from "@ionic/vue"
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import ProductThumb from "@/components/ProductThumb.vue"
import { ChevronLeft, Share2, Clock, Zap, Truck } from "lucide-vue-next"

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
</style>
