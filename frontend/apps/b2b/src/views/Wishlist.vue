<template>
	<BaseLayout pageTitle="Wishlist">
		<template #body>
			<div class="flex flex-col h-full bg-gray-50 overflow-hidden">
				<!-- Wishlist Header -->
				<div class="bg-white p-4 shadow-sm z-10">
					<h1 class="text-xl font-black text-gray-900 mb-1">My Wishlist</h1>
					<p class="text-xs text-gray-400 font-medium">{{ wishlistItems.length }} favorited items</p>
				</div>

				<ion-content>
					<!-- Wishlist Grid -->
					<div v-if="wishlistItems.length > 0" class="p-4 grid grid-cols-2 gap-4 pb-24">
						<ProductThumb
							v-for="product in wishlistItems"
							:key="product.id"
							:product="product"
							variant="vertical"
						/>
					</div>

					<!-- Empty Wishlist State -->
					<div v-else class="flex flex-col items-center justify-center py-24 px-10 text-center">
						<div class="w-24 h-24 bg-red-50 rounded-full flex items-center justify-center mb-6">
							<Heart class="w-10 h-10 text-red-400 fill-red-400/20" />
						</div>
						<h3 class="text-lg font-bold text-gray-900 mb-2">Your wishlist is empty</h3>
						<p class="text-sm text-gray-400 mb-8 max-w-[240px]">Save your favorite products to find them later and get notified about price drops.</p>
						<button 
							@click="$router.push('/products')"
							class="w-full py-4 bg-indigo-600 text-white font-bold rounded-2xl shadow-lg shadow-indigo-100 active:scale-95 transition-all"
						>
							Start Shopping
						</button>
					</div>
				</ion-content>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { ref } from "vue"
import { IonContent } from "@ionic/vue"
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import ProductThumb from "@/components/ProductThumb.vue"
import { Heart } from "lucide-vue-next"

// Mock data - in a real app, this would be reactive from a store or fetched from an API
const wishlistItems = ref([
	{ id: 1, name: "Napa Extra (Paracetamol)", manufacturer: "Beximco Pharma", price: 25.0, category: "Medicines", image: "https://via.placeholder.com/150?text=Napa", oldPrice: 30 },
	{ id: 3, name: "Hand Sanitizer 250ml", manufacturer: "ACI Limited", price: 220.0, category: "Personal Care", image: "https://via.placeholder.com/150?text=Sanitizer" },
	{ id: 5, name: "Horlicks Chocolate 500g", manufacturer: "Unilever", price: 580.0, category: "Nutrition", image: "https://via.placeholder.com/150?text=Horlicks" },
])
</script>
