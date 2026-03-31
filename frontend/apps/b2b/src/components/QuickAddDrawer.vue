<template>
	<Teleport to="body">
		<!-- Backdrop -->
		<Transition name="backdrop">
			<div
				v-if="isOpen"
				class="drawer-backdrop"
				@click="close"
			></div>
		</Transition>

		<!-- Drawer -->
		<Transition name="drawer">
			<div v-if="isOpen" class="drawer-content standalone:pb-safe-bottom">
				<!-- Drag Handle -->
				<div class="flex justify-center pt-3 pb-2">
					<div class="w-10 h-1 rounded-full bg-gray-300 dark:bg-gray-600"></div>
				</div>

				<div class="px-5 pb-6">
					<!-- Product Info Row -->
					<div class="flex gap-4 mb-5">
						<!-- Image -->
						<div class="w-20 h-20 flex-shrink-0 app-card !rounded-2xl p-2 flex items-center justify-center bg-white/60 dark:bg-gray-800/40">
							<img
								:src="product?.image"
								:alt="product?.item_name"
								class="max-w-full max-h-full object-contain"
							/>
						</div>

						<!-- Name + Manufacturer -->
						<div class="flex-1 flex flex-col justify-center min-w-0">
							<h3 class="text-base font-extrabold text-gray-900 dark:text-gray-100 leading-tight line-clamp-2">
								{{ product?.item_name }}
							</h3>
							<p class="text-xs font-medium text-gray-400 dark:text-gray-500 mt-1">
								{{ product?.manufacturer || product?.brand || 'Unknown' }}
							</p>
						</div>
					</div>

					<!-- Single Price (fallback) -->
					<div class="mb-5 flex items-baseline gap-2">
						<span class="text-2xl font-black price-text py-1 inline-block" :class="{'opacity-50 blur-[2px]': isPriceLoading}">
							৳{{ Number(currentPrice || 0).toFixed(2) }}
						</span>
						<span v-if="(customOldPrice || product?.oldPrice || product?.mrp) && (customOldPrice || product?.oldPrice || product?.mrp) > currentPrice" class="text-sm text-gray-400 line-through font-medium">
							৳{{ Number(customOldPrice || product?.oldPrice || product?.mrp).toFixed(2) }}
						</span>
						
						<span v-if="discountPercent" class="badge-discount !relative !ml-2 text-[10px] !px-2 !py-0.5 shadow-sm">
							{{ discountPercent }}% OFF
						</span>
					</div>

					<!-- Quantity Selector + Current Total -->
					<div class="flex items-center justify-between mb-5">
						<div class="flex items-center gap-1 app-card !rounded-2xl px-2 py-1.5 !shadow-inner-glow">
							<button
								@click="qty > 1 ? qty-- : null"
								class="w-9 h-9 flex items-center justify-center rounded-xl bg-white dark:bg-gray-800 shadow-sm active:scale-90 transition-all text-gray-500"
							>
								<Minus class="w-4 h-4" />
							</button>
							<span class="w-12 text-center text-base font-black text-brand-primary">{{ qty }}</span>
							<button
								@click="qty++"
								class="w-9 h-9 flex items-center justify-center rounded-xl bg-white dark:bg-gray-800 shadow-sm active:scale-90 transition-all text-gray-500"
							>
								<Plus class="w-4 h-4" />
							</button>
						</div>

						<div class="text-right">
							<p class="text-[10px] font-medium text-gray-400 uppercase tracking-wider">Total</p>
							<p class="text-xl font-black price-text">
								৳{{ (currentPrice * qty).toFixed(2) }}
							</p>
						</div>
					</div>

					<!-- Action Buttons -->
					<div class="flex gap-3">
						<button
							@click="goToDetail"
							class="flex-1 py-3.5 app-card !rounded-2xl text-sm font-bold text-gray-700 dark:text-gray-300 flex items-center justify-center gap-2 active:scale-95 transition-all border border-gray-200 dark:border-gray-700"
						>
							<ExternalLink class="w-4 h-4" />
							Details
						</button>
						<button
							@click="handleAddToCart"
							class="flex-[2] py-3.5 btn-primary !rounded-2xl flex items-center justify-center gap-2"
						>
							<ShoppingCart class="w-4 h-4" />
							<span>Add to Cart</span>
						</button>
					</div>
				</div>
			</div>
		</Transition>
	</Teleport>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { call } from 'frappe-ui'
import { Plus, Minus, ShoppingCart, ExternalLink } from 'lucide-vue-next'

const props = defineProps({
	isOpen: {
		type: Boolean,
		default: false,
	},
	product: {
		type: Object,
		default: () => ({}),
	},
})

const emit = defineEmits(['close', 'add-to-cart'])

const router = useRouter()
const qty = ref(1)

const currentPrice = ref(0)
const customOldPrice = ref(0)
const discountPercent = ref(0)
const isPriceLoading = ref(false)

const loadDynamicPrice = async () => {
	if (!props.product?.name) return
	
	isPriceLoading.value = true
	try {
        const res = await call('erpnext.api.item_api.calculate_price', {
            item_code: props.product.name,
            qty: qty.value
        })
        if (res) {
            currentPrice.value = res.final_price || res.price || 0
            customOldPrice.value = res.price || 0
            discountPercent.value = res.discount_percent || 0
        }
    } catch (err) {
        console.error("Failed to load dynamic price", err)
        currentPrice.value = props.product.final_price || props.product.price || 0
    } finally {
        isPriceLoading.value = false
    }
}

// Reset qty when product changes and load price
let priceTimeout;
watch(() => props.product, () => {
	qty.value = 1
	currentPrice.value = props.product?.final_price || props.product?.price || 0
	customOldPrice.value = props.product?.price || 0
	discountPercent.value = props.product?.discount_percent || 0
	loadDynamicPrice()
}, { immediate: true })

watch(qty, () => {
    clearTimeout(priceTimeout)
    priceTimeout = setTimeout(() => {
        loadDynamicPrice()
    }, 400)
})

const close = () => {
	emit('close')
}

const goToDetail = () => {
	close()
	router.push(`/product/${props.product?.name || props.product?.id}`)
}

const handleAddToCart = () => {
	emit('add-to-cart', {
		product: props.product,
		qty: qty.value,
		price: currentPrice.value,
	})
	close()
}
</script>

<style scoped>
/* Backdrop transition */
.backdrop-enter-active,
.backdrop-leave-active {
	transition: opacity 0.3s ease;
}
.backdrop-enter-from,
.backdrop-leave-to {
	opacity: 0;
}

/* Drawer transition */
.drawer-enter-active {
	transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s ease;
}
.drawer-leave-active {
	transition: transform 0.3s cubic-bezier(0.4, 0, 1, 1), opacity 0.2s ease;
}
.drawer-enter-from {
	transform: translateY(100%);
	opacity: 0;
}
.drawer-leave-to {
	transform: translateY(100%);
	opacity: 0;
}
</style>
