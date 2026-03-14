<template>
	<BaseLayout pageTitle="All Products">
		<template #body>
			<div class="flex flex-col h-full bg-gray-50 overflow-hidden">
				<!-- Search and Filter Header -->
				<div class="bg-white p-4 shadow-sm z-10">
					<div class="flex gap-2">
						<div class="relative flex-1">
							<Search class="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" />
							<input
								v-model="searchQuery"
								type="text"
								placeholder="Search medicine, vitamins..."
								class="w-full pl-10 pr-4 py-3 bg-gray-100 border-none rounded-xl text-sm focus:ring-2 focus:ring-indigo-500 transition-all"
								@keyup.enter="handleSearch"
							/>
						</div>
						<button
							@click="showFilters = true"
							class="p-3 bg-gray-100 rounded-xl hover:bg-gray-200 transition-colors relative"
						>
							<SlidersHorizontal class="w-5 h-5 text-gray-600" />
							<span v-if="activeFiltersCount > 0" class="absolute -top-1 -right-1 w-4 h-4 bg-red-500 text-white text-[10px] rounded-full flex items-center justify-center border-2 border-white">
								{{ activeFiltersCount }}
							</span>
						</button>
					</div>

					<!-- Recent Searches -->
					<div v-if="recentSearches.length > 0 && !searchQuery" class="mt-4">
						<div class="flex justify-between items-center mb-2">
							<span class="text-xs font-bold text-gray-400 uppercase tracking-wider">Recent Searches</span>
							<button @click="recentSearches = []" class="text-xs text-indigo-600 font-semibold">Clear</button>
						</div>
						<div class="flex flex-wrap gap-2">
							<button
								v-for="term in recentSearches"
								:key="term"
								@click="searchQuery = term; handleSearch()"
								class="px-3 py-1.5 bg-gray-50 text-gray-600 text-xs rounded-full border border-gray-100 hover:border-indigo-200 transition-colors"
							>
								{{ term }}
							</button>
						</div>
					</div>
				</div>

				<!-- Products Content -->
				<ion-content>
					<!-- Categories Horizontal Scroll -->
					<div class="p-4 overflow-x-auto flex gap-3 no-scrollbar">
						<button
							v-for="cat in categories"
							:key="cat"
							@click="selectedCategory = cat"
							class="whitespace-nowrap px-5 py-2 rounded-full text-sm font-semibold transition-all"
							:class="selectedCategory === cat ? 'bg-indigo-600 text-white shadow-md' : 'bg-white text-gray-600 border border-gray-100'"
						>
							{{ cat }}
						</button>
					</div>

					<!-- Products Grid/List Toggle Header -->
					<div class="px-4 mb-3 flex justify-between items-center">
						<span class="text-xs font-bold text-gray-400">{{ filteredProducts.length }} Products found</span>
						<div class="flex gap-2 bg-gray-100 p-1 rounded-lg">
							<button 
								@click="viewMode = 'grid'" 
								class="p-1 rounded-md transition-all"
								:class="viewMode === 'grid' ? 'bg-white shadow-sm text-indigo-600' : 'text-gray-400'"
							>
								<LayoutGrid class="w-4 h-4" />
							</button>
							<button 
								@click="viewMode = 'list'" 
								class="p-1 rounded-md transition-all"
								:class="viewMode === 'list' ? 'bg-white shadow-sm text-indigo-600' : 'text-gray-400'"
							>
								<List class="w-4 h-4" />
							</button>
						</div>
					</div>

					<!-- Products Display -->
					<div 
						class="px-4 pb-24"
						:class="viewMode === 'grid' ? 'grid grid-cols-2 gap-4' : 'flex flex-col gap-3'"
					>
						<ProductThumb
							v-for="product in filteredProducts"
							:key="product.id"
							:product="product"
							:variant="viewMode === 'grid' ? 'vertical' : 'horizontal'"
						/>
					</div>

					<!-- No Results -->
					<div v-if="filteredProducts.length === 0" class="flex flex-col items-center justify-center py-20 px-10 text-center">
						<PackageSearch class="w-16 h-16 text-gray-200 mb-4" />
						<h3 class="text-lg font-bold text-gray-900 mb-1">No products found</h3>
						<p class="text-sm text-gray-400">Try adjusting your filters or search terms.</p>
					</div>
				</ion-content>

				<!-- Filter Modal -->
				<ion-modal :is-open="showFilters" @didDismiss="showFilters = false" :initial-breakpoint="0.5" :breakpoints="[0, 0.5, 0.8]">
					<div class="p-6 bg-white h-full">
						<h2 class="text-xl font-bold mb-6">Filters</h2>
						<div class="space-y-6">
							<div>
								<span class="text-sm font-bold text-gray-900 block mb-3">Price Range</span>
								<div class="flex gap-4">
									<input type="number" placeholder="Min" class="w-full p-3 bg-gray-50 rounded-xl text-sm border-none" />
									<input type="number" placeholder="Max" class="w-full p-3 bg-gray-50 rounded-xl text-sm border-none" />
								</div>
							</div>
							<ion-button expand="block" mode="ios" @click="showFilters = false" class="mt-10 h-14 font-bold">
								Apply Filters
							</ion-button>
						</div>
					</div>
				</ion-modal>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { ref, computed } from "vue"
import { IonContent, IonModal, IonButton } from "@ionic/vue"
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import ProductThumb from "@/components/ProductThumb.vue"
import { Search, SlidersHorizontal, PackageSearch, LayoutGrid, List } from "lucide-vue-next"

const searchQuery = ref("")
const selectedCategory = ref("All")
const showFilters = ref(false)
const viewMode = ref("grid")
const activeFiltersCount = ref(0)
const recentSearches = ref(["Napa Extra", "Vitamin C", "Omega 3"])

const categories = ["All", "Medicines", "Wellness", "Personal Care", "Baby Care", "Nutrition"]

const products = ref([
	{ id: 1, name: "Napa Extra (Paracetamol)", manufacturer: "Beximco Pharma", price: 25.0, category: "Medicines", image: "https://via.placeholder.com/150?text=Napa", oldPrice: 30 },
	{ id: 2, name: "Vitamin C 500mg", manufacturer: "Square Pharma", price: 150.0, category: "Wellness", image: "https://via.placeholder.com/150?text=VitC" },
	{ id: 3, name: "Hand Sanitizer 250ml", manufacturer: "ACI Limited", price: 220.0, category: "Personal Care", image: "https://via.placeholder.com/150?text=Sanitizer" },
	{ id: 4, name: "Baby Lotion 200ml", manufacturer: "Johnson's", price: 450.0, category: "Baby Care", image: "https://via.placeholder.com/150?text=Lotion", oldPrice: 500 },
	{ id: 5, name: "Horlicks Chocolate 500g", manufacturer: "Unilever", price: 580.0, category: "Nutrition", image: "https://via.placeholder.com/150?text=Horlicks" },
	{ id: 6, name: "Sergel 20mg", manufacturer: "Healthcare Pharma", price: 70.0, category: "Medicines", image: "https://via.placeholder.com/150?text=Sergel" },
])

const filteredProducts = computed(() => {
	return products.value.filter(p => {
		const matchesSearch = p.name.toLowerCase().includes(searchQuery.value.toLowerCase())
		const matchesCategory = selectedCategory.value === "All" || p.category === selectedCategory.value
		return matchesSearch && matchesCategory
	})
})

const handleSearch = () => {
	if (searchQuery.value && !recentSearches.value.includes(searchQuery.value)) {
		recentSearches.value.unshift(searchQuery.value)
		if (recentSearches.value.length > 5) recentSearches.value.pop()
	}
}
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
