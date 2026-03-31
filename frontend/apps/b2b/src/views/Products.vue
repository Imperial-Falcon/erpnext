<template>
	<BaseLayout :pageTitle="__('All Products')" :showHeader="false">
		<template #body>
			<div class="flex flex-col h-full bg-transparent overflow-hidden relative">
				<!-- Ambient Backdrop -->
				<div class="absolute inset-0 overflow-hidden pointer-events-none z-[-1]">
					<div class="ambient-orb top-[-50px] right-[-100px] w-[300px] h-[300px] bg-brand-primary/15"></div>
					<div class="ambient-orb bottom-[10%] left-[-100px] w-[250px] h-[250px] bg-brand-secondary/12"></div>
				</div>

				<!-- Search and Filter Header -->
				<AppHeader :title="__('All Products')" :showBack="true" :isScrolled="false" customClass="bg-white/70 dark:bg-gray-950/70 backdrop-blur-2xl shadow-glass z-10 animate-fade-in-up">
					<template #bottom>
						<div class="flex gap-2">
							<div class="relative flex-1 group">
								<Search class="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400 group-hover:text-brand-primary transition-colors z-10" />
								<input
									v-model="searchQuery"
									type="text"
									placeholder="Search medicine, vitamins..."
									class="input-glass w-full !pl-10 !rounded-xl bg-transparent"
									@keyup.enter="handleSearch"
								/>
							</div>
							<button
								@click="showFilters = true"
								class="p-3 app-card !rounded-xl hover:shadow-glass active:scale-95 transition-all relative"
							>
								<SlidersHorizontal class="w-5 h-5 text-gray-600 dark:text-gray-300" />
								<span v-if="activeFiltersCount > 0" class="absolute -top-1 -right-1 w-4 h-4 text-white text-[10px] rounded-full flex items-center justify-center border-2 border-white dark:border-gray-800 shadow-md" style="background: linear-gradient(135deg, #f43f5e, #f97316);">
									{{ activeFiltersCount }}
								</span>
							</button>
						</div>

						<!-- Recent Searches -->
						<div v-if="recentSearches.length > 0 && !searchQuery" class="mt-4">
							<div class="flex justify-between items-center mb-2">
								<span class="text-xs font-bold text-gray-400 uppercase tracking-wider">Recent</span>
								<button @click="recentSearches = []" class="text-xs text-brand-primary font-semibold">Clear</button>
							</div>
							<div class="flex flex-wrap gap-2">
								<button
									v-for="term in recentSearches"
									:key="term"
									@click="searchQuery = term; handleSearch()"
									class="px-3 py-1.5 app-card !rounded-full text-gray-600 dark:text-gray-300 text-xs hover:shadow-glass transition-all duration-300"
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
					<div class="p-4 overflow-x-auto flex gap-3 no-scrollbar animate-fade-in-up stagger-1">
						<button
							v-for="cat in categories"
							:key="cat"
							@click="selectedCategory = cat"
							class="whitespace-nowrap px-5 py-2 rounded-full text-sm font-bold transition-all duration-300"
							:class="selectedCategory === cat ? 'bg-gradient-to-r from-brand-primary to-brand-secondary text-white shadow-neon' : 'app-card text-gray-600 dark:text-gray-300'"
						>
							{{ cat }}
						</button>
					</div>

					<!-- Recently Viewed Section -->
					<div v-if="!searchQuery && recentProducts.length > 0 && selectedCategory === 'All'" class="mb-4 px-4 animate-fade-in-up stagger-2">
						<div class="flex items-center justify-between mb-3 mt-2">
							<h3 class="text-sm font-extrabold text-gray-900 dark:text-gray-100">Recently Viewed</h3>
						</div>
						<div class="flex gap-4 overflow-x-auto no-scrollbar pb-4 -mx-4 px-4">
							<ProductThumb
								v-for="prod in recentProducts"
								:key="prod.name"
								:product="prod"
								variant="minimal"
								@open-quick-add="openQuickAdd"
							/>
						</div>
					</div>

					<!-- Products Grid/List Toggle -->
					<div class="px-4 mb-3 flex justify-between items-center animate-fade-in-up stagger-2">
						<span class="text-xs font-bold text-gray-400 uppercase tracking-widest">{{ filteredProducts.length }} Products</span>
						<div class="flex gap-1 app-card !rounded-xl p-1">
							<button
								@click="viewMode = 'grid'"
								class="p-1.5 rounded-lg transition-all active:scale-90"
								:class="viewMode === 'grid' ? 'bg-white dark:bg-gray-800 shadow-sm text-brand-primary' : 'text-gray-400 hover:text-gray-600'"
							>
								<LayoutGrid class="w-4 h-4" />
							</button>
							<button
								@click="viewMode = 'list'"
								class="p-1.5 rounded-lg transition-all active:scale-90"
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
								<div class="sticky top-0 z-10 backdrop-blur-2xl bg-white/60 dark:bg-gray-950/60 py-1 mb-3 rounded-xl flex items-center shadow-glass border border-brand-primary/5">
									<span class="w-7 h-7 flex items-center justify-center rounded-full bg-gradient-to-br from-brand-primary to-brand-secondary text-white font-bold shadow-neon text-xs ml-2">{{ letter }}</span>
								</div>
								<div :class="viewMode === 'grid' ? 'grid grid-cols-2 gap-4' : 'flex flex-col gap-3'">
									<ProductThumb
										v-for="product in group"
										:key="product.id"
										:product="product"
										:variant="viewMode === 'grid' ? 'vertical' : 'horizontal'"
										@open-quick-add="openQuickAdd"
									/>
								</div>
							</div>
						</template>

						<!-- Alphabetical Bar -->
						<div class="fixed right-1.5 top-1/2 -translate-y-1/2 z-50 flex flex-col items-center justify-center py-2 px-1 rounded-full bg-white/40 dark:bg-gray-950/40 backdrop-blur-2xl border border-brand-primary/5 shadow-glass opacity-40 hover:opacity-100 transition-all duration-300 touch-none"
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
									availableLetters.includes(char) ? 'text-gray-700 dark:text-gray-200' : 'text-gray-300/40 cursor-not-allowed',
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
						<PackageSearch class="w-16 h-16 text-gray-200 dark:text-gray-700 mb-4" />
						<h3 class="text-lg font-bold text-gray-900 dark:text-gray-100 mb-1">No products found</h3>
						<p class="text-sm text-gray-400">Try adjusting your filters or search terms.</p>
					</div>
					<!-- Infinite Scroll -->
					<ion-infinite-scroll @ionInfinite="loadMore">
						<ion-infinite-scroll-content loading-spinner="bubbles" loading-text="Loading more products..."></ion-infinite-scroll-content>
					</ion-infinite-scroll>
				</ion-content>

				<!-- Filter Modal -->
				<ion-modal :is-open="showFilters" @didDismiss="showFilters = false" :initial-breakpoint="0.5" :breakpoints="[0, 0.5, 0.8]">
					<div class="p-6 h-full" style="background: var(--glass-bg-strong); backdrop-filter: blur(40px);">
						<h2 class="text-xl font-extrabold text-gray-900 dark:text-gray-100 mb-6">Filters</h2>
						<div class="space-y-6">
							<div>
								<span class="text-sm font-bold text-gray-700 dark:text-gray-300 block mb-3">Price Range</span>
								<div class="flex gap-4">
									<input type="number" placeholder="Min" class="input-glass !rounded-xl" />
									<input type="number" placeholder="Max" class="input-glass !rounded-xl" />
								</div>
							</div>
							<button @click="showFilters = false" class="btn-primary w-full !py-4 !rounded-2xl mt-10 text-base">
								Apply Filters
							</button>
						</div>
					</div>
				</ion-modal>

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
import { ref, computed, inject, watch, onMounted } from "vue"
import { createResource } from "frappe-ui"
import { IonContent, IonModal, IonInfiniteScroll, IonInfiniteScrollContent } from "@ionic/vue"
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import ProductThumb from "@/components/ProductThumb.vue"
import AppHeader from "@/components/AppHeader.vue"
import QuickAddDrawer from "@/components/QuickAddDrawer.vue"
import { Search, SlidersHorizontal, PackageSearch, LayoutGrid, List } from "lucide-vue-next"

const __ = inject("$translate")

const searchQuery = ref("")
const selectedCategory = ref("All")
const showFilters = ref(false)
const viewMode = ref("grid")
const activeFiltersCount = ref(0)
const recentSearches = ref(["Napa Extra", "Vitamin C", "Omega 3"])

// Quick Add Drawer
const quickAddOpen = ref(false)
const quickAddProduct = ref(null)

const openQuickAdd = (product) => {
	quickAddProduct.value = product
	quickAddOpen.value = true
}

const handleAddToCart = (payload) => {
	console.log('Added to cart:', payload)
}

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

const products = ref([])
const page = ref(1)
const infiniteScrollDisabled = ref(false)

const productsResource = createResource({
	url: "erpnext.api.item_api.get_items",
	makeParams() {
		return {
			page: page.value,
			page_size: 20,
			search: searchQuery.value || null,
			item_group: selectedCategory.value === "All" ? null : selectedCategory.value,
		}
	},
	onSuccess(data) {
		if (!data || data.length < 20) {
			infiniteScrollDisabled.value = true
		} else {
			infiniteScrollDisabled.value = false
		}
		if (page.value === 1) {
			products.value = data || []
		} else if (data) {
			products.value = [...products.value, ...data]
		}
	}
})

const recentProducts = ref([])
const recentResource = createResource({
    url: "erpnext.api.item_api.get_recently_viewed_items",
    makeParams: () => ({ limit: 5 }),
    onSuccess(data) {
        if (data) recentProducts.value = data
    }
})

onMounted(() => {
	productsResource.fetch()
	recentResource.fetch()
})

const loadMore = async (ev) => {
	if (infiniteScrollDisabled.value) {
		ev.target.complete()
		ev.target.disabled = true
		return
	}
	page.value++
	await productsResource.fetch()
	ev.target.complete()
}

// Debounce search
let searchTimeout;
watch([searchQuery, selectedCategory], () => {
    clearTimeout(searchTimeout);
    searchTimeout = setTimeout(() => {
        page.value = 1
        productsResource.fetch()
    }, 400);
})

const filteredProducts = computed(() => products.value)

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
