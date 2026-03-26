<template>
	<BaseLayout :pageTitle="__('Checkout')" :showHeader="false">
		<template #body>
			<div class="flex flex-col h-full bg-gray-50 dark:bg-black overflow-hidden relative">
				<AppHeader :title="__('Checkout')" :showBack="true" :isScrolled="false" customClass="bg-white/70 dark:bg-black/70 backdrop-blur-xl shadow-glass z-50 animate-fade-in-up border-b border-white/20" />

				<!-- Ambient Backdrops -->
				<div class="absolute inset-0 overflow-hidden pointer-events-none z-0">
					<div class="absolute top-[30%] left-[-50px] w-[300px] h-[300px] bg-brand-primary/10 blur-[80px] rounded-full"></div>
					<div class="absolute bottom-[20%] right-[-50px] w-[250px] h-[250px] bg-brand-secondary/15 blur-[80px] rounded-full"></div>
				</div>

				<ion-content class="transparent-content pb-[160px]">
				<div class="pb-[180px]">
					<!-- Progress Tracker (Visual only) -->
					<div class="px-5 py-6 flex items-center justify-center gap-4 relative z-10 animate-fade-in-up">
						<div class="flex flex-col items-center gap-1.5">
							<div class="w-8 h-8 rounded-full bg-gradient-to-tr from-brand-primary to-brand-secondary text-white flex items-center justify-center shadow-neon">
								<Check class="w-4 h-4" />
							</div>
							<span class="text-[10px] font-black text-gray-900 dark:text-gray-100 uppercase tracking-tighter">Cart</span>
						</div>
						<div class="w-12 h-[2px] bg-brand-primary/50 mb-4 opacity-30 shadow-neon"></div>
						<div class="flex flex-col items-center gap-1.5">
							<div class="w-8 h-8 rounded-full bg-gradient-to-tr from-brand-primary to-brand-secondary text-white flex items-center justify-center shadow-neon">
								<MapPin class="w-4 h-4" />
							</div>
							<span class="text-[10px] font-black text-gray-900 dark:text-gray-100 uppercase tracking-tighter">Address</span>
						</div>
						<div class="w-12 h-[2px] bg-gray-200 dark:bg-gray-700 mb-4"></div>
						<div class="flex flex-col items-center gap-1.5">
							<div class="w-8 h-8 rounded-full app-card border border-gray-200 dark:border-gray-700 text-gray-300 dark:text-gray-600 flex items-center justify-center">
								<CreditCard class="w-4 h-4" />
							</div>
							<span class="text-[10px] font-black text-gray-400 uppercase tracking-tighter">Payment</span>
						</div>
					</div>

					<!-- Delivery Address -->
					<section class="px-5 mb-6 relative z-10 animate-fade-in-up" style="animation-delay: 50ms">
						<div class="flex justify-between items-center mb-3 px-1">
							<h3 class="text-xs font-black text-gray-900 dark:text-gray-100 uppercase tracking-widest">Delivery Address</h3>
							<button class="text-[10px] font-black tracking-widest text-brand-primary bg-brand-primary/10 px-3 py-1 rounded-full uppercase">Change</button>
						</div>
						<div class="app-card rounded-[1.5rem] p-5 border border-white/40 shadow-glass flex items-start gap-4 active:scale-[0.99] transition-all">
							<div class="w-12 h-12 rounded-2xl bg-brand-primary/10 flex items-center justify-center flex-shrink-0">
								<HomeIcon class="w-6 h-6 text-brand-primary" />
							</div>
							<div class="flex-1">
								<h4 class="text-sm font-black text-gray-900 dark:text-gray-100 mb-1">Office / Workplace</h4>
								<p class="text-xs font-medium text-gray-500 dark:text-gray-400 leading-relaxed">
									Level 4, House 12, Road 7, Sector 3, Uttara Model Town, Dhaka 1230
								</p>
								<p class="text-[10px] font-black text-brand-primary mt-2 tracking-widest uppercase">+880 1712 345678</p>
							</div>
						</div>
					</section>

					<!-- Payment Method (COD ONLY) -->
					<section class="px-5 mb-6 relative z-10 animate-fade-in-up" style="animation-delay: 100ms">
						<h3 class="text-xs font-black text-gray-900 dark:text-gray-100 uppercase tracking-widest mb-3 px-1">Payment Method</h3>
						<div class="app-card rounded-[1.5rem] p-5 border border-brand-primary shadow-[0_0_15px_rgba(var(--brand-primary-rgb),0.1)] flex items-center justify-between relative overflow-hidden">
							<!-- Selection Indicator -->
							<div class="absolute -right-6 -top-6 w-16 h-16 bg-gradient-to-tr from-brand-primary to-brand-secondary rounded-full flex items-end justify-start p-4 shadow-neon">
								<Check class="w-4 h-4 text-white" />
							</div>

							<div class="flex items-center gap-4">
								<div class="w-12 h-12 rounded-2xl bg-orange-500/10 flex items-center justify-center flex-shrink-0">
									<Banknote class="w-6 h-6 text-orange-500" />
								</div>
								<div>
									<h4 class="text-sm font-black text-gray-900 dark:text-gray-100">Cash on Delivery</h4>
									<p class="text-[10px] font-bold text-gray-400 uppercase tracking-widest mt-0.5">Pay when you receive</p>
								</div>
							</div>
						</div>
						<p class="mt-3 px-1 text-[10px] text-gray-400 font-medium italic">
							* Note: Online payment is currently unavailable for your region.
						</p>
					</section>

					<!-- Order Items -->
					<section class="px-5 mb-6 relative z-10 animate-fade-in-up" style="animation-delay: 150ms">
						<h3 class="text-xs font-black text-gray-900 dark:text-gray-100 uppercase tracking-widest mb-3 px-1">Order Summary</h3>
						<div class="app-card rounded-[1.5rem] border border-white/40 shadow-glass divide-y divide-gray-100 dark:divide-gray-800">
							<div v-for="item in cartItems" :key="item.id" class="p-4 flex items-center gap-3">
								<div class="w-12 h-12 bg-white/50 dark:bg-gray-800/50 rounded-xl flex-shrink-0 flex items-center justify-center p-1.5 shadow-sm border border-white/50 dark:border-gray-700">
									<img :src="item.image" class="max-w-full max-h-full object-contain mix-blend-multiply dark:mix-blend-normal" />
								</div>
								<div class="flex-1">
									<h5 class="text-xs font-black text-gray-900 dark:text-gray-100 line-clamp-1 leading-tight">{{ item.name }}</h5>
									<p class="text-[10px] font-bold text-gray-400 mt-0.5">Qty: {{ item.qty }}</p>
								</div>
								<span class="text-xs font-black text-brand-primary">{{ formatCurrency(item.price * item.qty, "BDT") }}</span>
							</div>
						</div>
					</section>

					<!-- Billing Details -->
					<section class="px-5 mb-10 relative z-10 animate-fade-in-up" style="animation-delay: 200ms">
						<div class="app-card rounded-[1.5rem] p-5 border border-white/40 shadow-glass space-y-3">
							<div class="flex justify-between items-center text-xs">
								<span class="font-bold text-gray-500 uppercase tracking-widest text-[10px]">Subtotal</span>
								<span class="font-black text-gray-900 dark:text-gray-100">{{ formatCurrency(subtotal, "BDT") }}</span>
							</div>
							<div class="flex justify-between items-center text-xs">
								<span class="font-bold text-gray-500 uppercase tracking-widest text-[10px]">Shipping</span>
								<span class="font-black text-brand-primary uppercase tracking-tighter">FREE</span>
							</div>
							<div class="flex justify-between items-center text-xs">
								<span class="font-bold text-gray-500 uppercase tracking-widest text-[10px]">Discount Applied</span>
								<span class="font-black text-brand-accent">- {{ formatCurrency(totalDiscount, "BDT") }}</span>
							</div>
							<div class="pt-3 border-t border-gray-100 dark:border-gray-800 flex justify-between items-center text-xs">
								<span class="font-black text-gray-900 dark:text-gray-100 uppercase tracking-widest text-[10px]">Total Payable</span>
								<span class="text-lg font-black bg-clip-text text-transparent bg-gradient-to-r from-brand-primary to-brand-secondary">{{ formatCurrency(total, "BDT") }}</span>
							</div>
						</div>
					</section>
				</div>
			</ion-content>

			<!-- Bottom Fixed Button -->
			<div class="fixed bottom-0 left-0 right-0 app-card rounded-t-[2rem] border-t border-white/40 p-5 pb-8 shadow-[0_-15px_40px_rgba(0,0,0,0.05)] z-50 backdrop-blur-3xl standalone:pb-12 animate-slide-up">
				<button
					class="w-full flex items-center justify-center gap-2 h-14 bg-gradient-to-tr from-brand-primary to-brand-secondary text-white rounded-[1.2rem] shadow-neon active:scale-95 transition-all outline-none"
					@click="handlePlaceOrder"
				>
					<Truck class="w-5 h-5 -ml-2" />
					<span class="font-black text-sm tracking-wide">Place Order (COD)</span>
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
import { 
	Check, MapPin, CreditCard, Home as HomeIcon, 
	Banknote, Truck 
} from "lucide-vue-next"
import { formatCurrency } from "@/utils/formatters"

const __ = inject("$translate")
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
