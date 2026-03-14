<template>
	<BaseLayout :pageTitle="__('Notifications')">
		<template #body>
			<div class="flex flex-col h-full bg-gray-50 overflow-hidden">
				<ion-content>
					<div class="p-6">
						<div class="flex items-center justify-between mb-6">
							<h2 class="text-lg font-black text-gray-900">{{ __("Recent Activity") }}</h2>
							<button class="text-xs font-black text-indigo-600 hover:text-indigo-700 active:scale-95 transition-all">
								{{ __("Mark all as read") }}
							</button>
						</div>

						<div v-if="notifications.length > 0" class="space-y-4">
							<div 
								v-for="notification in notifications" 
								:key="notification.id"
								@click="router.push(`/notification-detail/${notification.id}`)"
								class="bg-white rounded-3xl p-5 shadow-sm border border-gray-100 flex gap-4 active:bg-gray-50 transition-colors cursor-pointer relative overflow-hidden"
								:class="{ 'border-l-4 border-l-indigo-600': !notification.read }"
							>
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
										<div v-if="!notification.read" class="w-2 h-2 bg-indigo-600 rounded-full"></div>
									</div>
									<h3 class="font-black text-gray-900 leading-tight mb-1" :class="{ 'pr-4': !notification.read }">
										{{ notification.title }}
									</h3>
									<p class="text-sm text-gray-500 line-clamp-2">
										{{ notification.message }}
									</p>
								</div>
							</div>
						</div>

						<EmptyState
							v-else
							:title="__('All caught up!')"
							:message="__('No new notifications at the moment.')"
						>
							<template #icon>
								<BellOff class="w-12 h-12 text-gray-300" />
							</template>
						</EmptyState>
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

const __ = inject("$translate")
const router = useRouter()

const notifications = ref([
	{
		id: 1,
		type: "Order",
		title: "Order Shipped",
		message: "Your order #ORD-2023-001 has been shipped and will be delivered within 2 days.",
		time: "2 hours ago",
		read: false,
	},
	{
		id: 2,
		type: "Offer",
		title: "Special Offer Just for You!",
		message: "Get 20% flat discount on all vitamins this weekend. Use code VITA20.",
		time: "5 hours ago",
		read: false,
	},
	{
		id: 3,
		type: "Support",
		title: "Ticket Updated",
		message: "Our support team has responded to your ticket #TKT-002 regarding incorrect items.",
		time: "Yesterday",
		read: true,
	},
	{
		id: 4,
		type: "System",
		title: "System Maintenance",
		message: "The app will be down for scheduled maintenance on Sunday from 2 AM to 4 AM.",
		time: "2 days ago",
		read: true,
	},
])

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
