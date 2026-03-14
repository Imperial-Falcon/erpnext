<template>
	<ion-page>
		<ion-content class="ion-padding flex flex-col items-center justify-center">
			<div class="h-full flex flex-col items-center justify-center text-center px-6">
				<!-- Success Animation Icon -->
				<div class="relative mb-8">
					<div class="w-32 h-32 bg-emerald-50 rounded-full flex items-center justify-center animate-bounce">
						<CheckCircle2 class="w-16 h-16 text-emerald-500" />
					</div>
					<!-- Decorative particles -->
					<div class="absolute -top-2 -right-2 w-4 h-4 bg-yellow-400 rounded-full animate-ping"></div>
					<div class="absolute -bottom-2 -left-2 w-3 h-3 bg-indigo-400 rounded-full animate-pulse"></div>
				</div>

				<h1 class="text-3xl font-black text-gray-900 mb-2">Order Placed!</h1>
				<p class="text-gray-500 font-medium mb-8 leading-relaxed">
					Your order <span class="text-indigo-600 font-black">#ORD-99281</span> has been placed successfully. We'll notify you once it's shipped.
				</p>

				<!-- Summary Card -->
				<div class="w-full bg-white rounded-3xl p-6 border border-gray-100 shadow-xl shadow-gray-200/50 mb-10">
					<div class="flex justify-between items-center mb-4 pb-4 border-b border-gray-50">
						<div class="flex items-center gap-3">
							<div class="w-10 h-10 rounded-xl bg-gray-50 flex items-center justify-center">
								<Truck class="w-5 h-5 text-gray-600" />
							</div>
							<div class="text-left">
								<p class="text-[10px] font-black text-gray-400 uppercase tracking-widest">Delivery By</p>
								<p class="text-xs font-bold text-gray-900">18 March, 2026</p>
							</div>
						</div>
						<div class="text-right">
							<p class="text-[10px] font-black text-gray-400 uppercase tracking-widest">Total Amount</p>
							<p class="text-xs font-black text-indigo-600">{{ formatCurrency(5750, "BDT") }}</p>
						</div>
					</div>
					<p class="text-[10px] text-gray-400 font-medium italic">Payment Method: Cash on Delivery</p>
				</div>

				<!-- Actions -->
				<div class="w-full space-y-4">
					<ion-button expand="block" mode="ios" class="checkout-btn h-14 m-0" @click="$router.push('/orders')">
						<div class="flex items-center gap-2">
							<Package class="w-5 h-5" />
							<span class="font-black">Track My Order</span>
						</div>
					</ion-button>
					<button 
						@click="$router.push('/home')"
						class="w-full py-4 text-sm font-black text-gray-400 hover:text-indigo-600 transition-colors"
					>
						Back to Home
					</button>
				</div>
			</div>
		</ion-content>
	</ion-page>
</template>

<script setup>
import { IonPage, IonContent, IonButton } from "@ionic/vue"
import { CheckCircle2, Truck, Package } from "lucide-vue-next"
import { formatCurrency } from "@/utils/formatters"
</script>

<style scoped>
.checkout-btn {
	--background: #4f46e5;
	--border-radius: 20px;
}
</style>
