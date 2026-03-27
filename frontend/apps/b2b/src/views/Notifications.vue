<template>
	<BaseLayout :pageTitle="__('Notifications')" :showHeader="false">
		<template #body>
			<div class="flex flex-col h-full bg-gray-50 dark:bg-black overflow-hidden relative">
				<AppHeader :title="__('Notifications')" :showBack="true" :isScrolled="true">
					<template #actions>
						<button @click="markAllRead" class="text-[10px] font-black text-brand-primary bg-brand-primary/10 px-3 py-1.5 rounded-full uppercase tracking-widest active:scale-95 transition-all">
							{{ __("Read All") }}
						</button>
					</template>
				</AppHeader>

				<!-- Ambient Backdrops -->
				<div class="absolute inset-0 overflow-hidden pointer-events-none z-0">
					<div class="absolute top-[25%] left-[-50px] w-[300px] h-[300px] bg-brand-primary/10 blur-[80px] rounded-full"></div>
					<div class="absolute bottom-[25%] right-[-50px] w-[250px] h-[250px] bg-brand-secondary/15 blur-[80px] rounded-full"></div>
				</div>

				<ion-content class="transparent-content">
					<div class="p-5 relative z-10">
						<div v-if="notifications.length > 0" class="space-y-3">
							<div
								v-for="(notification, index) in notifications"
								:key="notification.id"
								@click="router.push(`/notification-detail/${notification.id}`)"
								class="app-card rounded-[1.5rem] p-5 shadow-glass border flex gap-4 active:scale-[0.99] transition-all cursor-pointer relative overflow-hidden animate-fade-in-up"
								:class="!notification.read ? 'border-brand-primary/30 shadow-[0_0_15px_rgba(139,92,246,0.08)]' : 'border-white/40'"
								:style="`animation-delay: ${index * 50}ms`"
							>
								<!-- Unread Indicator Bar -->
								<div v-if="!notification.read" class="absolute left-0 top-3 bottom-3 w-[3px] rounded-r-full bg-gradient-to-b from-brand-primary to-brand-secondary"></div>

								<!-- Type Icon -->
								<div
									class="shrink-0 w-12 h-12 rounded-2xl flex items-center justify-center"
									:class="getTypeStyles(notification.type).bg"
								>
									<component
										:is="getTypeStyles(notification.type).icon"
										class="w-6 h-6"
										:class="getTypeStyles(notification.type).text"
									/>
								</div>

								<!-- Content -->
								<div class="flex-1">
									<div class="flex justify-between items-start mb-1">
										<span class="text-[10px] font-black text-gray-400 uppercase tracking-widest">{{ notification.time }}</span>
										<div v-if="!notification.read" class="w-2.5 h-2.5 bg-gradient-to-tr from-brand-primary to-brand-secondary rounded-full shadow-neon"></div>
									</div>
									<h3 class="font-black text-gray-900 dark:text-gray-100 leading-tight mb-1" :class="{ 'pr-4': !notification.read }">
										{{ notification.title }}
									</h3>
									<p class="text-sm text-gray-500 dark:text-gray-400 line-clamp-2">
										{{ notification.message }}
									</p>
								</div>
							</div>
						</div>

						<div v-else class="flex flex-col items-center justify-center pt-24 text-center animate-fade-in-up">
							<div class="w-24 h-24 app-card rounded-full flex items-center justify-center mb-6 shadow-glass">
								<BellOff class="w-10 h-10 text-gray-300 dark:text-gray-600" />
							</div>
							<h3 class="text-lg font-black text-gray-900 dark:text-gray-100 mb-2">{{ __("All caught up!") }}</h3>
							<p class="text-sm text-gray-400">{{ __("No new notifications at the moment.") }}</p>
						</div>
					</div>
				</ion-content>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { ref, inject } from "vue"
import { useRouter } from "vue-router"
import { IonContent } from "@ionic/vue"
import { ShoppingBag, Tag, MessageSquare, BellOff, Info } from "lucide-vue-next"
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import AppHeader from "@/components/AppHeader.vue"

const __ = inject("$translate")
const router = useRouter()

const notifications = ref([
	{ id: 1, type: "Order", title: "Order Shipped", message: "Your order #ORD-2023-001 has been shipped and will be delivered within 2 days.", time: "2 hours ago", read: false },
	{ id: 2, type: "Offer", title: "Special Offer Just for You!", message: "Get 20% flat discount on all vitamins this weekend. Use code VITA20.", time: "5 hours ago", read: false },
	{ id: 3, type: "Support", title: "Ticket Updated", message: "Our support team has responded to your ticket #TKT-002 regarding incorrect items.", time: "Yesterday", read: true },
	{ id: 4, type: "System", title: "System Maintenance", message: "The app will be down for scheduled maintenance on Sunday from 2 AM to 4 AM.", time: "2 days ago", read: true },
])

const markAllRead = () => {
	notifications.value.forEach(n => n.read = true)
}

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
