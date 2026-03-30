<template>
	<BaseLayout :pageTitle="__('Wishlist')" :showHeader="false">
		<template #body>
			<div class="flex flex-col h-full overflow-hidden relative" style="background: var(--app-bg);">
				<AppHeader :title="__('Wishlist')" :showBack="true" :isScrolled="true">
					<template #actions>
						<span class="text-[10px] font-black text-gray-400 uppercase tracking-widest">{{ wishlistItems.length }} items</span>
					</template>
				</AppHeader>

				<!-- Ambient Backdrops -->
				<div class="absolute inset-0 overflow-hidden pointer-events-none z-0">
					<div class="absolute top-[20%] left-[-50px] w-[300px] h-[300px] bg-brand-accent/10 blur-[80px] rounded-full"></div>
					<div class="absolute bottom-[30%] right-[-50px] w-[250px] h-[250px] bg-brand-primary/15 blur-[80px] rounded-full"></div>
				</div>

				<ion-content class="transparent-content">
					<div class="relative z-10">
						<!-- Wishlist Grid -->
						<div v-if="wishlistItems.length > 0" class="p-5 grid grid-cols-2 gap-4 pb-24">
							<ProductThumb
								v-for="product in wishlistItems"
								:key="product.id"
								:product="product"
								variant="vertical"
							/>
						</div>

						<!-- Empty Wishlist State -->
						<div v-else class="flex flex-col items-center justify-center py-24 px-10 text-center animate-fade-in-up">
							<div class="w-24 h-24 app-card rounded-full flex items-center justify-center mb-6 shadow-glass relative">
								<div class="absolute inset-0 bg-brand-accent/10 rounded-full animate-ping opacity-30"></div>
								<Heart class="w-10 h-10 text-brand-accent fill-brand-accent/20" />
							</div>
							<h3 class="text-lg font-black text-gray-900 dark:text-gray-100 mb-2">Your wishlist is empty</h3>
							<p class="text-sm text-gray-400 mb-8 max-w-[240px]">Save your favorite products to find them later and get notified about price drops.</p>
							<button
								@click="$router.push('/products')"
								class="w-full py-4 bg-gradient-to-tr from-brand-primary to-brand-secondary text-white font-black rounded-[1.2rem] shadow-neon active:scale-95 transition-all"
							>
								Start Shopping
							</button>
						</div>
					</div>
				</ion-content>
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
import { Heart } from "lucide-vue-next"

const __ = inject("$translate")

const wishlistItems = ref([
	{ id: 1, name: "wish-1", item_name: "Napa Extra (Paracetamol)", manufacturer: "Beximco Pharma", price: 25.0, category: "Medicines", image: "https://via.placeholder.com/150?text=Napa", oldPrice: 30 },
	{ id: 3, name: "wish-3", item_name: "Hand Sanitizer 250ml", manufacturer: "ACI Limited", price: 220.0, category: "Personal Care", image: "https://via.placeholder.com/150?text=Sanitizer" },
	{ id: 5, name: "wish-5", item_name: "Horlicks Chocolate 500g", manufacturer: "Unilever", price: 580.0, category: "Nutrition", image: "https://via.placeholder.com/150?text=Horlicks" },
])
</script>

<style scoped>
.transparent-content { --background: transparent; }
</style>
