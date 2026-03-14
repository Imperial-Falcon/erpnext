<template>
	<ion-page>
		<!-- Header -->
		<ion-header class="ion-no-border" mode="ios">
			<ion-toolbar class="px-2">
				<ion-buttons slot="start">
					<ion-back-button default-href="/cart" text="" class="text-gray-900"></ion-back-button>
				</ion-buttons>
				<ion-title class="text-lg font-black tracking-tight">Checkout</ion-title>
			</ion-toolbar>
		</ion-header>

		<ion-content class="ion-no-padding">
			<div class="flex flex-col bg-gray-50/30 pb-40">
				<!-- Progress Tracker (Visual only) -->
				<div class="px-6 py-6 flex items-center justify-center gap-4">
					<div class="flex flex-col items-center gap-1.5">
						<div class="w-8 h-8 rounded-full bg-indigo-600 text-white flex items-center justify-center shadow-lg shadow-indigo-100">
							<Check class="w-4 h-4" />
						</div>
						<span class="text-[10px] font-black text-gray-900 uppercase tracking-tighter">Cart</span>
					</div>
					<div class="w-12 h-[2px] bg-indigo-600 mb-4 opacity-20"></div>
					<div class="flex flex-col items-center gap-1.5">
						<div class="w-8 h-8 rounded-full bg-indigo-600 text-white flex items-center justify-center shadow-lg shadow-indigo-200">
							<MapPin class="w-4 h-4" />
						</div>
						<span class="text-[10px] font-black text-gray-900 uppercase tracking-tighter">Address</span>
					</div>
					<div class="w-12 h-[2px] bg-gray-200 mb-4"></div>
					<div class="flex flex-col items-center gap-1.5">
						<div class="w-8 h-8 rounded-full bg-white border-2 border-gray-200 text-gray-300 flex items-center justify-center">
							<CreditCard class="w-4 h-4" />
						</div>
						<span class="text-[10px] font-black text-gray-400 uppercase tracking-tighter">Payment</span>
					</div>
				</div>

				<!-- Delivery Address -->
				<section class="px-4 mb-6">
					<div class="flex justify-between items-center mb-3 px-1">
						<h3 class="text-sm font-black text-gray-900 uppercase tracking-widest">Delivery Address</h3>
						<button class="text-xs font-black text-indigo-600 bg-indigo-50 px-3 py-1 rounded-full">Change</button>
					</div>
					<div class="bg-white rounded-2xl p-5 border border-gray-100 shadow-sm flex items-start gap-4 active:scale-[0.99] transition-all">
						<div class="w-12 h-12 rounded-2xl bg-indigo-50 flex items-center justify-center flex-shrink-0">
							<HomeIcon class="w-6 h-6 text-indigo-600" />
						</div>
						<div class="flex-1">
							<h4 class="text-sm font-black text-gray-900 mb-1">Office / Workplace</h4>
							<p class="text-xs font-medium text-gray-500 leading-relaxed">
								Level 4, House 12, Road 7, Sector 3, Uttara Model Town, Dhaka 1230
							</p>
							<p class="text-[10px] font-black text-indigo-600 mt-2 tracking-widest uppercase">+880 1712 345678</p>
						</div>
					</div>
				</section>

				<!-- Payment Method (COD ONLY) -->
				<section class="px-4 mb-6">
					<h3 class="text-sm font-black text-gray-900 uppercase tracking-widest mb-3 px-1">Payment Method</h3>
					<div class="bg-white rounded-2xl p-5 border-2 border-indigo-600 shadow-xl shadow-indigo-100/30 flex items-center justify-between relative overflow-hidden">
						<!-- Selection Indicator -->
						<div class="absolute -right-6 -top-6 w-16 h-16 bg-indigo-600 rounded-full flex items-end justify-start p-4">
							<Check class="w-4 h-4 text-white" />
						</div>

						<div class="flex items-center gap-4">
							<div class="w-12 h-12 rounded-2xl bg-orange-50 flex items-center justify-center flex-shrink-0">
								<Banknote class="w-6 h-6 text-orange-600" />
							</div>
							<div>
								<h4 class="text-sm font-black text-gray-900">Cash on Delivery</h4>
								<p class="text-[10px] font-bold text-gray-400">Pay when you receive items</p>
							</div>
						</div>
					</div>
					<p class="mt-3 px-1 text-[10px] text-gray-400 font-medium italic">
						* Note: Online payment is currently unavailable for your region.
					</p>
				</section>

				<!-- Order Items -->
				<section class="px-4 mb-6">
					<h3 class="text-sm font-black text-gray-900 uppercase tracking-widest mb-3 px-1">Order Summary</h3>
					<div class="bg-white rounded-2xl border border-gray-100 shadow-sm divide-y divide-gray-50">
						<div v-for="item in cartItems" :key="item.id" class="p-4 flex items-center gap-3">
							<div class="w-12 h-12 bg-gray-50 rounded-xl flex-shrink-0 flex items-center justify-center p-1.5">
								<img :src="item.image" class="max-w-full max-h-full object-contain" />
							</div>
							<div class="flex-1">
								<h5 class="text-xs font-black text-gray-900 line-clamp-1 leading-tight">{{ item.name }}</h5>
								<p class="text-[10px] font-bold text-gray-400">Qty: {{ item.qty }}</p>
							</div>
							<span class="text-xs font-black text-gray-900">{{ formatCurrency(item.price * item.qty, "BDT") }}</span>
						</div>
					</div>
				</section>

				<!-- Billing Details -->
				<section class="px-4 mb-10">
					<div class="bg-white rounded-2xl p-5 border border-gray-100 shadow-sm space-y-3">
						<div class="flex justify-between items-center text-xs">
							<span class="font-bold text-gray-500">Subtotal</span>
							<span class="font-black text-gray-900">{{ formatCurrency(subtotal, "BDT") }}</span>
						</div>
						<div class="flex justify-between items-center text-xs">
							<span class="font-bold text-gray-500">Shipping</span>
							<span class="font-black text-emerald-600 uppercase tracking-tighter">FREE</span>
						</div>
						<div class="flex justify-between items-center text-xs">
							<span class="font-bold text-gray-500">Discount Applied</span>
							<span class="font-black text-red-500">- {{ formatCurrency(totalDiscount, "BDT") }}</span>
						</div>
						<div class="pt-3 border-t border-gray-50 flex justify-between items-center">
							<span class="text-sm font-black text-gray-900">Total Payable</span>
							<span class="text-xl font-black text-indigo-600">{{ formatCurrency(total, "BDT") }}</span>
						</div>
					</div>
				</section>
			</div>
		</ion-content>

		<!-- Bottom Fixed Button -->
		<div class="fixed bottom-0 left-0 right-0 p-6 bg-white/80 backdrop-blur-xl border-t border-gray-100 z-50 standalone:pb-10">
			<ion-button expand="block" mode="ios" class="checkout-btn h-14 m-0" @click="handlePlaceOrder">
				<div class="flex items-center gap-3">
					<Truck class="w-5 h-5" />
					<span class="font-black text-sm uppercase tracking-wide">Place Order (COD)</span>
				</div>
			</ion-button>
		</div>
	</ion-page>
</template>

<script setup>
import { ref, computed } from "vue"
import { useRouter } from "vue-router"
import { 
	IonPage, IonHeader, IonToolbar, IonButtons, IonBackButton, 
	IonTitle, IonContent, IonButton 
} from "@ionic/vue"
import { 
	Check, MapPin, CreditCard, Home as HomeIcon, 
	Banknote, Truck, ArrowRight 
} from "lucide-vue-next"
import { formatCurrency } from "@/utils/formatters"

const router = useRouter()

// Mock cart data (should come from store in real app)
const cartItems = ref([
	{ id: 1, name: "Premium Multivitamin Capsules", price: 1250, qty: 1, image: "https://via.placeholder.com/100?text=Vitamin" },
	{ id: 2, name: "Whey Protein Isolate", price: 4500, qty: 2, image: "https://via.placeholder.com/100?text=Protein" },
])

const subtotal = computed(() => cartItems.value.reduce((acc, item) => acc + (item.price * 1.2) * item.qty, 0))
const totalDiscount = computed(() => subtotal.value * 0.1)
const total = computed(() => subtotal.value - totalDiscount.value)

const handlePlaceOrder = () => {
	router.push("/order-success")
}
</script>

<style scoped>
.checkout-btn {
	--background: #4f46e5;
	--background-activated: #4338ca;
	--border-radius: 20px;
	--box-shadow: 0 12px 24px -6px rgba(79, 70, 229, 0.4);
}

ion-toolbar {
	--background: transparent;
	--border-width: 0;
}
</style>
