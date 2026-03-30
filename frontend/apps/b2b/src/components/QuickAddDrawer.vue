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

					<!-- Quantity Breaks Pricing Table -->
					<div v-if="pricingTiers.length > 0" class="mb-5">
						<h4 class="text-[11px] font-bold text-gray-500 dark:text-gray-400 uppercase tracking-widest mb-2.5">
							Quantity Pricing
						</h4>
						<div class="app-card !rounded-2xl overflow-hidden !border-brand-primary/10">
							<div
								v-for="(tier, idx) in pricingTiers"
								:key="idx"
								class="flex items-center justify-between px-4 py-2.5 transition-colors duration-200"
								:class="[
									idx !== pricingTiers.length - 1 ? 'border-b border-gray-100 dark:border-gray-800' : '',
									isActiveTier(tier) ? 'bg-brand-primary/5 dark:bg-brand-primary/10' : '',
								]"
							>
								<div class="flex items-center gap-2">
									<div
										class="w-2 h-2 rounded-full transition-all duration-300"
										:class="isActiveTier(tier) ? 'bg-brand-primary scale-125' : 'bg-gray-300 dark:bg-gray-600'"
									></div>
									<span class="text-sm font-semibold text-gray-700 dark:text-gray-300">
										{{ tier.min_qty }}–{{ tier.max_qty || '∞' }} {{ product?.uom || 'Box' }}
									</span>
								</div>
								<span
									class="text-sm font-extrabold"
									:class="isActiveTier(tier) ? 'text-brand-primary' : 'text-gray-500 dark:text-gray-400'"
								>
									৳{{ tier.price.toFixed(2) }}
								</span>
							</div>
						</div>
					</div>

					<!-- Single Price (fallback) -->
					<div v-else class="mb-5 flex items-baseline gap-2">
						<span class="text-2xl font-black price-text">
							৳{{ currentPrice.toFixed(2) }}
						</span>
						<span v-if="product?.oldPrice || product?.mrp" class="text-sm text-gray-400 line-through font-medium">
							৳{{ (product?.oldPrice || product?.mrp)?.toFixed(2) }}
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
import { ref, computed, watch } from 'vue'
import { useRouter } from 'vue-router'
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

// Reset qty when product changes
watch(() => props.product, () => {
	qty.value = 1
})

// Pricing tiers — can come from product.pricing_tiers or mock
const pricingTiers = computed(() => {
	if (props.product?.pricing_tiers && props.product.pricing_tiers.length > 0) {
		return props.product.pricing_tiers
	}
	// Fallback: generate mock tiers from product price
	if (props.product?.price) {
		const base = props.product.price
		return [
			{ min_qty: 1, max_qty: 5, price: base },
			{ min_qty: 6, max_qty: 10, price: Math.round(base * 0.95 * 100) / 100 },
			{ min_qty: 11, max_qty: null, price: Math.round(base * 0.9 * 100) / 100 },
		]
	}
	return []
})

const currentPrice = computed(() => {
	if (pricingTiers.value.length === 0) return props.product?.price || 0
	for (const tier of pricingTiers.value) {
		const max = tier.max_qty || Infinity
		if (qty.value >= tier.min_qty && qty.value <= max) {
			return tier.price
		}
	}
	return props.product?.price || 0
})

const isActiveTier = (tier) => {
	const max = tier.max_qty || Infinity
	return qty.value >= tier.min_qty && qty.value <= max
}

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
