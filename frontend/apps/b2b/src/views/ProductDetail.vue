<template>
	<BaseLayout :pageTitle="__('Product Details')" :showHeader="false">
		<template #body>
			<div class="flex flex-col h-full overflow-hidden relative">
				<AppHeader :title="__('Product Details')" :showBack="true" customClass="absolute w-full z-50 bg-white/50 dark:bg-gray-950/50 backdrop-blur-2xl pb-4 pt-12 shadow-glass border-b border-brand-primary/5">
					<template #actions>
						<button class="p-2 app-card !rounded-xl shadow-sm active:scale-90 transition-all">
							<Share2 class="w-5 h-5 text-gray-600 dark:text-gray-300" />
						</button>
					</template>
				</AppHeader>

				<!-- Ambient Backdrops -->
				<div class="absolute inset-0 overflow-hidden pointer-events-none -z-10" style="background: var(--app-bg);">
					<div class="ambient-orb top-0 right-0 w-[400px] h-[400px] bg-brand-primary/8"></div>
					<div class="ambient-orb bottom-0 left-[-100px] w-[300px] h-[300px] bg-brand-secondary/8"></div>
				</div>

				<ion-content class="ion-no-padding transparent-content px-2 pt-24 pb-32">
					<!-- Image Section -->
					<div class="relative w-full aspect-square mt-20 app-card mx-auto max-w-[95%] bg-white/60 dark:bg-gray-900/40 flex items-center justify-center p-8 overflow-hidden !rounded-[2.5rem] shadow-glass mb-8 z-10 animate-fade-in-up">
						<img
							:src="product.image"
							class="max-w-full max-h-full object-contain drop-shadow-2xl hover:scale-105 transition-transform duration-700 mix-blend-multiply dark:mix-blend-normal"
							alt="product image"
						/>

						<!-- Floating Badges -->
						<div class="absolute top-5 left-5 flex flex-col gap-2">
							<div v-if="discount" class="badge-discount shadow-neon-accent">
								{{ discount }} OFF
							</div>
							<div class="text-white text-[10px] font-bold px-3 py-1.5 rounded-xl shadow-neon" style="background: linear-gradient(135deg, #059669, #0891b2);">
								FREE DELIVERY
							</div>
						</div>

						<button class="absolute bottom-5 right-5 p-3 app-card !rounded-2xl shadow-sm border border-white/20 active:scale-90 transition-all hover:shadow-glass text-gray-400 hover:text-rose-500">
							<Heart class="w-5 h-5" />
						</button>
					</div>

					<!-- Info Section -->
					<div class="px-5 mb-6 animate-fade-in-up stagger-1">
						<div class="app-card-strong p-6 shadow-glass !rounded-[2rem]">
							<div class="flex flex-col gap-1 mb-5">
								<span class="text-[10px] font-bold text-brand-primary uppercase tracking-[0.2em]">{{ product.category }}</span>
								<h1 class="text-2xl font-extrabold text-gray-900 dark:text-gray-100 leading-tight">{{ product.name }}</h1>
								<p class="text-xs font-medium text-gray-400">By {{ product.manufacturer }}</p>
							</div>

							<!-- Pricing -->
							<div class="flex items-end gap-3 pb-5 border-b border-gray-100 dark:border-gray-800">
								<span class="text-3xl font-black price-text tracking-tighter py-1" :class="{'opacity-50 blur-[2px]': isPriceLoading}">৳{{ Number(currentPrice || 0).toFixed(2) }}</span>
								<div v-if="(customOldPrice || product.oldPrice) && (customOldPrice || product.oldPrice) > currentPrice" class="flex flex-col mb-1.5">
									<span class="text-xs text-gray-400 line-through font-medium">৳{{ Number(customOldPrice || product.oldPrice).toFixed(2) }}</span>
									<span v-if="discountPercent" class="text-[9px] font-bold text-emerald-600 leading-none bg-emerald-50 dark:bg-emerald-900/30 px-2 py-1 rounded-md">{{ discountPercent }}% OFF</span>
								</div>
							</div>

							<!-- Out of stock indicator or Badge -->
							<div v-if="product.stock_qty <= 0" class="py-5 border-b border-gray-100 dark:border-gray-800">
                                <div class="w-full bg-rose-50 dark:bg-rose-900/20 text-rose-600 border border-rose-100 dark:border-rose-900/50 p-4 rounded-2xl flex items-center gap-3">
                                    <div class="w-8 h-8 rounded-full bg-rose-100 dark:bg-rose-900/50 flex items-center justify-center font-bold">!</div>
                                    <div>
                                        <h4 class="text-sm font-bold">Temporarily Out of Stock</h4>
                                        <p class="text-xs mt-0.5 opacity-80">Check back later or view substitutes below.</p>
                                    </div>
                                </div>
                            </div>
                            <!-- Removed Mock Pricing Tiers UI since ERPNext handles dynamic pricing transparently -->

							<!-- Pack Size Selection -->
							<div class="py-5 border-b border-gray-100 dark:border-gray-800">
								<h3 class="text-xs font-bold text-gray-700 dark:text-gray-300 mb-3 uppercase tracking-wider">Select Pack Size</h3>
								<div class="flex gap-2.5 overflow-x-auto no-scrollbar pb-1">
									<button
										v-for="(size, idx) in packSizes"
										:key="size"
										@click="selectedPack = idx"
										class="whitespace-nowrap px-5 py-2.5 rounded-xl text-xs font-bold transition-all duration-300 border"
										:class="selectedPack === idx ? 'bg-gradient-to-r from-brand-primary to-brand-secondary text-white border-transparent shadow-neon' : 'app-card text-gray-500 border-gray-200 dark:border-gray-700 hover:border-brand-primary/30'"
									>
										{{ size }}
									</button>
								</div>
							</div>

							<!-- Features Grid -->
							<div class="grid grid-cols-2 gap-3 py-5">
								<div class="app-card p-3 !rounded-2xl flex items-center gap-3 shadow-sm">
									<div class="w-8 h-8 rounded-xl bg-emerald-50 dark:bg-emerald-900/30 text-emerald-500 flex items-center justify-center">
										<Zap class="w-4 h-4" />
									</div>
									<span class="text-[10px] font-bold text-gray-600 dark:text-gray-300 uppercase tracking-tight">Fast Acting</span>
								</div>
								<div class="app-card p-3 !rounded-2xl flex items-center gap-3 shadow-sm">
									<div class="w-8 h-8 rounded-xl bg-amber-50 dark:bg-amber-900/30 text-amber-500 flex items-center justify-center">
										<ShieldCheck class="w-4 h-4" />
									</div>
									<span class="text-[10px] font-bold text-gray-600 dark:text-gray-300 uppercase tracking-tight">Lab Tested</span>
								</div>
							</div>

							<!-- About Product -->
							<div class="pt-3">
								<h3 class="text-xs font-bold text-gray-700 dark:text-gray-300 mb-2 uppercase tracking-wider">About This Product</h3>
								<p class="text-xs text-gray-500 dark:text-gray-400 leading-relaxed font-medium">
									{{ product.description || "Comprehensive multi-vitamin formula designed to support your daily energy needs." }}
								</p>
							</div>
						</div>
					</div>

					<!-- Substitute Products -->
					<div v-if="product.substitutes && product.substitutes.length > 0" class="mb-10 px-5 animate-fade-in-up stagger-2">
						<SectionHeader title="Substitute Products" :showSeeAll="false" />
						<div class="flex gap-4 overflow-x-auto no-scrollbar pb-4 -mx-5 px-5 mt-2">
							<ProductThumb
								v-for="sub in product.substitutes"
								:key="sub.name"
								:product="sub"
								variant="minimal"
								@open-quick-add="() => {}"
							/>
						</div>
					</div>
				</ion-content>

				<!-- Fixed Bottom Bar -->
				<div class="app-card-strong fixed bottom-0 left-0 right-0 p-5 !rounded-t-[2rem] shadow-float border-t border-brand-primary/5 flex items-center gap-4 z-50 standalone:pb-10 transition-all font-sans">
					<!-- Quantity Controls -->
					<div class="flex items-center px-2 py-1.5 app-card !rounded-2xl shadow-inner-glow">
						<button
							@click="qty > 1 ? qty-- : null"
							class="w-9 h-9 flex items-center justify-center bg-white dark:bg-gray-800 rounded-xl shadow-sm active:scale-90 transition-all text-gray-500"
						>
							<Minus class="w-4 h-4" />
						</button>
						<span class="w-10 text-center text-sm font-black text-brand-primary">{{ qty }}</span>
						<button
							@click="qty++"
							class="w-9 h-9 flex items-center justify-center bg-white dark:bg-gray-800 rounded-xl shadow-sm active:scale-90 transition-all text-gray-500"
						>
							<Plus class="w-4 h-4" />
						</button>
					</div>

					<!-- Add to Cart -->
					<button class="flex-1 h-12 btn-primary !rounded-2xl flex items-center justify-center gap-2" @click="addToCart">
						<ShoppingCart class="w-4 h-4" />
						<span class="font-bold text-sm tracking-wide">Add to Cart — ৳{{ (currentPrice * qty).toFixed(2) }}</span>
					</button>
				</div>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { ref, computed, inject, watch, onMounted } from "vue"
import { useRoute } from "vue-router"
import { createResource, call } from "frappe-ui"
import { IonContent } from "@ionic/vue"
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import AppHeader from "@/components/AppHeader.vue"
import { Share2, Heart, Plus, Minus, ShoppingCart, Zap, ShieldCheck, Tags } from "lucide-vue-next"
import ProductThumb from "@/components/ProductThumb.vue"
import SectionHeader from "@/components/SectionHeader.vue"

const __ = inject("$translate")

const route = useRoute()
const qty = ref(1)
const selectedPack = ref(1)
const packSizes = ['10 Tablets', '30 Tablets', '50 Tablets']

const product = ref({})
const currentPrice = ref(0)
const customOldPrice = ref(0)
const discountPercent = ref(0)
const isPriceLoading = ref(false)

const productResource = createResource({
    url: 'erpnext.api.item_api.get_item_details',
    makeParams() {
        return { item_code: route.params.id }
    },
    onSuccess(data) {
        if (data) {
            product.value = data
            currentPrice.value = data.final_price || data.price || 0
            customOldPrice.value = data.price || 0
            discountPercent.value = data.discount_percent || 0
            
            // Log view
            call('erpnext.api.item_api.log_item_view', { item_code: route.params.id })
        }
    }
})

onMounted(() => {
    productResource.fetch()
})

const loadDynamicPrice = async () => {
    if (!product.value.name) return
    isPriceLoading.value = true
    try {
        const res = await call('erpnext.api.item_api.calculate_price', {
            item_code: product.value.name,
            qty: qty.value
        })
        if (res) {
            currentPrice.value = res.final_price || res.price || 0
            customOldPrice.value = res.price || 0
            discountPercent.value = res.discount_percent || 0
        }
    } catch (err) {
        currentPrice.value = product.value.final_price || product.value.price || 0
    } finally {
        isPriceLoading.value = false
    }
}

let priceTimeout;
watch(qty, () => {
    clearTimeout(priceTimeout)
    priceTimeout = setTimeout(() => {
        loadDynamicPrice()
    }, 400)
})

const discount = computed(() => {
    if (discountPercent.value > 0) {
        return discountPercent.value + "%"
    } else if (product.value.oldPrice && product.value.oldPrice > currentPrice.value) {
		const diff = product.value.oldPrice - currentPrice.value
		return Math.round((diff / product.value.oldPrice) * 100) + "%"
	}
	return null
})

const addToCart = () => {
	console.log("Added to cart:", product.value.name, "Qty:", qty.value, "Price:", currentPrice.value)
}
</script>

<style scoped>
.transparent-content {
	--background: transparent;
}
.no-scrollbar::-webkit-scrollbar {
	display: none;
}
.no-scrollbar {
	-ms-overflow-style: none;
	scrollbar-width: none;
}
</style>
