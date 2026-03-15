<template>
	<BaseLayout :pageTitle="categoryName">
		<template #body>
			<div class="flex flex-col h-full bg-gray-50 dark:bg-black overflow-hidden">
				<ion-content>
					<!-- Category Info Banner -->
					<div class="bg-white dark:bg-gray-900 p-6 shadow-sm border-b border-gray-50 dark:border-gray-800">
						<h1 class="text-2xl font-black text-gray-900 dark:text-gray-100 leading-tight">{{ categoryName }}</h1>
						<p class="text-sm text-gray-400 font-medium mt-1">{{ filteredProducts.length }} Products available in this category</p>
					</div>

					<!-- Products Grid -->
					<div v-if="filteredProducts.length > 0" class="p-4 grid grid-cols-2 gap-4 pb-24">
						<ProductThumb
							v-for="product in filteredProducts"
							:key="product.id"
							:product="product"
							variant="vertical"
						/>
					</div>

					<!-- Empty State -->
					<div v-else class="flex flex-col items-center justify-center py-20 px-10 text-center">
						<div class="w-20 h-20 bg-indigo-50 dark:bg-indigo-900/30 rounded-full flex items-center justify-center mb-4">
							<PackageSearch class="w-10 h-10 text-indigo-400" />
						</div>
						<h3 class="text-lg font-bold text-gray-900 dark:text-gray-100 mb-1">No products found</h3>
						<p class="text-sm text-gray-400">There are currently no products available in this category.</p>
						<button 
							@click="$router.push('/products')"
							class="mt-6 px-6 py-3 bg-indigo-600 text-white font-bold rounded-xl shadow-lg shadow-indigo-100 dark:shadow-none active:scale-95 transition-all"
						>
							Browse All Products
						</button>
					</div>
				</ion-content>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { ref, computed } from "vue"
import { useRoute } from "vue-router"
import { IonContent } from "@ionic/vue"
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import ProductThumb from "@/components/ProductThumb.vue"
import { ChevronLeft, PackageSearch } from "lucide-vue-next"

const route = useRoute()
const categoryName = computed(() => route.params.name || "Category")

// Mock data - in a real app, this would be fetched from an API based on category
const products = ref([
	{ id: 1, name: "Napa Extra (Paracetamol)", manufacturer: "Beximco Pharma", price: 25.0, category: "Medicines", image: "https://via.placeholder.com/150?text=Napa", oldPrice: 30 },
	{ id: 2, name: "Vitamin C 500mg", manufacturer: "Square Pharma", price: 150.0, category: "Wellness", image: "https://via.placeholder.com/150?text=VitC" },
	{ id: 6, name: "Sergel 20mg", manufacturer: "Healthcare Pharma", price: 70.0, category: "Medicines", image: "https://via.placeholder.com/150?text=Sergel" },
])

const filteredProducts = computed(() => {
	return products.value.filter(p => p.category.toLowerCase() === categoryName.value.toLowerCase())
})
</script>
