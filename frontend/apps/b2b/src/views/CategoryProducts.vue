<template>
	<BaseLayout :pageTitle="categoryName" :showHeader="false">
		<template #body>
			<div class="flex flex-col h-full overflow-hidden relative">
				<AppHeader
					:title="categoryName"
					:showBack="true"
					:isScrolled="false"
					customClass="bg-white/70 dark:bg-gray-950/70 backdrop-blur-2xl shadow-glass z-50 animate-fade-in-up border-b border-brand-primary/5"
				>
					<template #bottom>
						<div class="pb-3 text-center">
							<span class="inline-flex items-center gap-1.5 px-3 py-1 app-card !rounded-full">
								<span class="w-2 h-2 rounded-full bg-brand-primary animate-pulse"></span>
								<span class="text-[10px] font-bold text-gray-500 uppercase tracking-widest">{{ filteredProducts.length }} Products</span>
							</span>
						</div>
					</template>
				</AppHeader>

				<!-- Ambient Backdrops -->
				<div class="absolute inset-0 overflow-hidden pointer-events-none -z-10" style="background: var(--app-bg);">
					<div class="ambient-orb top-[20%] right-[-50px] w-[300px] h-[300px] bg-brand-primary/8"></div>
					<div class="ambient-orb bottom-[10%] left-[-50px] w-[250px] h-[250px] bg-brand-secondary/10"></div>
				</div>

				<ion-content class="transparent-content pt-2 pb-10">
					<!-- Products Grid -->
					<div v-if="filteredProducts.length > 0" class="p-4 grid grid-cols-2 gap-4 pb-24">
						<ProductThumb
							v-for="product in filteredProducts"
							:key="product.id"
							:product="product"
							variant="vertical"
							@open-quick-add="openQuickAdd"
						/>
					</div>

					<!-- Empty State -->
					<div v-else class="flex flex-col items-center justify-center py-20 px-10 text-center animate-fade-in-up stagger-1">
						<div class="w-24 h-24 app-card !rounded-full flex items-center justify-center mb-6 shadow-glass relative">
							<div class="absolute inset-0 bg-brand-primary/10 rounded-full animate-ping opacity-50"></div>
							<PackageSearch class="w-10 h-10 text-brand-primary" />
						</div>
						<h3 class="text-xl font-extrabold text-gray-900 dark:text-gray-100 mb-2">No products found</h3>
						<p class="text-sm text-gray-400 font-medium">There are currently no products in this category.</p>
						<button
							@click="$router.push('/products')"
							class="mt-8 btn-primary"
						>
							Browse All Products
						</button>
					</div>
				</ion-content>

				<!-- Quick Add Drawer -->
				<QuickAddDrawer
					:isOpen="quickAddOpen"
					:product="quickAddProduct"
					@close="quickAddOpen = false"
					@add-to-cart="handleAddToCart"
				/>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { ref, computed } from "vue"
import { useRoute } from "vue-router"
import { IonContent } from "@ionic/vue"
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import AppHeader from "@/components/AppHeader.vue"
import ProductThumb from "@/components/ProductThumb.vue"
import QuickAddDrawer from "@/components/QuickAddDrawer.vue"
import { PackageSearch } from "lucide-vue-next"

const route = useRoute()
const categoryName = computed(() => route.params.name || "Category")

const quickAddOpen = ref(false)
const quickAddProduct = ref(null)

const openQuickAdd = (product) => {
	quickAddProduct.value = product
	quickAddOpen.value = true
}

const handleAddToCart = (payload) => {
	console.log('Added to cart:', payload)
}

const products = ref([
	{ id: 1, name: 1, item_name: "Napa Extra (Paracetamol)", manufacturer: "Beximco Pharma", price: 25.0, category: "Medicines", image: "https://via.placeholder.com/150?text=Napa", oldPrice: 30 },
	{ id: 2, name: 2, item_name: "Vitamin C 500mg", manufacturer: "Square Pharma", price: 150.0, category: "Wellness", image: "https://via.placeholder.com/150?text=VitC" },
	{ id: 6, name: 6, item_name: "Sergel 20mg", manufacturer: "Healthcare Pharma", price: 70.0, category: "Medicines", image: "https://via.placeholder.com/150?text=Sergel" },
])

const filteredProducts = computed(() => {
	return products.value.filter(p => p.category.toLowerCase() === categoryName.value.toLowerCase())
})
</script>

<style scoped>
.transparent-content {
	--background: transparent;
}
</style>
