<template>
	<BaseLayout :pageTitle="__('Product Details')" :showHeader="false">
		<template #body>
			<div class="flex flex-col h-full overflow-hidden relative">
				<AppHeader :title="__('Product Details')" :showBack="true" customClass="absolute w-full z-50 bg-white/50 dark:bg-black/50 backdrop-blur-md pb-4 pt-12 shadow-[0_4px_30px_rgba(0,0,0,0.05)] border-b border-white/20">
					<template #actions>
						<button class="p-2 app-card !rounded-full shadow-[0_4px_30px_rgba(0,0,0,0.05)] active:scale-90 transition-all">
							<Share2 class="w-5 h-5 text-gray-700 dark:text-gray-300" />
						</button>
					</template>
				</AppHeader>

				<!-- Ambient Backdrops -->
				<div class="absolute inset-0 overflow-hidden pointer-events-none -z-10 bg-gray-50 dark:bg-black">
					<div class="absolute top-0 right-0 w-[400px] h-[400px] bg-brand-primary/10 blur-[100px] rounded-full"></div>
					<div class="absolute bottom-0 left-[-100px] w-[300px] h-[300px] bg-brand-secondary/10 blur-[100px] rounded-full"></div>
				</div>

				<ion-content class="ion-no-padding transparent-content px-2 pt-24 pb-32">
				<!-- Image Section -->
				<div class="relative w-full aspect-square mt-20 app-card mx-auto max-w-[95%] bg-white/60 dark:bg-gray-900/40 flex items-center justify-center p-8 overflow-hidden rounded-[2.5rem] shadow-glass mb-8 z-10 animate-fade-in-up">
					<img 
						:src="product.image" 
						class="max-w-full max-h-full object-contain drop-shadow-2xl hover:scale-105 transition-transform duration-700 mix-blend-multiply dark:mix-blend-normal" 
						alt="product image" 
					/>
					
					<!-- Floating Badges -->
					<div class="absolute top-5 left-5 flex flex-col gap-2">
						<div v-if="discount" class="bg-gradient-to-r from-red-500 to-orange-500 text-white text-[10px] font-black px-3 py-1.5 rounded-xl shadow-neon">
							{{ discount }} OFF
						</div>
						<div class="bg-gradient-to-r from-brand-primary to-brand-accent text-white text-[10px] font-black px-3 py-1.5 rounded-xl shadow-neon">
							FREE DELIVERY
						</div>
					</div>

					<button class="absolute bottom-5 right-5 p-3 app-card rounded-2xl shadow-sm border border-white/20 active:scale-90 transition-all hover:shadow-neon hover:text-brand-accent text-gray-400">
						<Heart class="w-5 h-5" />
					</button>
				</div>

				<!-- Info Section -->
				<div class="px-5 mb-10 animate-fade-in-up" style="animation-delay: 50ms;">
					<div class="app-card p-6 shadow-glass rounded-[2rem] border border-white/40">
						<div class="flex flex-col gap-1 mb-6">
							<span class="text-[10px] font-black text-brand-primary uppercase tracking-[0.2em]">{{ product.category }}</span>
							<h1 class="text-2xl font-black text-gray-900 dark:text-gray-100 leading-tight">{{ product.name }}</h1>
							<p class="text-xs font-bold text-gray-400">By {{ product.manufacturer }}</p>
						</div>

						<!-- Pricing -->
						<div class="flex items-end gap-3 pb-6 border-b border-gray-100 dark:border-gray-800">
							<span class="text-3xl font-black bg-clip-text text-transparent bg-gradient-to-r from-brand-primary to-brand-secondary tracking-tighter">{{ formatCurrency(product.price, "BDT") }}</span>
							<div v-if="product.oldPrice" class="flex flex-col mb-1.5">
								<span class="text-xs text-gray-400 line-through font-bold">{{ formatCurrency(product.oldPrice, "BDT") }}</span>
								<span class="text-[9px] font-black text-emerald-500 leading-none bg-emerald-50 dark:bg-emerald-900/30 px-2 py-1 rounded-sm">Save {{ formatCurrency(product.oldPrice - product.price, "BDT") }}</span>
							</div>
						</div>

						<!-- Selection Chips -->
						<div class="py-6 border-b border-gray-100 dark:border-gray-800">
							<h3 class="text-xs font-black text-gray-900 dark:text-gray-100 mb-3 uppercase tracking-wider">Select Pack Size</h3>
							<div class="flex gap-2.5 overflow-x-auto no-scrollbar pb-1">
								<button 
									v-for="size in ['10 Tablets', '30 Tablets', '50 Tablets']" 
									:key="size"
									class="whitespace-nowrap px-5 py-2.5 rounded-xl text-xs font-bold transition-all border"
									:class="size === '30 Tablets' ? 'bg-gradient-to-r from-brand-primary to-brand-secondary text-white border-transparent shadow-neon' : 'app-card text-gray-500 border-gray-200 dark:border-gray-700 hover:border-brand-primary/30'"
								>
									{{ size }}
								</button>
							</div>
						</div>

						<!-- Features Grid -->
						<div class="grid grid-cols-2 gap-3 py-6">
							<div class="app-card p-3 rounded-2xl flex items-center gap-3 border shadow-sm">
								<div class="w-8 h-8 rounded-lg bg-emerald-50 text-emerald-500 flex items-center justify-center">
									<Zap class="w-4 h-4" />
								</div>
								<span class="text-[10px] font-black text-gray-700 dark:text-gray-300 uppercase tracking-tight">Fast Acting</span>
							</div>
							<div class="app-card p-3 rounded-2xl flex items-center gap-3 border shadow-sm">
								<div class="w-8 h-8 rounded-lg bg-amber-50 text-amber-500 flex items-center justify-center">
									<ShieldCheck class="w-4 h-4" />
								</div>
								<span class="text-[10px] font-black text-gray-700 dark:text-gray-300 uppercase tracking-tight">Lab Tested</span>
							</div>
						</div>

						<!-- About Product -->
						<div class="pt-6">
							<h3 class="text-xs font-black text-gray-900 dark:text-gray-100 mb-2 uppercase tracking-wider">About This Product</h3>
							<p class="text-xs text-gray-500 dark:text-gray-400 leading-relaxed font-medium">
								{{ product.description || "Comprehensive multi-vitamin formula designed to support your daily energy needs." }}
							</p>
						</div>
					</div>
				</div>

				<!-- Related Products -->
					<div class="mb-10 px-5 animate-fade-in-up" style="animation-delay: 100ms;">
						<SectionHeader title="Frequently Bought Together" :showSeeAll="false" />
						<div class="flex gap-4 overflow-x-auto no-scrollbar pb-4 -mx-5 px-5 mt-2">
							<ProductThumb 
								v-for="i in 3" 
								:key="i" 
								:product="mockRelated[i-1]" 
								variant="minimal" 
							/>
						</div>
					</div>
				</ion-content>

				<!-- Fixed Bottom Bar -->
				<div class="app-card fixed bottom-0 left-0 right-0 p-5 rounded-t-[2rem] shadow-[0_-15px_40px_rgba(0,0,0,0.05)] border-t border-white/40 flex items-center gap-4 z-50 standalone:pb-10 transition-all font-sans">
					<!-- Quantity Controls -->
					<div class="flex items-center px-2 py-1.5 app-card shadow-inner border border-gray-100 dark:border-gray-800 rounded-[1.2rem]">
						<button 
							@click="qty > 1 ? qty-- : null"
							class="w-8 h-8 flex items-center justify-center app-card rounded-xl shadow-sm active:scale-90 transition-all text-gray-500"
						>
							<Minus class="w-4 h-4" />
						</button>
						<span class="w-10 text-center text-sm font-black text-brand-primary">{{ qty }}</span>
						<button 
							@click="qty++"
							class="w-8 h-8 flex items-center justify-center app-card rounded-xl shadow-sm active:scale-90 transition-all text-gray-500"
						>
							<Plus class="w-4 h-4" />
						</button>
					</div>

					<!-- Add to Cart -->
					<button class="flex-1 h-12 bg-gradient-to-tr from-brand-primary to-brand-secondary text-white rounded-[1.2rem] shadow-neon active:scale-95 transition-all flex items-center justify-center gap-2" @click="addToCart">
						<ShoppingCart class="w-4 h-4" />
						<span class="font-black text-sm tracking-wide">Add to Cart</span>
					</button>
				</div>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { ref, computed, inject } from "vue"
import { useRoute } from "vue-router"
import { IonContent } from "@ionic/vue"
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import AppHeader from "@/components/AppHeader.vue"
import { Share2, Heart, Plus, Minus, ShoppingCart, Zap, ShieldCheck } from "lucide-vue-next"
import { formatCurrency } from "@/utils/formatters"
import ProductThumb from "@/components/ProductThumb.vue"
import SectionHeader from "@/components/SectionHeader.vue"

const __ = inject("$translate")

const route = useRoute()
const qty = ref(1)

// Mock current product
const product = ref({
	id: route.params.id || 1,
	name: "Premium Multivitamin Complex",
	manufacturer: "BioLife Pharmaceuticals",
	category: "Wellness & Nutrition",
	price: 1250.0,
	oldPrice: 1500.0,
	image: "https://via.placeholder.com/300?text=Multivitamin",
	description: "BioLife Premium Multivitamin is a high-potency formula specifically engineered to support the active lifestyle of professionals. Packed with 24 essential minerals and vitamins, it provides long-lasting energy release and supports a healthy immune response throughout the day."
})

const mockRelated = [
	{ id: 101, name: "Omega 3 Ultra", price: 850, image: "https://via.placeholder.com/150?text=Omega" },
	{ id: 102, name: "Vitamin C Serum", price: 450, image: "https://via.placeholder.com/150?text=Serum" },
	{ id: 103, name: "Protein Shake", price: 3200, image: "https://via.placeholder.com/150?text=Protein" },
]

const discount = computed(() => {
	if (product.value.oldPrice && product.value.oldPrice > product.value.price) {
		const diff = product.value.oldPrice - product.value.price
		return Math.round((diff / product.value.oldPrice) * 100) + "%"
	}
	return null
})

const addToCart = () => {
	console.log("Added to cart:", product.value.name, "Qty:", qty.value)
}
</script>

<style scoped>
.transparent-content {
	--background: transparent;
}
</style>
