<template>
	<BaseLayout :pageTitle="__('Support Tickets')">
		<template #body>
			<div class="flex flex-col h-full bg-gray-50 overflow-hidden">
				<ion-content>
					<div class="p-6">
						<div class="flex items-center justify-between mb-6">
							<h2 class="text-lg font-black text-gray-900">{{ __("My Inquiries") }}</h2>
							<button 
								@click="router.push('/contact')"
								class="flex items-center gap-2 px-4 py-2 bg-indigo-600 text-white rounded-xl text-xs font-black shadow-md shadow-indigo-100 active:scale-95 transition-all"
							>
								<Plus class="w-4 h-4" />
								<span>{{ __("New Ticket") }}</span>
							</button>
						</div>

						<div v-if="tickets.length > 0" class="space-y-4">
							<div 
								v-for="ticket in tickets" 
								:key="ticket.id"
								@click="router.push(`/contact-detail/${ticket.id}`)"
								class="bg-white rounded-3xl p-5 shadow-sm border border-gray-100 active:bg-gray-50 transition-colors cursor-pointer"
							>
								<div class="flex justify-between items-start mb-3">
									<div class="flex flex-col">
										<span class="text-[10px] font-black text-gray-400 uppercase tracking-widest mb-1">{{ ticket.date }}</span>
										<h3 class="font-black text-gray-900 leading-tight">{{ ticket.subject }}</h3>
									</div>
									<div 
										class="px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-wider"
										:class="ticket.status === 'Open' ? 'bg-orange-50 text-orange-600' : 'bg-green-50 text-green-600'"
									>
										{{ ticket.status }}
									</div>
								</div>
								
								<p class="text-sm text-gray-500 line-clamp-2 mb-4">
									{{ ticket.last_message }}
								</p>

								<div class="flex items-center justify-between pt-4 border-t border-gray-50">
									<div class="flex -space-x-2">
										<div class="w-7 h-7 rounded-full bg-indigo-100 border-2 border-white flex items-center justify-center text-[10px] font-black text-indigo-600 uppercase">
											U
										</div>
										<div v-if="ticket.status === 'Closed'" class="w-7 h-7 rounded-full bg-gray-100 border-2 border-white flex items-center justify-center text-[10px] font-black text-gray-600 uppercase">
											S
										</div>
									</div>
									<div class="flex items-center gap-1 text-indigo-600 text-xs font-black">
										<span>{{ __("View Details") }}</span>
										<ChevronRight class="w-4 h-4" />
									</div>
								</div>
							</div>
						</div>

						<EmptyState
							v-else
							:title="__('No tickets found')"
							:message="__('You haven\'t raised any support tickets yet.')"
						>
							<template #icon>
								<MessageSquareOff class="w-12 h-12 text-gray-300" />
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
import { Plus, ChevronRight, MessageSquareOff } from "lucide-vue-next"
import BaseLayout from "@/components/layouts/BaseLayout.vue"

const __ = inject("$translate")
const router = useRouter()

const tickets = ref([
	{
		id: "TKT-001",
		date: "Oct 12, 2023",
		subject: "Delayed delivery for Order #12345",
		status: "Closed",
		last_message: "The delivery was delayed due to heavy rain. We apologize for the inconvenience. Your package should arrive tomorrow.",
	},
	{
		id: "TKT-002",
		date: "Oct 15, 2023",
		subject: "Incorrect item received",
		status: "Open",
		last_message: "I received Panadol instead of Napa Extra. Please check the order and replace it as soon as possible.",
	},
	{
		id: "TKT-003",
		date: "Oct 18, 2023",
		subject: "Payment query",
		status: "Open",
		last_message: "The amount was deducted from my account but the order status is still 'Pending Payment'.",
	},
])
</script>
