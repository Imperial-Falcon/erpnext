<template>
	<BaseLayout :pageTitle="__('Order History')" :showHeader="false">
		<template #body>
			<div class="flex flex-col h-full overflow-hidden relative" style="background: var(--app-bg);">
				<AppHeader :title="__('Order History')" :showBack="true" :isScrolled="true" />

				<!-- Ambient Backdrops -->
				<div class="absolute inset-0 overflow-hidden pointer-events-none z-0">
					<div class="absolute top-[30%] left-[-50px] w-[300px] h-[300px] bg-brand-primary/10 blur-[80px] rounded-full"></div>
					<div class="absolute bottom-[20%] right-[-50px] w-[250px] h-[250px] bg-brand-secondary/15 blur-[80px] rounded-full"></div>
				</div>

				<!-- Filters Bar -->
				<div class="px-5 pt-2 pb-4 relative z-10 space-y-3 animate-fade-in-up">
					<div class="flex gap-2 overflow-x-auto no-scrollbar">
						<button
							v-for="status in ['All', 'Active', 'Delivered', 'Cancelled']"
							:key="status"
							@click="selectedStatus = status"
							class="whitespace-nowrap px-5 py-2 rounded-full text-[10px] font-black tracking-widest uppercase transition-all active:scale-95"
							:class="selectedStatus === status
								? 'bg-gradient-to-r from-brand-primary to-brand-secondary text-white shadow-neon'
								: 'app-card border border-white/40 text-gray-500 dark:text-gray-400'"
						>
							{{ status }}
						</button>
					</div>

					<!-- Date Range Filter -->
					<div class="flex items-center gap-3 app-card border border-white/40 p-2.5 rounded-[1.2rem]">
						<Calendar class="w-4 h-4 text-gray-400 ml-2" />
						<div class="flex items-center gap-2 flex-1">
							<input type="date" class="bg-transparent border-none text-[11px] font-black text-gray-600 dark:text-gray-400 focus:ring-0 p-0 w-full" />
							<span class="text-gray-300 text-xs">—</span>
							<input type="date" class="bg-transparent border-none text-[11px] font-black text-gray-600 dark:text-gray-400 focus:ring-0 p-0 w-full" />
						</div>
						<button class="p-1.5 app-card rounded-lg shadow-sm">
							<Filter class="w-3.5 h-3.5 text-brand-primary" />
						</button>
					</div>
				</div>

				<ion-content class="transparent-content">
					<div class="relative z-10 pb-20">
						<!-- Order List -->
						<div v-if="filteredOrders.length > 0" class="px-5 space-y-4">
							<div
								v-for="(order, index) in filteredOrders"
								:key="order.id"
								@click="$router.push(`/order-detail/${order.id}`)"
								class="app-card rounded-[1.5rem] p-5 shadow-glass border border-white/40 flex flex-col gap-4 active:scale-[0.99] transition-all cursor-pointer animate-fade-in-up"
								:style="`animation-delay: ${index * 50}ms`"
							>
								<div class="flex justify-between items-start">
									<div class="flex flex-col gap-1">
										<span class="text-[10px] font-black text-gray-400 tracking-[0.2em] uppercase">Order #{{ order.id }}</span>
										<h3 class="text-sm font-black text-gray-900 dark:text-gray-100">{{ order.date }}</h3>
									</div>
									<div
										class="px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-tighter"
										:class="statusStyles[order.status]"
									>
										{{ order.status }}
									</div>
								</div>

								<div class="flex items-center gap-3">
									<div class="flex -space-x-3 overflow-hidden">
										<div v-for="i in 3" :key="i" class="w-10 h-10 rounded-xl bg-white/50 dark:bg-gray-800/50 border-2 border-white dark:border-gray-900 flex items-center justify-center p-1.5 shadow-sm">
											<img src="https://via.placeholder.com/100" class="max-w-full max-h-full object-contain" />
										</div>
										<div v-if="order.itemCount > 3" class="w-10 h-10 rounded-xl bg-brand-primary/10 border-2 border-white dark:border-gray-900 flex items-center justify-center shadow-sm">
											<span class="text-[10px] font-black text-brand-primary">+{{ order.itemCount - 3 }}</span>
										</div>
									</div>
									<div class="flex-1 px-1">
										<p class="text-[11px] font-bold text-gray-500">{{ order.itemCount }} Items • COD</p>
										<p class="text-[11px] font-bold text-gray-400">Dhaka Office</p>
									</div>
									<div class="text-right flex flex-col">
										<span class="text-sm font-black bg-clip-text text-transparent bg-gradient-to-r from-brand-primary to-brand-secondary">{{ formatCurrency(order.total, "BDT") }}</span>
										<ChevronRight class="w-4 h-4 text-gray-300 dark:text-gray-600 ml-auto mt-1" />
									</div>
								</div>
							</div>
						</div>

						<!-- Empty State -->
						<div v-else class="flex flex-col items-center justify-center pt-24 px-10 text-center animate-fade-in-up">
							<div class="w-24 h-24 app-card rounded-full flex items-center justify-center mb-6 shadow-glass relative">
								<div class="absolute inset-0 bg-brand-primary/10 rounded-full animate-ping opacity-30"></div>
								<PackageSearch class="w-10 h-10 text-gray-300 dark:text-gray-600" />
							</div>
							<h3 class="text-lg font-black text-gray-900 dark:text-gray-100 mb-1">No orders found</h3>
							<p class="text-xs text-gray-400 font-medium">Try adjusting your filters or date range.</p>
						</div>
					</div>
				</ion-content>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { ref, computed, inject } from "vue"
import { IonContent } from "@ionic/vue"
import { Calendar, Filter, ChevronRight, PackageSearch } from "lucide-vue-next"
import { formatCurrency } from "@/utils/formatters"
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import AppHeader from "@/components/AppHeader.vue"

const __ = inject("$translate")
const selectedStatus = ref("All")

const statusStyles = {
	'Active': 'bg-brand-primary/10 text-brand-primary',
	'Delivered': 'bg-emerald-500/10 text-emerald-600',
	'Cancelled': 'bg-brand-accent/10 text-brand-accent',
	'Processing': 'bg-amber-500/10 text-amber-600'
}

const orders = ref([
	{ id: 'ORD-99281', date: '14 Mar, 2026', status: 'Active', total: 5750, itemCount: 5 },
	{ id: 'ORD-98122', date: '10 Mar, 2026', status: 'Delivered', total: 12500, itemCount: 12 },
	{ id: 'ORD-97554', date: '05 Mar, 2026', status: 'Delivered', total: 4200, itemCount: 4 },
	{ id: 'ORD-96331', date: '01 Mar, 2026', status: 'Cancelled', total: 850, itemCount: 1 },
])

const filteredOrders = computed(() => {
	if (selectedStatus.value === "All") return orders.value
	return orders.value.filter(o => o.status === selectedStatus.value)
})
</script>

<style scoped>
.transparent-content {
	--background: transparent;
}
</style>
