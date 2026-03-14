<template>
	<BaseLayout pageTitle="Shopping Cart">
		<template #body>
			<div class="flex flex-col h-full bg-gray-50 overflow-hidden">
				<!-- Cart Items List (Scrollable Area) -->
				<ion-content class="flex-1">
					<div v-if="cartItems.length > 0" class="p-4 space-y-4 pb-10">
						<div
							v-for="item in cartItems"
							:key="item.id"
							class="bg-white rounded-2xl p-3 flex gap-3 shadow-sm border border-gray-100"
						>
							<!-- Product Image -->
							<div class="w-20 h-20 bg-gray-50 rounded-xl flex-shrink-0 flex items-center justify-center p-2 overflow-hidden border border-gray-50">
								<img :src="item.image" :alt="item.name" class="max-w-full max-h-full object-contain" />
							</div>

							<!-- Item Details -->
							<div class="flex-1 flex flex-col justify-between py-0.5">
								<div>
									<div class="flex justify-between items-start">
										<h3 class="text-sm font-bold text-gray-900 line-clamp-1 leading-tight">
											{{ item.name }}
										</h3>
										<button @click="removeItem(item.id)" class="text-gray-300 hover:text-red-500 transition-colors ml-2">
											<Trash2 class="w-4 h-4" />
										</button>
									</div>
									<p class="text-[11px] text-gray-500 mt-0.5">{{ item.description }}</p>
								</div>

								<div class="flex items-center justify-between mt-2">
									<div class="flex flex-col">
										<span v-if="item.oldPrice" class="text-[10px] text-gray-400 line-through">
											{{ formatCurrency(item.oldPrice, "BDT") }}
										</span>
										<span class="text-sm font-extrabold text-indigo-600">
											{{ formatCurrency(item.price, "BDT") }}
										</span>
									</div>

									<!-- Quantity Controls -->
									<div class="flex items-center bg-gray-50 rounded-lg p-1 border border-gray-100">
										<button
											@click="decrementQty(item.id)"
											class="w-7 h-7 flex items-center justify-center bg-white rounded-md shadow-sm text-gray-600 active:bg-gray-100 transition-colors"
											:disabled="item.qty <= 1"
											:class="{ 'opacity-30 cursor-not-allowed': item.qty <= 1 }"
										>
											<Minus class="w-3.5 h-3.5" />
										</button>
										<span class="w-8 text-center text-xs font-bold text-gray-900">
											{{ item.qty }}
										</span>
										<button
											@click="incrementQty(item.id)"
											class="w-7 h-7 flex items-center justify-center bg-white rounded-md shadow-sm text-gray-600 active:bg-gray-100 transition-colors"
										>
											<Plus class="w-3.5 h-3.5" />
										</button>
									</div>
								</div>
							</div>
						</div>
					</div>

					<!-- Empty State -->
					<div v-else class="h-full flex flex-col items-center justify-center p-8 text-center mt-20">
						<div class="w-20 h-20 bg-white rounded-2xl flex items-center justify-center mb-6 shadow-xl shadow-gray-100">
							<ShoppingCart class="w-8 h-8 text-indigo-500" />
						</div>
						<h3 class="text-lg font-bold text-gray-900 mb-1">Your cart is empty</h3>
						<p class="text-gray-400 text-sm mb-8 px-10">Look like you haven't added anything to your cart yet.</p>
						<button
							class="px-10 py-3.5 bg-indigo-600 text-white font-bold rounded-2xl hover:bg-indigo-700 transition-all shadow-lg shadow-indigo-100 active:scale-95"
							@click="$router.push('/')"
						>
							Start Shopping
						</button>
					</div>
				</ion-content>

				<!-- Fixed Bottom Summary & Checkout -->
				<div v-if="cartItems.length > 0" class="bg-white border-t border-gray-100 p-5 pb-8 space-y-4 shadow-[0_-10px_30px_rgba(0,0,0,0.04)] z-50">
					<div class="space-y-2.5">
						<div class="flex justify-between text-sm text-gray-500 font-medium">
							<span>Subtotal</span>
							<span>{{ formatCurrency(subtotal, "BDT") }}</span>
						</div>
						<div class="flex justify-between text-sm text-red-500 font-medium">
							<span>Discount</span>
							<span>- {{ formatCurrency(totalDiscount, "BDT") }}</span>
						</div>
						<div class="flex justify-between items-center pt-3 border-t border-gray-50 mt-1">
							<span class="text-base font-bold text-gray-900">Total Payable</span>
							<span class="text-xl font-black text-indigo-600">{{ formatCurrency(total, "BDT") }}</span>
						</div>
					</div>

					<ion-button
						expand="block"
						class="checkout-btn font-bold h-14"
						mode="ios"
						@click="handleCheckout"
					>
						Proceed to Checkout
						<ArrowRight class="w-5 h-5 ml-2" />
					</ion-button>
				</div>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { ref, computed } from "vue"
import { useRouter } from "vue-router"
import { IonContent, IonButton } from "@ionic/vue"
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import { ShoppingCart, Trash2, Plus, Minus, ArrowRight } from "lucide-vue-next"
import { formatCurrency } from "@/utils/formatters"

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
ion-content {
	--background: transparent;
}

.checkout-btn {
	--background: #4f46e5;
	--background-activated: #4338ca;
	--border-radius: 16px;
	--box-shadow: 0 10px 15px -3px rgba(79, 70, 229, 0.2);
	margin: 0;
	font-weight: 700;
	letter-spacing: -0.01em;
}
</style>
