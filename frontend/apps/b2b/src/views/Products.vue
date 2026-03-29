<template>
	<BaseLayout :pageTitle="__('All Products')" :showHeader="false">
		<template #body>
			<div class="flex flex-col h-full bg-transparent overflow-hidden relative">
				<!-- Ambient Backdrop Effects Wrapper -->
				<div class="absolute inset-0 overflow-hidden pointer-events-none z-[-1]">
					<div class="absolute top-[-50px] right-[-100px] w-[300px] h-[300px] bg-brand-primary/20 blur-[80px] rounded-full"></div>
					<div class="absolute bottom-[10%] left-[-100px] w-[250px] h-[250px] bg-brand-secondary/20 blur-[80px] rounded-full"></div>
				</div>

				<!-- Search and Filter Header -->
				<AppHeader :title="__('All Products')" :showBack="true" :isScrolled="false" customClass="bg-white/70 dark:bg-black/70 backdrop-blur-xl shadow-[0_4px_30px_rgba(0,0,0,0.05)] z-10 animate-fade-in-up">
					<template #bottom>
						<div class="flex gap-2">
							<div class="relative flex-1 group">
								<Search class="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400 group-hover:text-brand-primary transition-colors z-10" />
								<input
									v-model="searchQuery"
									type="text"
									placeholder="Search medicine, vitamins..."
									class="w-full pl-10 pr-4 py-3 app-card border-none text-sm focus:ring-2 focus:ring-brand-primary transition-all bg-transparent group-hover:shadow-glass placeholder-gray-400"
									@keyup.enter="handleSearch"
								/>
							</div>
							<button
								@click="showFilters = true"
								class="p-3 app-card hover:shadow-neon active:scale-95 transition-all relative border-none"
							>
								<SlidersHorizontal class="w-5 h-5 text-gray-600 dark:text-gray-300" />
								<span v-if="activeFiltersCount > 0" class="absolute -top-1 -right-1 w-4 h-4 bg-brand-accent text-white text-[10px] rounded-full flex items-center justify-center border-2 border-white dark:border-gray-800 shadow-md">
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
									class="px-3 py-1.5 app-card !rounded-full text-gray-600 dark:text-gray-300 text-xs hover:border-brand-primary transition-colors border-none"
								>
									{{ term }}
								</button>
							</div>
						</div>
					</template>
				</AppHeader>

				<!-- Products Content -->
				<ion-content ref="contentRef" :scroll-events="true">
					<!-- Categories Horizontal Scroll -->
					<div class="p-4 overflow-x-auto flex gap-3 no-scrollbar animate-fade-in-up" style="animation-delay: 0.1s">
						<button
							v-for="cat in categories"
							:key="cat"
							@click="selectedCategory = cat"
							class="whitespace-nowrap px-5 py-2 rounded-full text-sm font-bold transition-all"
							:class="selectedCategory === cat ? 'bg-gradient-to-r from-brand-primary to-brand-secondary text-white shadow-neon drop-shadow-md' : 'app-card text-gray-600 dark:text-gray-300 border-none'"
						>
							{{ cat }}
						</button>
					</div>

					<!-- Products Grid/List Toggle Header -->
					<div class="px-4 mb-3 flex justify-between items-center animate-fade-in-up" style="animation-delay: 0.2s">
						<span class="text-xs font-bold text-gray-400 uppercase tracking-widest">{{ filteredProducts.length }} Products found</span>
						<div class="flex gap-1 app-card p-1">
							<button 
								@click="viewMode = 'grid'" 
								class="p-1 rounded-md transition-all active:scale-90"
								:class="viewMode === 'grid' ? 'bg-white dark:bg-gray-800 shadow-sm text-brand-primary' : 'text-gray-400 hover:text-gray-600'"
							>
								<LayoutGrid class="w-4 h-4" />
							</button>
							<button 
								@click="viewMode = 'list'" 
								class="p-1 rounded-md transition-all active:scale-90"
								:class="viewMode === 'list' ? 'bg-white dark:bg-gray-800 shadow-sm text-brand-primary' : 'text-gray-400 hover:text-gray-600'"
							>
								<List class="w-4 h-4" />
							</button>
						</div>
					</div>

					<!-- Products Display -->
					<div class="px-4 pb-24 relative">
						<template v-for="(group, letter) in groupedProducts" :key="letter">
							<div :id="'letter-' + letter" class="mb-6 scroll-mt-32">
								<div class="sticky top-0 z-10 backdrop-blur-xl bg-white/70 dark:bg-black/70 py-1 mb-3 rounded-lg flex items-center shadow-[0_4px_30px_rgba(0,0,0,0.05)] border border-white/40 dark:border-gray-800/80">
									<span class="w-7 h-7 flex items-center justify-center rounded-full bg-gradient-to-br from-brand-primary to-brand-secondary text-white font-bold shadow-neon text-xs ml-2">{{ letter }}</span>
								</div>
								<div :class="viewMode === 'grid' ? 'grid grid-cols-2 gap-4' : 'flex flex-col gap-3'">
									<ProductThumb
										v-for="product in group"
										:key="product.id"
										:product="product"
										:variant="viewMode === 'grid' ? 'vertical' : 'horizontal'"
									/>
								</div>
							</div>
						</template>
						
						<!-- Alphabetical Bar -->
						<div class="fixed right-2 top-1/2 -translate-y-1/2 z-50 flex flex-col items-center justify-center py-2 px-1 rounded-full bg-white/30 dark:bg-black/30 backdrop-blur-xl border border-white/40 dark:border-gray-700/50 shadow-[0_8px_32px_0_rgba(31,38,135,0.15)] opacity-40 hover:opacity-100 hover:bg-white/70 dark:hover:bg-black/70 transition-all duration-300 touch-none"
							@touchmove.prevent="handleAlphaScroll"
							@mousemove="handleAlphaScroll"
							@mouseleave="activeLetter = null"
							@touchend="activeLetter = null"
							ref="alphaBarRef"
						>
							<button 
								v-for="char in alphabet" 
								:key="char"
								@click="scrollToLetter(char)"
								class="text-[10px] sm:text-xs font-bold w-4 h-4 sm:w-5 sm:h-5 flex items-center justify-center rounded-full transition-all duration-200"
								:class="[
									availableLetters.includes(char) ? 'text-gray-800 dark:text-gray-100' : 'text-gray-400/40 cursor-not-allowed',
									activeLetter === char ? 'scale-150 -translate-x-3 bg-brand-primary text-white shadow-neon' : '',
									availableLetters.includes(char) && activeLetter !== char ? 'hover:scale-125 hover:-translate-x-2 hover:bg-brand-primary/20 hover:text-brand-primary' : ''
								]"
							>
								{{ char }}
							</button>
						</div>
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
import { ref, computed, inject } from "vue"
import { IonContent, IonModal, IonButton } from "@ionic/vue"
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import ProductThumb from "@/components/ProductThumb.vue"
import AppHeader from "@/components/AppHeader.vue"
import { Search, SlidersHorizontal, PackageSearch, LayoutGrid, List } from "lucide-vue-next"

const __ = inject("$translate")

const searchQuery = ref("")
const selectedCategory = ref("All")
const showFilters = ref(false)
const viewMode = ref("grid")
const activeFiltersCount = ref(0)
const recentSearches = ref(["Napa Extra", "Vitamin C", "Omega 3"])

const categories = ["All", "Medicines", "Wellness", "Personal Care", "Baby Care", "Nutrition"]

const alphabet = Array.from({ length: 26 }, (_, i) => String.fromCharCode(65 + i))
const contentRef = ref(null)
const alphaBarRef = ref(null)
const activeLetter = ref(null)

const handleAlphaScroll = (e) => {
	if (e.type === 'mousemove' && e.buttons !== 1) return;
	
	const clientY = e.touches ? e.touches[0].clientY : e.clientY;
	const clientX = e.touches ? e.touches[0].clientX : e.clientX;
	
	const el = document.elementFromPoint(clientX, clientY);
	if (el && el.tagName === 'BUTTON' && el.parentElement === alphaBarRef.value) {
		const letter = el.innerText.trim();
		if (letter && availableLetters.value.includes(letter) && activeLetter.value !== letter) {
			activeLetter.value = letter;
			scrollToLetter(letter, 'auto');
		}
	}
}

const scrollToLetter = (letter, behavior = 'smooth') => {
	if (!availableLetters.value.includes(letter)) return;
	
	activeLetter.value = letter;
	setTimeout(() => {
		if (activeLetter.value === letter && behavior === 'smooth') {
			activeLetter.value = null;
		}
	}, 1000);

	const el = document.getElementById('letter-' + letter);
	if (el) {
		el.scrollIntoView({ behavior: behavior, block: 'start' });
	}
}

const products = ref([
	{ id: 1, item_name: "Napa Extra (Paracetamol)", manufacturer: "Beximco Pharma", price: 25.0, category: "Medicines", image: "https://via.placeholder.com/150?text=Napa", oldPrice: 30 },
	{ id: 2, item_name: "Vitamin C 500mg", manufacturer: "Square Pharma", price: 150.0, category: "Wellness", image: "https://via.placeholder.com/150?text=VitC" },
	{ id: 3, item_name: "Hand Sanitizer 250ml", manufacturer: "ACI Limited", price: 220.0, category: "Personal Care", image: "https://via.placeholder.com/150?text=Sanitizer" },
	{ id: 4, item_name: "Baby Lotion 200ml", manufacturer: "Johnson's", price: 450.0, category: "Baby Care", image: "https://via.placeholder.com/150?text=Lotion", oldPrice: 500 },
	{ id: 5, item_name: "Horlicks Chocolate 500g", manufacturer: "Unilever", price: 580.0, category: "Nutrition", image: "https://via.placeholder.com/150?text=Horlicks" },
	{ id: 6, item_name: "Sergel 20mg", manufacturer: "Healthcare Pharma", price: 70.0, category: "Medicines", image: "https://via.placeholder.com/150?text=Sergel" },
])

const filteredProducts = computed(() => {
	return products.value.filter(p => {
		const matchesSearch = p.item_name.toLowerCase().includes(searchQuery.value.toLowerCase())
		const matchesCategory = selectedCategory.value === "All" || p.category === selectedCategory.value
		return matchesSearch && matchesCategory
	})
})

const sortedFilteredProducts = computed(() => {
	return [...filteredProducts.value].sort((a, b) => a.item_name.localeCompare(b.item_name))
})

const groupedProducts = computed(() => {
	const groups = {}
	sortedFilteredProducts.value.forEach(p => {
		const firstLetter = p.item_name.charAt(0).toUpperCase()
		const letter = /[A-Z]/.test(firstLetter) ? firstLetter : '#'
		if (!groups[letter]) groups[letter] = []
		groups[letter].push(p)
	})
	
	return Object.keys(groups).sort().reduce((res, key) => {
		res[key] = groups[key]
		return res
	}, {})
})

const availableLetters = computed(() => Object.keys(groupedProducts.value))

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
