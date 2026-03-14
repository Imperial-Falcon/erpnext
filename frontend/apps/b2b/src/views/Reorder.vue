<template>
	<BaseLayout pageTitle="Reorder">
		<template #body>
			<div class="flex flex-col h-full bg-gray-50 overflow-hidden">
				<!-- Header -->
				<div class="bg-white p-4 shadow-sm z-10 flex items-center gap-4">
					<button @click="$router.back()" class="p-2 hover:bg-gray-100 rounded-full transition-colors">
						<ChevronLeft class="w-6 h-6 text-gray-700" />
					</button>
					<div>
						<h1 class="text-lg font-black text-gray-900 leading-tight">Reorder</h1>
						<p class="text-xs text-gray-400 font-medium">Based on Order #{{ orderId }}</p>
					</div>
				</div>

				<ion-content>
					<!-- Info Box -->
					<div class="p-4">
						<div class="bg-indigo-50 border border-indigo-100 rounded-2xl p-4 flex gap-3">
							<div class="w-10 h-10 bg-indigo-100 rounded-xl flex items-center justify-center flex-shrink-0">
								<RotateCcw class="w-5 h-5 text-indigo-600" />
							</div>
							<div>
								<h3 class="text-sm font-bold text-indigo-900 mb-0.5">Quick Reorder</h3>
								<p class="text-[11px] text-indigo-700 leading-tight">We've pre-filled your cart with items from your previous order. You can adjust quantities before checkout.</p>
							</div>
						</div>
					</div>

					<!-- Items List -->
					<div class="px-4 pb-32">
						<div class="flex items-center justify-between mb-3 px-1">
							<h2 class="text-xs font-black text-gray-400 uppercase tracking-widest">Items ({{ items.length }})</h2>
							<button class="text-xs font-bold text-red-500 hover:text-red-600 transition-colors">Clear All</button>
						</div>

						<div class="space-y-3">
							<div v-for="item in items" :key="item.id" class="bg-white rounded-2xl p-3 shadow-sm border border-gray-100 flex gap-4">
								<!-- Item Image -->
								<div class="w-20 h-20 bg-gray-50 rounded-xl flex-shrink-0 flex items-center justify-center p-2">
									<img :src="item.image" :alt="item.name" class="max-w-full max-h-full object-contain" />
								</div>

								<!-- Item Details -->
								<div class="flex-1 flex flex-col justify-between py-0.5">
									<div>
										<div class="flex justify-between items-start">
											<h3 class="text-sm font-bold text-gray-900 line-clamp-1 leading-tight">
												{{ item.name }}
											</h3>
											<button class="text-gray-300 hover:text-red-500">
												<Trash2 class="w-4 h-4" />
											</button>
										</div>
										<p class="text-[11px] text-gray-500 mt-1">{{ item.manufacturer }}</p>
									</div>

									<div class="flex items-end justify-between">
										<span class="text-base font-black text-indigo-600">
											{{ formatCurrency(item.price * item.quantity, "BDT") }}
										</span>
										
										<!-- Quantity Controls -->
										<div class="flex items-center bg-gray-50 rounded-lg p-1 border border-gray-100">
											<button 
												@click="item.quantity > 1 ? item.quantity-- : null"
												class="w-7 h-7 flex items-center justify-center bg-white rounded-md shadow-sm text-gray-600 active:scale-90 transition-all"
											>
												<Minus class="w-3.5 h-3.5" />
											</button>
											<span class="w-8 text-center text-xs font-black text-gray-900">{{ item.quantity }}</span>
											<button 
												@click="item.quantity++"
												class="w-7 h-7 flex items-center justify-center bg-indigo-600 rounded-md shadow-sm text-white active:scale-90 transition-all"
											>
												<Plus class="w-3.5 h-3.5" />
											</button>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</ion-content>

				<!-- Summary & Checkout CTA -->
				<div class="fixed bottom-0 left-0 right-0 bg-white/80 backdrop-blur-md border-t border-gray-100 p-4 pb-8 z-20">
					<div class="flex items-center justify-between mb-4 px-2">
						<div class="flex flex-col">
							<span class="text-[10px] text-gray-400 font-bold uppercase tracking-widest leading-none mb-1">Total Amount</span>
							<span class="text-xl font-black text-gray-900 leading-none">{{ formatCurrency(totalAmount, "BDT") }}</span>
						</div>
						<div class="text-right">
							<span class="block text-[10px] text-green-600 font-bold uppercase tracking-widest leading-none mb-1">You Save</span>
							<span class="text-sm font-bold text-green-600 leading-none">{{ formatCurrency(120, "BDT") }}</span>
						</div>
					</div>
					<button 
						@click="$router.push('/checkout')"
						class="w-full py-4 bg-indigo-600 text-white font-black rounded-2xl shadow-xl shadow-indigo-100 flex items-center justify-center gap-3 active:scale-[0.98] transition-all"
					>
						<span>Proceed to Checkout</span>
						<ArrowRight class="w-5 h-5" />
					</button>
				</div>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { ref, computed } from "vue"
import { useRoute } from "vue-router"
import { IonContent } from "@ionic/vue"
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import { ChevronLeft, Trash2, Plus, Minus, RotateCcw, ArrowRight } from "lucide-vue-next"
import { formatCurrency } from "@/utils/formatters"

const route = useRoute()
const orderId = computed(() => route.params.id || "ORD-001")

// Mock data - in a real app, this would be fetched based on the orderId
const items = ref([
	{ id: 1, name: "Napa Extra (Paracetamol)", manufacturer: "Beximco Pharma", price: 25.0, quantity: 10, image: "https://via.placeholder.com/150?text=Napa" },
	{ id: 2, name: "Vitamin C 500mg", manufacturer: "Square Pharma", price: 150.0, quantity: 2, image: "https://via.placeholder.com/150?text=VitC" },
	{ id: 6, name: "Sergel 20mg", manufacturer: "Healthcare Pharma", price: 70.0, quantity: 5, image: "https://via.placeholder.com/150?text=Sergel" },
])

const totalAmount = computed(() => {
	return items.value.reduce((sum, item) => sum + item.price * item.quantity, 0)
})
</script>
