<template>
	<ion-page>
		<ion-header class="ion-no-border" mode="ios">
			<ion-toolbar class="px-2">
				<ion-buttons slot="start">
					<ion-back-button default-href="/orders" text="" class="text-gray-900"></ion-back-button>
				</ion-buttons>
				<ion-title class="text-lg font-black tracking-tight">Order Details</ion-title>
				<ion-buttons slot="end">
					<button class="p-2 mr-2 bg-gray-50 rounded-xl active:scale-90 transition-all">
						<FileText class="w-5 h-5 text-gray-700" />
					</button>
				</ion-buttons>
			</ion-toolbar>
		</ion-header>

		<ion-content class="ion-no-padding">
			<div class="flex flex-col bg-gray-50/30 pb-32">
				<!-- Order ID & Date Header -->
				<div class="bg-white px-6 py-6 border-b border-gray-50 flex justify-between items-center">
					<div class="flex flex-col gap-1">
						<h2 class="text-xl font-black text-gray-900">#ORD-99281</h2>
						<p class="text-[11px] font-black text-gray-400 uppercase tracking-widest">Placed on 14 Mar, 2026</p>
					</div>
					<div class="px-4 py-1.5 bg-indigo-50 rounded-full text-[11px] font-black text-indigo-600 uppercase">
						Active
					</div>
				</div>

				<!-- Delivery Status Timeline -->
				<section class="px-4 py-8 bg-white mb-4 shadow-sm">
					<h3 class="px-2 text-sm font-black text-gray-900 uppercase tracking-widest mb-6">Delivery Timeline</h3>
					<div class="relative pl-8 space-y-8">
						<!-- Vertical Line -->
						<div class="absolute left-[11px] top-2 bottom-2 w-0.5 bg-gray-100"></div>

						<div v-for="(step, index) in timeline" :key="index" class="relative flex flex-col gap-1">
							<!-- Node -->
							<div 
								class="absolute -left-8 w-6 h-6 rounded-full border-4 border-white shadow-sm flex items-center justify-center transition-all duration-500"
								:class="step.active ? 'bg-indigo-600 scale-110' : 'bg-gray-200'"
							>
								<Check v-if="step.completed" class="w-2.5 h-2.5 text-white" />
							</div>
							<div class="flex justify-between items-start">
								<h4 class="text-sm font-black" :class="step.active ? 'text-gray-900' : 'text-gray-400'">{{ step.title }}</h4>
								<span class="text-[10px] font-bold text-gray-400">{{ step.time }}</span>
							</div>
							<p class="text-xs font-medium text-gray-400">{{ step.desc }}</p>
						</div>
					</div>
				</section>

				<!-- Shipping Address -->
				<section class="px-4 mb-4">
					<div class="bg-white rounded-[24px] p-6 border border-gray-100 shadow-sm">
						<div class="flex items-center gap-3 mb-4">
							<MapPin class="w-5 h-5 text-indigo-600" />
							<h3 class="text-sm font-black text-gray-900 uppercase tracking-widest">Shipping Address</h3>
						</div>
						<p class="text-sm font-bold text-gray-900 mb-1">Office / Workplace</p>
						<p class="text-xs font-medium text-gray-500 leading-relaxed">
							Level 4, House 12, Road 7, Sector 3, Uttara Model Town, Dhaka 1230
						</p>
						<p class="text-[11px] font-black text-indigo-600 mt-2 tracking-widest uppercase">+880 1712 345678</p>
					</div>
				</section>

				<!-- Order Items -->
				<section class="px-4 mb-4">
					<div class="bg-white rounded-[24px] border border-gray-100 shadow-sm overflow-hidden">
						<div class="px-6 py-4 border-b border-gray-50 flex items-center gap-3">
							<Package class="w-5 h-5 text-indigo-600" />
							<h3 class="text-sm font-black text-gray-900 uppercase tracking-widest">Items Ordered</h3>
						</div>
						<div class="divide-y divide-gray-50">
							<div v-for="i in 2" :key="i" class="p-4 flex items-center gap-4">
								<div class="w-14 h-14 bg-gray-50 rounded-2xl flex-shrink-0 flex items-center justify-center p-2">
									<img src="https://via.placeholder.com/100" class="max-w-full max-h-full object-contain" />
								</div>
								<div class="flex-1">
									<h4 class="text-xs font-black text-gray-900 line-clamp-1">Product Title Sample #{{ i }}</h4>
									<p class="text-[10px] font-bold text-gray-400">Pack of 30 Tablets • Qty: 2</p>
								</div>
								<div class="text-right">
									<p class="text-xs font-black text-gray-900">{{ formatCurrency(1250 * 2, "BDT") }}</p>
									<p class="text-[10px] font-bold text-gray-400">1250 x 2</p>
								</div>
							</div>
						</div>
					</div>
				</section>

				<!-- Billing Summary -->
				<section class="px-4 mb-10">
					<div class="bg-indigo-600 rounded-[24px] p-6 text-white shadow-xl shadow-indigo-100">
						<div class="space-y-3 mb-6">
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
						<div class="pt-4 border-t border-white/10 flex justify-between items-center">
							<span class="text-lg font-black uppercase tracking-widest">Total Payable</span>
							<span class="text-2xl font-black">{{ formatCurrency(4750, "BDT") }}</span>
						</div>
						<p class="mt-4 text-center text-[10px] font-black text-white/50 uppercase tracking-[0.2em]">Cash on Delivery</p>
					</div>
				</section>
			</div>
		</ion-content>

		<!-- Bottom Fixed Action -->
		<div class="fixed bottom-0 left-0 right-0 p-6 bg-white/80 backdrop-blur-xl border-t border-gray-100 z-50 standalone:pb-10">
			<button 
				@click="$router.push(`/reorder/${$route.params.id || 'ORD-99281'}`)"
				class="w-full h-14 bg-gray-900 text-white font-black rounded-2xl flex items-center justify-center gap-3 active:scale-[0.98] transition-all"
			>
				<RotateCcw class="w-5 h-5" />
				<span>Reorder Items</span>
			</button>
		</div>
	</ion-page>
</template>

<script setup>
import { IonPage, IonHeader, IonToolbar, IonButtons, IonBackButton, IonTitle, IonContent } from "@ionic/vue"
import { FileText, MapPin, Package, Check, RotateCcw } from "lucide-vue-next"
import { formatCurrency } from "@/utils/formatters"

const timeline = [
	{ title: 'Order Placed', time: '14 Mar, 10:30 AM', desc: 'Your order has been received.', active: true, completed: true },
	{ title: 'Processing', time: '14 Mar, 11:45 AM', desc: 'Items are being packed.', active: true, completed: true },
	{ title: 'Shipped', time: 'Pending', desc: 'Awaiting courier pickup.', active: false, completed: false },
	{ title: 'Out for Delivery', time: 'Pending', desc: 'Courier is on the way.', active: false, completed: false },
]
</script>

<style scoped>
ion-toolbar {
	--background: transparent;
	--border-width: 0;
}
</style>
