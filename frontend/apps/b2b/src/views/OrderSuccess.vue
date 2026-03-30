<template>
	<BaseLayout :pageTitle="__('Order Success')" :showHeader="false">
		<template #body>
			<div class="flex flex-col h-full overflow-hidden relative" style="background: var(--app-bg);">
				<!-- Ambient Backdrops -->
				<div class="absolute inset-0 overflow-hidden pointer-events-none z-0">
					<div class="absolute top-[10%] left-[-50px] w-[320px] h-[320px] bg-emerald-500/15 blur-[100px] rounded-full"></div>
					<div class="absolute bottom-[20%] right-[-50px] w-[280px] h-[280px] bg-brand-primary/15 blur-[100px] rounded-full"></div>
				</div>

				<ion-content class="transparent-content">
					<div class="h-full flex flex-col items-center justify-center text-center px-6 relative z-10">
						<!-- Success Animation Icon -->
						<div class="relative mb-8 animate-fade-in-up">
							<div class="w-28 h-28 app-card rounded-full flex items-center justify-center shadow-[0_0_40px_rgba(16,185,129,0.3)] border border-emerald-200/50 dark:border-emerald-800/50">
								<CheckCircle2 class="w-14 h-14 text-emerald-500" />
							</div>
							<!-- Decorative particles -->
							<div class="absolute -top-3 -right-3 w-5 h-5 bg-yellow-400 rounded-full animate-ping opacity-60"></div>
							<div class="absolute -bottom-2 -left-3 w-4 h-4 bg-brand-primary rounded-full animate-pulse opacity-60"></div>
							<div class="absolute top-1/2 -right-6 w-3 h-3 bg-brand-secondary rounded-full animate-bounce opacity-40"></div>
						</div>

						<h1 class="text-3xl font-black text-gray-900 dark:text-gray-100 mb-2 animate-fade-in-up" style="animation-delay: 0.1s">Order Placed!</h1>
						<p class="text-gray-500 font-medium mb-8 leading-relaxed animate-fade-in-up" style="animation-delay: 0.15s">
							Your order <span class="font-black bg-clip-text text-transparent bg-gradient-to-r from-brand-primary to-brand-secondary">#ORD-99281</span> has been placed successfully. We'll notify you once it's shipped.
						</p>

						<!-- Summary Card -->
						<div class="w-full app-card rounded-[1.75rem] p-6 border border-white/40 shadow-glass mb-10 animate-fade-in-up" style="animation-delay: 0.2s">
							<div class="flex justify-between items-center mb-4 pb-4 border-b border-gray-100 dark:border-gray-800">
								<div class="flex items-center gap-3">
									<div class="w-10 h-10 rounded-xl bg-brand-primary/10 flex items-center justify-center">
										<Truck class="w-5 h-5 text-brand-primary" />
									</div>
									<div class="text-left">
										<p class="text-[10px] font-black text-gray-400 uppercase tracking-widest">Delivery By</p>
										<p class="text-xs font-bold text-gray-900 dark:text-gray-100">18 March, 2026</p>
									</div>
								</div>
								<div class="text-right">
									<p class="text-[10px] font-black text-gray-400 uppercase tracking-widest">Total Amount</p>
									<p class="text-xs font-black bg-clip-text text-transparent bg-gradient-to-r from-brand-primary to-brand-secondary">{{ formatCurrency(5750, "BDT") }}</p>
								</div>
							</div>
							<p class="text-[10px] text-gray-400 font-medium italic">Payment Method: Cash on Delivery</p>
						</div>

						<!-- Actions -->
						<div class="w-full space-y-4 animate-fade-in-up" style="animation-delay: 0.25s">
							<button
								@click="$router.push('/orders')"
								class="w-full flex items-center justify-center gap-2 h-14 bg-gradient-to-tr from-brand-primary to-brand-secondary text-white rounded-[1.2rem] shadow-neon active:scale-95 transition-all"
							>
								<Package class="w-5 h-5" />
								<span class="font-black tracking-wide">Track My Order</span>
							</button>
							<button
								@click="$router.push('/home')"
								class="w-full py-4 text-sm font-black text-gray-400 hover:text-brand-primary transition-colors uppercase tracking-widest"
							>
								Back to Home
							</button>
						</div>
					</div>
				</ion-content>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { inject } from "vue"
import { IonContent } from "@ionic/vue"
import { CheckCircle2, Truck, Package } from "lucide-vue-next"
import { formatCurrency } from "@/utils/formatters"
import BaseLayout from "@/components/layouts/BaseLayout.vue"

const __ = inject("$translate")
</script>

<style scoped>
.transparent-content {
	--background: transparent;
}
</style>
