<template>
	<BaseLayout :pageTitle="__('Order Details')" :showHeader="false">
		<template #body>
			<div class="flex flex-col h-full bg-gray-50 dark:bg-black overflow-hidden relative">
				<AppHeader :title="__('Order Details')" :showBack="true" :isScrolled="true">
					<template #actions>
						<button class="p-2.5 app-card active:scale-90 transition-all hover:shadow-neon">
							<FileText class="w-5 h-5 text-gray-700 dark:text-gray-300" />
						</button>
					</template>
				</AppHeader>

				<!-- Ambient Backdrops -->
				<div class="absolute inset-0 overflow-hidden pointer-events-none z-0">
					<div class="absolute top-[20%] left-[-50px] w-[300px] h-[300px] bg-brand-primary/10 blur-[80px] rounded-full"></div>
					<div class="absolute bottom-[30%] right-[-50px] w-[250px] h-[250px] bg-brand-secondary/15 blur-[80px] rounded-full"></div>
				</div>

				<ion-content class="transparent-content">
					<div class="relative z-10 pb-32">
						<!-- Order ID & Date Header -->
						<div class="px-5 py-5 flex justify-between items-center animate-fade-in-up">
							<div class="flex flex-col gap-1">
								<h2 class="text-xl font-black text-gray-900 dark:text-gray-100">#ORD-99281</h2>
								<p class="text-[11px] font-black text-gray-400 uppercase tracking-widest">Placed on 14 Mar, 2026</p>
							</div>
							<div class="px-4 py-1.5 bg-brand-primary/10 rounded-full text-[11px] font-black text-brand-primary uppercase">
								Active
							</div>
						</div>

						<!-- Delivery Status Timeline -->
						<section class="px-5 py-6 mb-4 animate-fade-in-up" style="animation-delay: 50ms">
							<h3 class="px-1 text-xs font-black text-gray-900 dark:text-gray-100 uppercase tracking-widest mb-6">Delivery Timeline</h3>
							<div class="relative pl-8 space-y-8">
								<!-- Vertical Line -->
								<div class="absolute left-[11px] top-2 bottom-2 w-0.5 bg-gray-100 dark:bg-gray-800"></div>

								<div v-for="(step, index) in timeline" :key="index" class="relative flex flex-col gap-1">
									<div
										class="absolute -left-8 w-6 h-6 rounded-full border-4 border-white dark:border-gray-900 shadow-sm flex items-center justify-center transition-all duration-500"
										:class="step.active ? 'bg-gradient-to-tr from-brand-primary to-brand-secondary shadow-neon scale-110' : 'bg-gray-200 dark:bg-gray-700'"
									>
										<Check v-if="step.completed" class="w-2.5 h-2.5 text-white" />
									</div>
									<div class="flex justify-between items-start">
										<h4 class="text-sm font-black" :class="step.active ? 'text-gray-900 dark:text-gray-100' : 'text-gray-400'">{{ step.title }}</h4>
										<span class="text-[10px] font-bold text-gray-400">{{ step.time }}</span>
									</div>
									<p class="text-xs font-medium text-gray-400">{{ step.desc }}</p>
								</div>
							</div>
						</section>

						<!-- Shipping Address -->
						<section class="px-5 mb-4 animate-fade-in-up" style="animation-delay: 100ms">
							<div class="app-card rounded-[1.5rem] p-6 border border-white/40 shadow-glass">
								<div class="flex items-center gap-3 mb-4">
									<MapPin class="w-5 h-5 text-brand-primary" />
									<h3 class="text-xs font-black text-gray-900 dark:text-gray-100 uppercase tracking-widest">Shipping Address</h3>
								</div>
								<p class="text-sm font-bold text-gray-900 dark:text-gray-100 mb-1">Office / Workplace</p>
								<p class="text-xs font-medium text-gray-500 dark:text-gray-400 leading-relaxed">
									Level 4, House 12, Road 7, Sector 3, Uttara Model Town, Dhaka 1230
								</p>
								<p class="text-[11px] font-black text-brand-primary mt-2 tracking-widest uppercase">+880 1712 345678</p>
							</div>
						</section>

						<!-- Order Items -->
						<section class="px-5 mb-4 animate-fade-in-up" style="animation-delay: 150ms">
							<div class="app-card rounded-[1.5rem] border border-white/40 shadow-glass overflow-hidden">
								<div class="px-6 py-4 border-b border-gray-100 dark:border-gray-800 flex items-center gap-3">
									<Package class="w-5 h-5 text-brand-primary" />
									<h3 class="text-xs font-black text-gray-900 dark:text-gray-100 uppercase tracking-widest">Items Ordered</h3>
								</div>
								<div class="divide-y divide-gray-100 dark:divide-gray-800">
									<div v-for="i in 2" :key="i" class="p-4 flex items-center gap-4">
										<div class="w-14 h-14 bg-white/50 dark:bg-gray-800/50 rounded-2xl flex-shrink-0 flex items-center justify-center p-2 border border-white/50 dark:border-gray-700 shadow-sm">
											<img src="https://via.placeholder.com/100" class="max-w-full max-h-full object-contain mix-blend-multiply dark:mix-blend-normal" />
										</div>
										<div class="flex-1">
											<h4 class="text-xs font-black text-gray-900 dark:text-gray-100 line-clamp-1">Product Title Sample #{{ i }}</h4>
											<p class="text-[10px] font-bold text-gray-400 mt-0.5">Pack of 30 Tablets • Qty: 2</p>
										</div>
										<div class="text-right">
											<p class="text-xs font-black text-brand-primary">{{ formatCurrency(1250 * 2, "BDT") }}</p>
											<p class="text-[10px] font-bold text-gray-400">1250 x 2</p>
										</div>
									</div>
								</div>
							</div>
						</section>

						<!-- Billing Summary -->
						<section class="px-5 mb-10 animate-fade-in-up" style="animation-delay: 200ms">
							<div class="rounded-[1.5rem] p-6 text-white shadow-neon relative overflow-hidden bg-gradient-to-br from-brand-primary via-violet-600 to-brand-secondary">
								<div class="absolute inset-0 bg-[radial-gradient(circle_at_80%_20%,rgba(255,255,255,0.1)_0%,transparent_50%)]"></div>
								<div class="relative z-10 space-y-3 mb-6">
									<div class="flex justify-between items-center text-xs opacity-80">
										<span class="font-bold">Subtotal</span>
										<span class="font-black">{{ formatCurrency(5000, "BDT") }}</span>
									</div>
									<div class="flex justify-between items-center text-xs opacity-80">
										<span class="font-bold">Shipping Fee</span>
										<span class="font-black">FREE</span>
									</div>
									<div class="flex justify-between items-center text-xs">
										<span class="font-bold text-white/90">Discount Applied</span>
										<span class="font-black text-emerald-300">- {{ formatCurrency(250, "BDT") }}</span>
									</div>
								</div>
								<div class="relative z-10 pt-4 border-t border-white/20 flex justify-between items-center">
									<span class="text-sm font-black uppercase tracking-widest">Total Payable</span>
									<span class="text-2xl font-black">{{ formatCurrency(4750, "BDT") }}</span>
								</div>
								<p class="relative z-10 mt-4 text-center text-[10px] font-black text-white/50 uppercase tracking-[0.2em]">Cash on Delivery</p>
							</div>
						</section>
					</div>
				</ion-content>

				<!-- Bottom Fixed Action -->
				<div class="fixed bottom-0 left-0 right-0 app-card rounded-t-[2rem] border-t border-white/40 p-5 pb-8 shadow-[0_-15px_40px_rgba(0,0,0,0.05)] z-50 backdrop-blur-3xl standalone:pb-12">
					<button
						@click="$router.push(`/reorder/${$route.params.id || 'ORD-99281'}`)"
						class="w-full h-14 bg-gradient-to-tr from-brand-primary to-brand-secondary text-white font-black rounded-[1.2rem] flex items-center justify-center gap-3 active:scale-[0.98] transition-all shadow-neon"
					>
						<RotateCcw class="w-5 h-5" />
						<span class="tracking-wide">Reorder Items</span>
					</button>
				</div>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { inject } from "vue"
import { useRoute } from "vue-router"
import { IonContent } from "@ionic/vue"
import { FileText, MapPin, Package, Check, RotateCcw } from "lucide-vue-next"
import { formatCurrency } from "@/utils/formatters"
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import AppHeader from "@/components/AppHeader.vue"

const __ = inject("$translate")
const route = useRoute()

const timeline = [
	{ title: 'Order Placed', time: '14 Mar, 10:30 AM', desc: 'Your order has been received.', active: true, completed: true },
	{ title: 'Processing', time: '14 Mar, 11:45 AM', desc: 'Items are being packed.', active: true, completed: true },
	{ title: 'Shipped', time: 'Pending', desc: 'Awaiting courier pickup.', active: false, completed: false },
	{ title: 'Out for Delivery', time: 'Pending', desc: 'Courier is on the way.', active: false, completed: false },
]
</script>

<style scoped>
.transparent-content {
	--background: transparent;
}
</style>
