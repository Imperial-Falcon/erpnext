<template>
	<BaseLayout :pageTitle="__('Shopping Cart')" :showHeader="false">
		<template #body>
			<div class="flex flex-col h-full overflow-hidden relative" style="background: var(--app-bg);">
				<AppHeader :title="__('Shopping Cart')" :showBack="true" :isScrolled="false" customClass="bg-white/70 dark:bg-gray-950/70 backdrop-blur-2xl shadow-glass z-50 animate-fade-in-up border-b border-brand-primary/5" />

				<!-- Ambient Backdrops -->
				<div class="absolute inset-0 overflow-hidden pointer-events-none z-0">
					<div class="ambient-orb top-[20%] left-[-50px] w-[300px] h-[300px] bg-brand-primary/8"></div>
					<div class="ambient-orb bottom-[20%] right-[-50px] w-[250px] h-[250px] bg-brand-secondary/10"></div>
				</div>

				<!-- Cart Items List (Scrollable Area) -->
				<ion-content class="transparent-content pb-[160px]">
					<div v-if="cartItems.length > 0" class="p-5 space-y-4 relative z-10 pb-32">
						<div
							v-for="(item, index) in cartItems"
							:key="item.id"
							class="app-card rounded-[1.5rem] p-3 flex gap-3 shadow-glass border border-white/40 animate-fade-in-up"
							:style="`animation-delay: ${index * 50}ms`"
						>
							<!-- Product Image -->
							<div class="w-20 h-20 bg-white/50 dark:bg-gray-800/50 rounded-xl flex-shrink-0 flex items-center justify-center p-2 overflow-hidden border border-white/50 shadow-sm mix-blend-multiply dark:mix-blend-normal">
								<img :src="item.image" :alt="item.name" class="max-w-full max-h-full object-contain" />
							</div>

							<!-- Item Details -->
							<div class="flex-1 flex flex-col justify-between py-0.5">
								<div>
									<div class="flex justify-between items-start">
										<h3 class="text-sm font-black text-gray-900 dark:text-gray-100 line-clamp-1 leading-tight">
											{{ item.name }}
										</h3>
										<button @click="removeItem(item.id)" class="text-gray-400 hover:text-red-500 active:scale-90 transition-all ml-2 p-1 bg-gray-50/50 dark:bg-gray-800/50 rounded-lg">
											<Trash2 class="w-4 h-4" />
										</button>
									</div>
									<p class="text-[11px] font-bold text-gray-400 uppercase tracking-widest mt-1">{{ item.description }}</p>
								</div>

								<div class="flex items-center justify-between mt-2">
									<div class="flex flex-col">
										<span v-if="item.oldPrice" class="text-[10px] font-bold text-gray-500 line-through">
											{{ formatCurrency(item.oldPrice, "BDT") }}
										</span>
										<span class="text-sm font-black price-text">
											৳{{ formatCurrency(item.price, "BDT") }}
										</span>
									</div>

									<!-- Quantity Controls -->
									<div class="flex items-center px-1.5 py-1 app-card shadow-inner border border-gray-100 dark:border-gray-800 rounded-[1.2rem]">
										<button
											@click="decrementQty(item.id)"
											class="w-7 h-7 flex items-center justify-center app-card rounded-[0.8rem] shadow-sm text-gray-500 active:scale-95 transition-all"
											:disabled="item.qty <= 1"
											:class="{ 'opacity-30 cursor-not-allowed': item.qty <= 1 }"
										>
											<Minus class="w-3.5 h-3.5" />
										</button>
										<span class="w-8 text-center text-xs font-black text-brand-primary">
											{{ item.qty }}
										</span>
										<button
											@click="incrementQty(item.id)"
											class="w-7 h-7 flex items-center justify-center app-card rounded-[0.8rem] shadow-sm text-gray-500 active:scale-95 transition-all"
										>
											<Plus class="w-3.5 h-3.5" />
										</button>
									</div>
								</div>
							</div>
						</div>
					</div>

					<!-- Empty State -->
					<div v-else class="h-full flex flex-col items-center justify-center p-8 text-center mt-20 relative z-10 animate-fade-in-up">
						<div class="w-24 h-24 app-card rounded-full flex items-center justify-center mb-6 shadow-glass relative">
							<div class="absolute inset-0 bg-brand-primary/10 rounded-full animate-ping opacity-50"></div>
							<ShoppingCart class="w-10 h-10 text-brand-primary" />
						</div>
						<h3 class="text-xl font-black text-gray-900 dark:text-gray-100 mb-2">Your cart is empty</h3>
						<p class="text-gray-500 text-sm mb-8 px-8 font-medium">Looks like you haven't added anything to your cart yet.</p>
						<button
							class="btn-primary !px-10"
							@click="$router.push('/home')"
						>
							Start Shopping
						</button>
					</div>
				</ion-content>

				<!-- Fixed Bottom Summary & Checkout -->
				<div v-if="cartItems.length > 0" class="fixed bottom-0 left-0 right-0 app-card-strong !rounded-t-[2rem] border-t border-brand-primary/5 p-5 pb-8 space-y-4 shadow-float z-50 standalone:pb-12 animate-slide-up">
					<div class="space-y-2.5">
						<div class="flex justify-between text-sm text-gray-500 dark:text-gray-400 font-bold">
							<span>Subtotal</span>
							<span>{{ formatCurrency(subtotal, "BDT") }}</span>
						</div>
						<div class="flex justify-between text-sm text-brand-accent font-bold">
							<span>Discount</span>
							<span>- {{ formatCurrency(totalDiscount, "BDT") }}</span>
						</div>
						<div class="flex justify-between items-center pt-3 border-t border-gray-100 dark:border-gray-800 mt-1">
							<span class="text-sm font-black text-gray-900 dark:text-gray-100 uppercase tracking-widest">Total</span>
							<span class="text-2xl font-black price-text">৳{{ formatCurrency(total, "BDT") }}</span>
						</div>
					</div>

					<button
						class="w-full btn-primary flex items-center justify-center gap-2 !h-14 !rounded-2xl mt-2"
						@click="handleCheckout"
					>
						<span class="font-bold text-sm tracking-wide">Proceed to Checkout</span>
						<ArrowRight class="w-5 h-5 ml-1" />
					</button>
				</div>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { ref, computed, inject } from "vue"
import { useRouter } from "vue-router"
import { IonContent } from "@ionic/vue"
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import AppHeader from "@/components/AppHeader.vue"
import { ShoppingCart, Trash2, Plus, Minus, ArrowRight } from "lucide-vue-next"
import { formatCurrency } from "@/utils/formatters"

const __ = inject("$translate")
const router = useRouter()

// Mock data
const cartItems = ref([
	{
		id: 1,
		name: "Premium Multivitamin Capsules",
		description: "60 Capsules • Pack of 1",
		oldPrice: 1500.0,
		price: 1250.0,
		qty: 1,
		image: "https://via.placeholder.com/150?text=Vitamin",
	},
	{
		id: 2,
		name: "Whey Protein Isolate",
		description: "Chocolate Flavor • 1kg",
		oldPrice: 5000.0,
		price: 4500.0,
		qty: 2,
		image: "https://via.placeholder.com/150?text=Protein",
	},
	{
		id: 3,
		name: "Organic Honey",
		description: "Pure Raw Honey • 500g",
		oldPrice: 1000.0,
		price: 850.0,
		qty: 1,
		image: "https://via.placeholder.com/150?text=Honey",
	},
])

// Computed values
const subtotal = computed(() => {
	return cartItems.value.reduce((acc, item) => acc + (item.oldPrice || item.price) * item.qty, 0)
})

const totalDiscount = computed(() => {
	return cartItems.value.reduce((acc, item) => {
		const discount = item.oldPrice ? (item.oldPrice - item.price) * item.qty : 0
		return acc + discount
	}, 0)
})

const total = computed(() => {
	return subtotal.value - totalDiscount.value
})

// Methods
const incrementQty = (id) => {
	const item = cartItems.value.find((i) => i.id === id)
	if (item) item.qty++
}

const decrementQty = (id) => {
	const item = cartItems.value.find((i) => i.id === id)
	if (item && item.qty > 1) item.qty--
}

const removeItem = (id) => {
	cartItems.value = cartItems.value.filter((i) => i.id !== id)
}

const handleCheckout = () => {
	router.push("/checkout")
}
</script>

<style scoped>
.transparent-content {
	--background: transparent;
}
.animate-slide-up {
	animation: slideUp 0.4s cubic-bezier(0.16, 1, 0.3, 1) both;
}
@keyframes slideUp {
	from {
		transform: translateY(100%);
		opacity: 0;
	}
	to {
		transform: translateY(0);
		opacity: 1;
	}
}
</style>
