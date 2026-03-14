<template>
	<ion-page>
		<ion-header class="ion-no-border" mode="ios">
			<ion-toolbar class="px-2">
				<ion-buttons slot="start">
					<ion-back-button default-href="/profile" text="" class="text-gray-900"></ion-back-button>
				</ion-buttons>
				<ion-title class="text-lg font-black tracking-tight">Order History</ion-title>
				<ion-buttons slot="end">
					<button class="p-2 mr-2 bg-gray-50 rounded-xl active:scale-90 transition-all relative">
						<Search class="w-5 h-5 text-gray-700" />
					</button>
				</ion-buttons>
			</ion-toolbar>

			<!-- Quick Filters & Date -->
			<div class="px-4 pb-4 pt-2 bg-white flex flex-col gap-4">
				<div class="flex gap-2 overflow-x-auto no-scrollbar">
					<button 
						v-for="status in ['All', 'Active', 'Delivered', 'Cancelled']" 
						:key="status"
						@click="selectedStatus = status"
						class="whitespace-nowrap px-5 py-2 rounded-full text-[11px] font-black tracking-widest uppercase transition-all"
						:class="selectedStatus === status ? 'bg-indigo-600 text-white shadow-lg shadow-indigo-100' : 'bg-gray-100 text-gray-500'"
					>
						{{ status }}
					</button>
				</div>
				
				<!-- Date Range Filter -->
				<div class="flex items-center gap-3 bg-gray-50 p-2.5 rounded-2xl border border-gray-100">
					<Calendar class="w-4 h-4 text-gray-400 ml-2" />
					<div class="flex items-center gap-2 flex-1">
						<input type="date" class="bg-transparent border-none text-[11px] font-black text-gray-600 focus:ring-0 p-0" />
						<span class="text-gray-300 text-xs">—</span>
						<input type="date" class="bg-transparent border-none text-[11px] font-black text-gray-600 focus:ring-0 p-0" />
					</div>
					<button class="p-1.5 bg-white rounded-lg shadow-sm border border-gray-50">
						<Filter class="w-3.5 h-3.5 text-indigo-600" />
					</button>
				</div>
			</div>
		</ion-header>

		<ion-content class="ion-no-padding">
			<div class="flex flex-col bg-gray-50/30 pb-20">
				<!-- Order List -->
				<div v-if="filteredOrders.length > 0" class="px-4 pt-4 space-y-4">
					<div 
						v-for="order in filteredOrders" 
						:key="order.id"
						@click="$router.push(`/order-detail/${order.id}`)"
						class="bg-white rounded-[24px] p-5 shadow-sm border border-gray-100 flex flex-col gap-4 active:scale-[0.99] transition-all cursor-pointer"
					>
						<div class="flex justify-between items-start">
							<div class="flex flex-col gap-1">
								<span class="text-[10px] font-black text-gray-400 tracking-[0.2em] uppercase">Order #{{ order.id }}</span>
								<h3 class="text-sm font-black text-gray-900">{{ order.date }}</h3>
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
								<div v-for="i in 3" :key="i" class="w-10 h-10 rounded-xl bg-gray-100 border-2 border-white flex items-center justify-center p-1.5 shadow-sm">
									<img src="https://via.placeholder.com/100" class="max-w-full max-h-full object-contain" />
								</div>
								<div v-if="order.itemCount > 3" class="w-10 h-10 rounded-xl bg-indigo-50 border-2 border-white flex items-center justify-center shadow-sm">
									<span class="text-[10px] font-black text-indigo-600">+{{ order.itemCount - 3 }}</span>
								</div>
							</div>
							<div class="flex-1 px-1">
								<p class="text-[11px] font-bold text-gray-500">{{ order.itemCount }} Items • Cash on Delivery</p>
								<p class="text-[11px] font-bold text-gray-400">Arrived at: Dhaka Office</p>
							</div>
							<div class="text-right flex flex-col">
								<span class="text-sm font-black text-indigo-600">{{ formatCurrency(order.total, "BDT") }}</span>
								<ChevronRight class="w-4 h-4 text-gray-300 ml-auto mt-1" />
							</div>
						</div>
					</div>
				</div>

				<!-- Empty State -->
				<div v-else class="flex flex-col items-center justify-center pt-24 px-10 text-center">
					<div class="w-20 h-20 bg-white rounded-[32px] flex items-center justify-center mb-6 shadow-xl shadow-gray-200/50">
						<PackageSearch class="w-8 h-8 text-gray-200" />
					</div>
					<h3 class="text-lg font-black text-gray-900 mb-1">No orders found</h3>
					<p class="text-xs text-gray-400 font-medium">Try adjusting your filters or date range.</p>
				</div>
			</div>
		</ion-content>
	</ion-page>
</template>

<script setup>
import { ref, computed } from "vue"
import { 
	IonPage, IonHeader, IonToolbar, IonButtons, IonBackButton, 
	IonTitle, IonContent 
} from "@ionic/vue"
import { Search, Calendar, Filter, ChevronRight, PackageSearch } from "lucide-vue-next"
import { formatCurrency } from "@/utils/formatters"

const selectedStatus = ref("All")

const statusStyles = {
	'Active': 'bg-indigo-50 text-indigo-600',
	'Delivered': 'bg-emerald-50 text-emerald-600',
	'Cancelled': 'bg-red-50 text-red-600',
	'Processing': 'bg-amber-50 text-amber-600'
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
.no-scrollbar::-webkit-scrollbar {
	display: none;
}
</style>
