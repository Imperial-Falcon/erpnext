<template>
	<BaseLayout :pageTitle="__('Special Offers')" :showHeader="false">
		<template #body>
			<div class="flex flex-col h-full bg-transparent overflow-hidden relative">
				<AppHeader :title="__('Special Offers')" :showBack="true" customClass="z-50 bg-white/70 dark:bg-gray-950/70 backdrop-blur-xl shadow-[0_4px_30px_rgba(0,0,0,0.05)] border-b border-brand-primary/5" />
				
				<!-- Ambient backdrops -->
				<div class="absolute inset-0 overflow-hidden pointer-events-none -z-10">
					<div class="absolute top-[10%] left-[-50px] w-[300px] h-[300px] bg-red-500/10 blur-[80px] rounded-full"></div>
					<div class="absolute bottom-[30%] right-[-50px] w-[250px] h-[250px] bg-brand-primary/10 blur-[80px] rounded-full"></div>
				</div>

				<ion-content class="transparent-content pb-10">
					<!-- Flash Sale Header -->
					<div class="p-5 bg-gradient-to-r from-red-500 to-orange-500 text-white shadow-neon relative overflow-hidden app-card mx-4 mt-6 rounded-[2rem]">
						<div class="absolute inset-0 bg-white/10 mix-blend-overlay"></div>
						<div class="flex justify-between items-center mb-4">
							<div>
								<h2 class="text-xl font-black uppercase tracking-tighter italic">Flash Sale</h2>
								<p class="text-xs opacity-90">Ending in 04:25:10</p>
							</div>
							<div class="flex gap-1">
								<div v-for="t in ['04', '25', '10']" :key="t" class="bg-white/20 backdrop-blur-md px-2 py-1 rounded text-sm font-bold">
									{{ t }}
								</div>
							</div>
						</div>
						
						<!-- Flash Sale Items (Minimal Scroll) -->
						<div class="flex gap-4 overflow-x-auto no-scrollbar pb-2">
							<ProductThumb 
								v-for="offer in mockOffers.slice(0, 3)" 
								:key="offer.id" 
								:product="offer" 
								variant="minimal" 
							/>
						</div>
					</div>

					<!-- Promotional Banners -->
					<div class="p-4 space-y-4">
						<div 
							@click="$router.push('/offer-detail/1')"
							class="relative h-40 rounded-2xl overflow-hidden shadow-lg group cursor-pointer"
						>
							<img src="https://picsum.photos/400/200?random=1" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
							<div class="absolute inset-0 bg-gradient-to-r from-black/60 to-transparent flex flex-col justify-center p-6 text-white">
								<span class="text-[10px] font-bold uppercase tracking-widest mb-1 text-yellow-400">Exclusive Deal</span>
								<h3 class="text-xl font-black leading-tight mb-2">Up to 50% Off<br/>on Vitamins</h3>
								<button class="w-fit px-4 py-1.5 bg-white text-black text-xs font-bold rounded-full">Shop Now</button>
							</div>
						</div>

						<div 
							@click="$router.push('/offer-detail/2')"
							class="relative h-40 rounded-2xl overflow-hidden shadow-lg group cursor-pointer"
						>
							<img src="https://picsum.photos/400/200?random=2" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
							<div class="absolute inset-0 bg-gradient-to-l from-black/60 to-transparent flex flex-col justify-center items-end p-6 text-white text-right">
								<span class="text-[10px] font-bold uppercase tracking-widest mb-1 text-green-400">New Arrival</span>
								<h3 class="text-xl font-black leading-tight mb-2">Organic Honey<br/>Flat 20% Off</h3>
								<button class="w-fit px-4 py-1.5 bg-indigo-600 text-white text-xs font-bold rounded-full">Explore</button>
							</div>
						</div>
					</div>

					<!-- Discounted Grid (Vertical Cards) -->
					<div class="px-5 pb-24">
						<div class="flex items-center justify-between mb-5">
							<h3 class="text-lg font-black text-gray-900 dark:text-gray-100">Best Deals for You</h3>
							<div class="w-8 h-8 rounded-xl bg-orange-50 text-orange-500 flex items-center justify-center">
								<BadgePercent class="w-5 h-5" />
							</div>
						</div>
						
						<div class="grid grid-cols-2 gap-4">
							<ProductThumb 
								v-for="offer in mockOffers" 
								:key="offer.id" 
								:product="offer" 
								variant="vertical" 
							/>
						</div>
					</div>
				</ion-content>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { inject } from "vue"
import { IonContent } from "@ionic/vue"
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import AppHeader from "@/components/AppHeader.vue"
import ProductThumb from "@/components/ProductThumb.vue"
import { BadgePercent } from "lucide-vue-next"

const __ = inject("$translate")

const mockOffers = [
	{ id: 1, name: "Omega 3 Capsules", price: 850, oldPrice: 1200, discount: "30%", image: "https://via.placeholder.com/150?text=Omega", manufacturer: "NutriLife" },
	{ id: 2, name: "Face Wash 150ml", price: 320, oldPrice: 450, discount: "25%", image: "https://via.placeholder.com/150?text=FaceWash", manufacturer: "Care+" },
	{ id: 3, name: "Whey Protein 1kg", price: 3800, oldPrice: 4500, discount: "BDT 700", image: "https://via.placeholder.com/150?text=Whey", manufacturer: "MusclePeak" },
	{ id: 4, name: "Green Tea 25 Bags", price: 180, oldPrice: 250, discount: "28%", image: "https://via.placeholder.com/150?text=GreenTea", manufacturer: "NatureSip" },
]
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
