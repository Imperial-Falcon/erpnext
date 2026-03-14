<template>
	<ion-page>
		<!-- Header with Back Button -->
		<ion-header class="ion-no-border" mode="ios">
			<ion-toolbar class="px-2">
				<ion-buttons slot="start">
					<ion-back-button default-href="/home" text="" class="text-gray-900"></ion-back-button>
				</ion-buttons>
				<ion-title class="text-base font-black">Product Details</ion-title>
				<ion-buttons slot="end">
					<button class="p-2 bg-gray-50 rounded-xl active:scale-90 transition-all mr-2">
						<Share2 class="w-5 h-5 text-gray-700" />
					</button>
				</ion-buttons>
			</ion-toolbar>
		</ion-header>

		<ion-content class="ion-no-padding">
			<div class="flex flex-col bg-white pb-32">
				<!-- Image Section -->
				<div class="relative w-full aspect-square bg-gray-50 flex items-center justify-center p-10 overflow-hidden">
					<img 
						:src="product.image" 
						class="max-w-full max-h-full object-contain drop-shadow-2xl hover:scale-105 transition-transform duration-500" 
						alt="product image" 
					/>
					
					<!-- Floating Badges -->
					<div class="absolute top-6 left-6 flex flex-col gap-2">
						<div v-if="discount" class="bg-red-500 text-white text-[10px] font-black px-3 py-1.5 rounded-full shadow-lg shadow-red-200">
							{{ discount }} OFF
						</div>
						<div class="bg-indigo-600 text-white text-[10px] font-black px-3 py-1.5 rounded-full shadow-lg shadow-indigo-200">
							FREE DELIVERY
						</div>
					</div>

					<button class="absolute bottom-6 right-6 p-3 bg-white rounded-full shadow-xl shadow-gray-200 border border-gray-100 active:scale-90 transition-all">
						<Heart class="w-5 h-5 text-gray-400" />
					</button>
				</div>

				<!-- Info Section -->
				<div class="px-6 pt-8">
					<div class="flex flex-col gap-1 mb-4">
						<span class="text-[11px] font-black text-indigo-600 uppercase tracking-widest">{{ product.category }}</span>
						<h1 class="text-2xl font-black text-gray-900 leading-tight">{{ product.name }}</h1>
						<p class="text-sm font-medium text-gray-400">By {{ product.manufacturer }}</p>
					</div>

					<!-- Pricing -->
					<div class="flex items-end gap-3 mb-8">
						<span class="text-3xl font-black text-indigo-600 tracking-tighter">{{ formatCurrency(product.price, "BDT") }}</span>
						<div v-if="product.oldPrice" class="flex flex-col">
							<span class="text-sm text-gray-400 line-through font-medium">{{ formatCurrency(product.oldPrice, "BDT") }}</span>
							<span class="text-[10px] font-black text-red-500 leading-none">Save {{ formatCurrency(product.oldPrice - product.price, "BDT") }}</span>
						</div>
					</div>

					<!-- Selection Chips (Example: Pack Size) -->
					<div class="mb-8">
						<h3 class="text-sm font-black text-gray-900 mb-4">Select Pack Size</h3>
						<div class="flex gap-3 overflow-x-auto no-scrollbar pb-2">
							<button 
								v-for="size in ['10 Tablets', '30 Tablets', '50 Tablets']" 
								:key="size"
								class="whitespace-nowrap px-6 py-3 rounded-2xl text-xs font-black border transition-all"
								:class="size === '30 Tablets' ? 'bg-indigo-600 text-white border-indigo-600 shadow-lg shadow-indigo-100' : 'bg-white text-gray-500 border-gray-100 hover:border-indigo-200'"
							>
								{{ size }}
							</button>
						</div>
					</div>

					<!-- Features Grid -->
					<div class="grid grid-cols-2 gap-4 mb-10">
						<div class="p-4 bg-emerald-50 rounded-2xl border border-emerald-100 flex items-center gap-3">
							<div class="w-8 h-8 rounded-xl bg-emerald-500 flex items-center justify-center">
								<Zap class="w-4 h-4 text-white" />
							</div>
							<span class="text-[11px] font-black text-emerald-800 uppercase tracking-tighter">Fast Acting</span>
						</div>
						<div class="p-4 bg-orange-50 rounded-2xl border border-orange-100 flex items-center gap-3">
							<div class="w-8 h-8 rounded-xl bg-orange-500 flex items-center justify-center">
								<ShieldCheck class="w-4 h-4 text-white" />
							</div>
							<span class="text-[11px] font-black text-orange-800 uppercase tracking-tighter">Lab Tested</span>
						</div>
					</div>

					<!-- About Product -->
					<div class="mb-10">
						<h3 class="text-sm font-black text-gray-900 mb-3">About This Product</h3>
						<p class="text-sm text-gray-500 leading-relaxed font-medium">
							{{ product.description || "Comprehensive multi-vitamin formula designed to support your daily energy needs and immune system. Contains high-potency Vitamin C, Vitamin D, and Zinc for maximum protection and vitality." }}
						</p>
					</div>

					<!-- Related Products -->
					<div class="mb-10">
						<SectionHeader title="Frequently Bought Together" :showSeeAll="false" />
						<div class="flex gap-4 overflow-x-auto no-scrollbar pb-4 -mx-6 px-6">
							<ProductThumb 
								v-for="i in 3" 
								:key="i" 
								:product="mockRelated[i-1]" 
								variant="minimal" 
							/>
						</div>
					</div>
				</div>
			</div>
		</ion-content>

		<!-- Fixed Bottom Bar -->
		<div class="fixed bottom-0 left-0 right-0 p-6 bg-white/80 backdrop-blur-xl border-t border-gray-100 flex items-center gap-4 z-50 standalone:pb-10">
			<!-- Quantity Controls -->
			<div class="flex items-center bg-gray-50 rounded-2xl p-1.5 border border-gray-100 shadow-inner">
				<button 
					@click="qty > 1 ? qty-- : null"
					class="w-10 h-10 flex items-center justify-center bg-white rounded-xl shadow-sm active:scale-90 transition-all"
				>
					<Minus class="w-4 h-4 text-gray-600" />
				</button>
				<span class="w-12 text-center text-sm font-black text-gray-900">{{ qty }}</span>
				<button 
					@click="qty++"
					class="w-10 h-10 flex items-center justify-center bg-white rounded-xl shadow-sm active:scale-90 transition-all"
				>
					<Plus class="w-4 h-4 text-gray-600" />
				</button>
			</div>

			<!-- Add to Cart -->
			<ion-button expand="block" mode="ios" class="checkout-btn h-14 flex-1 m-0" @click="addToCart">
				<div class="flex items-center gap-3">
					<ShoppingCart class="w-5 h-5" />
					<span class="font-black text-sm">Add to Cart</span>
				</div>
			</ion-button>
		</div>
	</ion-page>
</template>

<script setup>
import { ref, computed } from "vue"
import { useRoute } from "vue-router"
import { 
	IonPage, IonHeader, IonToolbar, IonButtons, IonBackButton, 
	IonTitle, IonContent, IonButton 
} from "@ionic/vue"
import { Share2, Heart, Plus, Minus, ShoppingCart, Zap, ShieldCheck } from "lucide-vue-next"
import { formatCurrency } from "@/utils/formatters"
import ProductThumb from "@/components/ProductThumb.vue"
import SectionHeader from "@/components/SectionHeader.vue"

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
.checkout-btn {
	--background: #4f46e5;
	--background-activated: #4338ca;
	--border-radius: 20px;
	--box-shadow: 0 12px 24px -6px rgba(79, 70, 229, 0.4);
}

ion-toolbar {
	--background: transparent;
	--border-width: 0;
}
</style>
