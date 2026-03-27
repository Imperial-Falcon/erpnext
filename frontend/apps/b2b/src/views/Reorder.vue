<template>
	<BaseLayout :pageTitle="__('Reorder')" :showHeader="false">
		<template #body>
			<div class="flex flex-col h-full bg-gray-50 dark:bg-black overflow-hidden relative">
				<AppHeader :title="__('Reorder')" :subtitle="`Order #${orderId}`" :showBack="true" :isScrolled="true" />

				<!-- Ambient Backdrops -->
				<div class="absolute inset-0 overflow-hidden pointer-events-none z-0">
					<div class="absolute top-[25%] left-[-50px] w-[300px] h-[300px] bg-brand-primary/10 blur-[80px] rounded-full"></div>
					<div class="absolute bottom-[30%] right-[-50px] w-[250px] h-[250px] bg-brand-secondary/15 blur-[80px] rounded-full"></div>
				</div>

				<ion-content class="transparent-content">
					<div class="relative z-10">
						<!-- Info Box -->
						<div class="p-5 animate-fade-in-up">
							<div class="app-card rounded-[1.5rem] border border-brand-primary/20 shadow-[0_0_15px_rgba(139,92,246,0.08)] p-4 flex gap-3">
								<div class="w-10 h-10 bg-brand-primary/10 rounded-xl flex items-center justify-center flex-shrink-0">
									<RotateCcw class="w-5 h-5 text-brand-primary" />
								</div>
								<div>
									<h3 class="text-sm font-black text-gray-900 dark:text-gray-100 mb-0.5">Quick Reorder</h3>
									<p class="text-[11px] text-gray-500 dark:text-gray-400 leading-tight">Pre-filled from your previous order. Adjust quantities before checkout.</p>
								</div>
							</div>
						</div>

						<!-- Items List -->
						<div class="px-5 pb-48">
							<div class="flex items-center justify-between mb-3 px-1">
								<h2 class="text-xs font-black text-gray-400 uppercase tracking-widest">Items ({{ items.length }})</h2>
								<button class="text-[10px] font-black text-brand-accent uppercase tracking-widest active:scale-95 transition-all">Clear All</button>
							</div>

							<div class="space-y-3">
								<div
									v-for="(item, index) in items"
									:key="item.id"
									class="app-card rounded-[1.5rem] p-3 shadow-glass border border-white/40 flex gap-4 animate-fade-in-up"
									:style="`animation-delay: ${index * 50}ms`"
								>
									<div class="w-20 h-20 bg-white/50 dark:bg-gray-800/50 rounded-xl flex-shrink-0 flex items-center justify-center p-2 border border-white/50 dark:border-gray-700 shadow-sm">
										<img :src="item.image" :alt="item.name" class="max-w-full max-h-full object-contain mix-blend-multiply dark:mix-blend-normal" />
									</div>

									<div class="flex-1 flex flex-col justify-between py-0.5">
										<div>
											<div class="flex justify-between items-start">
												<h3 class="text-sm font-black text-gray-900 dark:text-gray-100 line-clamp-1 leading-tight">{{ item.name }}</h3>
												<button class="text-gray-400 hover:text-brand-accent active:scale-90 transition-all ml-2 p-1 bg-gray-50/50 dark:bg-gray-800/50 rounded-lg">
													<Trash2 class="w-4 h-4" />
												</button>
											</div>
											<p class="text-[11px] font-bold text-gray-400 uppercase tracking-widest mt-1">{{ item.manufacturer }}</p>
										</div>

										<div class="flex items-end justify-between">
											<span class="text-sm font-black bg-clip-text text-transparent bg-gradient-to-r from-brand-primary to-brand-secondary">
												{{ formatCurrency(item.price * item.quantity, "BDT") }}
											</span>

											<div class="flex items-center px-1.5 py-1 app-card shadow-inner border border-gray-100 dark:border-gray-800 rounded-[1.2rem]">
												<button
													@click="item.quantity > 1 ? item.quantity-- : null"
													class="w-7 h-7 flex items-center justify-center app-card rounded-[0.8rem] shadow-sm text-gray-500 active:scale-95 transition-all"
												>
													<Minus class="w-3.5 h-3.5" />
												</button>
												<span class="w-8 text-center text-xs font-black text-brand-primary">{{ item.quantity }}</span>
												<button
													@click="item.quantity++"
													class="w-7 h-7 flex items-center justify-center app-card rounded-[0.8rem] shadow-sm text-gray-500 active:scale-95 transition-all"
												>
													<Plus class="w-3.5 h-3.5" />
												</button>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</ion-content>

				<!-- Summary & Checkout CTA -->
				<div class="fixed bottom-0 left-0 right-0 app-card rounded-t-[2rem] border-t border-white/40 p-5 pb-8 shadow-[0_-15px_40px_rgba(0,0,0,0.05)] z-50 backdrop-blur-3xl standalone:pb-12">
					<div class="flex items-center justify-between mb-4 px-1">
						<div class="flex flex-col">
							<span class="text-[10px] text-gray-400 font-black uppercase tracking-widest leading-none mb-1">Total Amount</span>
							<span class="text-xl font-black bg-clip-text text-transparent bg-gradient-to-r from-brand-primary to-brand-secondary leading-none">{{ formatCurrency(totalAmount, "BDT") }}</span>
						</div>
						<div class="text-right">
							<span class="block text-[10px] text-emerald-500 font-black uppercase tracking-widest leading-none mb-1">You Save</span>
							<span class="text-sm font-bold text-emerald-500 leading-none">{{ formatCurrency(120, "BDT") }}</span>
						</div>
					</div>
					<button
						@click="$router.push('/checkout')"
						class="w-full h-14 bg-gradient-to-tr from-brand-primary to-brand-secondary text-white font-black rounded-[1.2rem] shadow-neon flex items-center justify-center gap-3 active:scale-[0.98] transition-all"
					>
						<span class="tracking-wide">Proceed to Checkout</span>
						<ArrowRight class="w-5 h-5" />
					</button>
				</div>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { ref, computed, inject } from "vue"
import { useRoute } from "vue-router"
import { IonContent } from "@ionic/vue"
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import AppHeader from "@/components/AppHeader.vue"
import { Trash2, Plus, Minus, RotateCcw, ArrowRight } from "lucide-vue-next"
import { formatCurrency } from "@/utils/formatters"

const __ = inject("$translate")
const route = useRoute()
const orderId = computed(() => route.params.id || "ORD-001")

const items = ref([
	{ id: 1, name: "Napa Extra (Paracetamol)", manufacturer: "Beximco Pharma", price: 25.0, quantity: 10, image: "https://via.placeholder.com/150?text=Napa" },
	{ id: 2, name: "Vitamin C 500mg", manufacturer: "Square Pharma", price: 150.0, quantity: 2, image: "https://via.placeholder.com/150?text=VitC" },
	{ id: 6, name: "Sergel 20mg", manufacturer: "Healthcare Pharma", price: 70.0, quantity: 5, image: "https://via.placeholder.com/150?text=Sergel" },
])

const totalAmount = computed(() => items.value.reduce((sum, item) => sum + item.price * item.quantity, 0))
</script>

<style scoped>
.transparent-content { --background: transparent; }
</style>
