<template>
	<BaseLayout :pageTitle="__('Notification Detail')">
		<template #body>
			<div class="flex flex-col h-full bg-gray-50 overflow-hidden">
				<ion-content>
					<div class="p-6">
						<!-- Icon Header -->
						<div class="flex justify-center my-8">
							<div 
								class="w-24 h-24 rounded-[32px] flex items-center justify-center shadow-xl"
								:class="getTypeStyles(notification.type).bg"
							>
								<component 
									:is="getTypeStyles(notification.type).icon" 
									class="w-12 h-12" 
									:class="getTypeStyles(notification.type).text"
								/>
							</div>
						</div>

						<!-- Content Card -->
						<div class="bg-white rounded-[32px] p-8 shadow-xl shadow-gray-200/50 border border-gray-100 text-center relative overflow-hidden">
							<!-- Decoration -->
							<div class="absolute -top-10 -right-10 w-32 h-32 bg-gray-50 rounded-full blur-3xl"></div>
							
							<span class="relative text-[10px] font-black text-gray-400 uppercase tracking-widest mb-4 block">
								{{ notification.type }} Notification • {{ notification.time }}
							</span>
							
							<h2 class="relative text-2xl font-black text-gray-900 leading-tight mb-4">
								{{ notification.title }}
							</h2>
							
							<p class="relative text-gray-500 leading-relaxed mb-8">
								{{ notification.message }}
							</p>

							<!-- Action Buttons -->
							<div class="relative space-y-3">
								<Button
									v-for="action in actions"
									:key="action.label"
									:variant="action.primary ? 'solid' : 'subtle'"
									:theme="action.theme || 'indigo'"
									size="lg"
									class="w-full !rounded-2xl h-14 font-black transition-all"
									@click="handleAction(action)"
								>
									<template #prefix>
										<component :is="action.icon" class="w-5 h-5 mr-2" />
									</template>
									{{ action.label }}
								</Button>
								
								<button 
									@click="router.back()"
									class="w-full py-4 text-sm font-black text-gray-400 uppercase tracking-widest active:scale-95 transition-all"
								>
									{{ __("Go Back") }}
								</button>
							</div>
						</div>

						<!-- Coupon Card if Offer -->
						<div v-if="notification.type === 'Offer'" class="mt-6 bg-indigo-600 rounded-[32px] p-6 text-white text-center relative overflow-hidden">
							<div class="absolute inset-0 opacity-10">
								<svg class="w-full h-full" viewBox="0 0 100 100" preserveAspectRatio="none">
									<path d="M0 0 L100 0 L100 100 L0 100 Z" fill="none" stroke="currentColor" stroke-width="2" stroke-dasharray="4 4"/>
								</svg>
							</div>
							<p class="text-[10px] font-black uppercase tracking-[0.2em] mb-2 opacity-80">{{ __("Promo Code") }}</p>
							<div class="text-3xl font-black tracking-tighter mb-4 italic">VITA20</div>
							<button class="bg-white text-indigo-600 px-6 py-2 rounded-xl text-xs font-black uppercase tracking-widest active:scale-95 transition-all shadow-lg">
								{{ __("Copy Code") }}
							</button>
						</div>
					</div>
				</ion-content>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { ref, computed, inject } from "vue"
import { useRouter, useRoute } from "vue-router"
import { IonContent } from "@ionic/vue"
import { ShoppingBag, Tag, MessageSquare, Info, ExternalLink, MapPin, Ticket, Copy } from "lucide-vue-next"
import BaseLayout from "@/components/layouts/BaseLayout.vue"

const __ = inject("$translate")
const router = useRouter()
const route = useRoute()

const notification = ref({
	id: route.params.id || 1,
	type: "Order",
	title: "Order Shipped",
	message: "Your order #ORD-2023-001 has been shipped and will be delivered within 2 days. You can track your package using the button below.",
	time: "2 hours ago",
})

const actions = computed(() => {
	switch (notification.value.type) {
		case "Order":
			return [
				{ label: __("Track Order"), icon: MapPin, primary: true, theme: "indigo" },
				{ label: __("Order Details"), icon: ExternalLink, primary: false },
			]
		case "Offer":
			return [
				{ label: __("Shop Now"), icon: ShoppingBag, primary: true, theme: "orange" },
			]
		case "Support":
			return [
				{ label: __("View Ticket"), icon: Ticket, primary: true, theme: "blue" },
			]
		default:
			return [
				{ label: __("Learn More"), icon: Info, primary: true },
			]
	}
})

const handleAction = (action) => {
	console.log("Action clicked:", action.label)
	// Implement navigation based on action
}

const getTypeStyles = (type) => {
	switch (type) {
		case "Order":
			return { icon: ShoppingBag, bg: "bg-emerald-50", text: "text-emerald-600" }
		case "Offer":
			return { icon: Tag, bg: "bg-orange-50", text: "text-orange-600" }
		case "Support":
			return { icon: MessageSquare, bg: "bg-blue-50", text: "text-blue-600" }
		default:
			return { icon: Info, bg: "bg-indigo-50", text: "text-indigo-600" }
	}
}
</script>
