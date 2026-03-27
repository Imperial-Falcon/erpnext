<template>
	<BaseLayout :pageTitle="__('Notification Detail')" :showHeader="false">
		<template #body>
			<div class="flex flex-col h-full bg-gray-50 dark:bg-black overflow-hidden relative">
				<AppHeader :title="__('Details')" :showBack="true" :isScrolled="true" />

				<!-- Ambient Backdrops -->
				<div class="absolute inset-0 overflow-hidden pointer-events-none z-0">
					<div class="absolute top-[15%] left-[-50px] w-[300px] h-[300px] bg-brand-primary/10 blur-[80px] rounded-full"></div>
					<div class="absolute bottom-[25%] right-[-50px] w-[250px] h-[250px] bg-brand-secondary/15 blur-[80px] rounded-full"></div>
				</div>

				<ion-content class="transparent-content">
					<div class="p-5 relative z-10">
						<!-- Icon Header -->
						<div class="flex justify-center my-6 animate-fade-in-up">
							<div
								class="w-20 h-20 rounded-[2rem] flex items-center justify-center shadow-glass app-card border border-white/40"
								:class="getTypeStyles(notification.type).bg"
							>
								<component
									:is="getTypeStyles(notification.type).icon"
									class="w-10 h-10"
									:class="getTypeStyles(notification.type).text"
								/>
							</div>
						</div>

						<!-- Content Card -->
						<div class="app-card rounded-[1.75rem] p-8 shadow-glass border border-white/40 text-center relative overflow-hidden mb-6 animate-fade-in-up" style="animation-delay: 50ms">
							<div class="absolute -top-10 -right-10 w-32 h-32 bg-brand-primary/5 rounded-full blur-3xl"></div>

							<span class="relative text-[10px] font-black text-gray-400 uppercase tracking-widest mb-4 block">
								{{ notification.type }} Notification • {{ notification.time }}
							</span>
							<h2 class="relative text-2xl font-black text-gray-900 dark:text-gray-100 leading-tight mb-4">
								{{ notification.title }}
							</h2>
							<p class="relative text-gray-500 dark:text-gray-400 leading-relaxed mb-8">
								{{ notification.message }}
							</p>

							<!-- Action Buttons -->
							<div class="relative space-y-3">
								<button
									v-for="action in actions"
									:key="action.label"
									@click="handleAction(action)"
									class="w-full flex items-center justify-center gap-2 h-14 rounded-[1.2rem] font-black transition-all active:scale-[0.98]"
									:class="action.primary
										? 'bg-gradient-to-tr from-brand-primary to-brand-secondary text-white shadow-neon'
										: 'app-card border border-white/40 text-gray-700 dark:text-gray-300 shadow-glass'"
								>
									<component :is="action.icon" class="w-5 h-5" />
									<span>{{ action.label }}</span>
								</button>

								<button
									@click="router.back()"
									class="w-full py-4 text-sm font-black text-gray-400 uppercase tracking-widest active:scale-95 transition-all hover:text-brand-primary"
								>
									{{ __("Go Back") }}
								</button>
							</div>
						</div>

						<!-- Coupon Card if Offer -->
						<div v-if="notification.type === 'Offer'" class="rounded-[1.75rem] p-6 text-white text-center relative overflow-hidden bg-gradient-to-br from-brand-primary via-violet-600 to-brand-secondary shadow-neon animate-fade-in-up" style="animation-delay: 100ms">
							<div class="absolute inset-0 bg-[radial-gradient(circle_at_30%_70%,rgba(255,255,255,0.1)_0%,transparent_50%)]"></div>
							<p class="relative text-[10px] font-black uppercase tracking-[0.2em] mb-2 opacity-80">{{ __("Promo Code") }}</p>
							<div class="relative text-3xl font-black tracking-tighter mb-4 italic">VITA20</div>
							<button class="relative bg-white text-brand-primary px-6 py-2.5 rounded-xl text-xs font-black uppercase tracking-widest active:scale-95 transition-all shadow-lg">
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
import { ShoppingBag, Tag, MessageSquare, Info, ExternalLink, MapPin, Ticket } from "lucide-vue-next"
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import AppHeader from "@/components/AppHeader.vue"

const __ = inject("$translate")
const router = useRouter()
const route = useRoute()

const notification = ref({
	id: route.params.id || 1, type: "Order", title: "Order Shipped",
	message: "Your order #ORD-2023-001 has been shipped and will be delivered within 2 days. You can track your package using the button below.",
	time: "2 hours ago",
})

const actions = computed(() => {
	switch (notification.value.type) {
		case "Order": return [
			{ label: __("Track Order"), icon: MapPin, primary: true },
			{ label: __("Order Details"), icon: ExternalLink, primary: false },
		]
		case "Offer": return [{ label: __("Shop Now"), icon: ShoppingBag, primary: true }]
		case "Support": return [{ label: __("View Ticket"), icon: Ticket, primary: true }]
		default: return [{ label: __("Learn More"), icon: Info, primary: true }]
	}
})

const handleAction = (action) => { console.log("Action:", action.label) }

const getTypeStyles = (type) => {
	switch (type) {
		case "Order": return { icon: ShoppingBag, bg: "bg-emerald-500/10", text: "text-emerald-600" }
		case "Offer": return { icon: Tag, bg: "bg-orange-500/10", text: "text-orange-500" }
		case "Support": return { icon: MessageSquare, bg: "bg-sky-500/10", text: "text-sky-600" }
		default: return { icon: Info, bg: "bg-brand-primary/10", text: "text-brand-primary" }
	}
}
</script>

<style scoped>
.transparent-content { --background: transparent; }
</style>
