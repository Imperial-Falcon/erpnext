<template>
	<BaseLayout :pageTitle="__('Ticket Details')">
		<template #body>
			<div class="flex flex-col h-full bg-gray-50 overflow-hidden">
				<ion-content>
					<div class="p-6 pb-32">
						<!-- Ticket Header -->
						<div class="bg-white rounded-3xl p-6 shadow-sm border border-gray-100 mb-6">
							<div class="flex justify-between items-start mb-4">
								<h2 class="text-xl font-black text-gray-900 leading-tight">{{ ticket.subject }}</h2>
								<div 
									class="shrink-0 px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-wider"
									:class="ticket.status === 'Open' ? 'bg-orange-50 text-orange-600' : 'bg-green-50 text-green-600'"
								>
									{{ ticket.status }}
								</div>
							</div>
							<div class="flex items-center gap-4 text-xs font-bold text-gray-400 uppercase tracking-widest">
								<span>{{ ticket.id }}</span>
								<span class="w-1 h-1 bg-gray-300 rounded-full"></span>
								<span>{{ ticket.date }}</span>
							</div>
						</div>

						<!-- Message History -->
						<div class="space-y-6">
							<div 
								v-for="(msg, index) in ticket.messages" 
								:key="index"
								class="flex flex-col"
								:class="msg.sender === 'User' ? 'items-end' : 'items-start'"
							>
								<div class="flex items-center gap-2 mb-2 px-2">
									<span class="text-[10px] font-black text-gray-400 uppercase tracking-widest">{{ msg.sender_name }}</span>
									<span class="text-[10px] font-bold text-gray-300">{{ msg.time }}</span>
								</div>
								<div 
									class="max-w-[85%] p-4 rounded-3xl text-sm leading-relaxed shadow-sm"
									:class="msg.sender === 'User' 
										? 'bg-indigo-600 text-white rounded-tr-none' 
										: 'bg-white text-gray-700 border border-gray-100 rounded-tl-none'"
								>
									{{ msg.content }}
								</div>
							</div>
						</div>
					</div>
				</ion-content>

				<!-- Reply Input -->
				<div class="absolute bottom-0 left-0 right-0 p-4 bg-white/80 backdrop-blur-md border-t border-gray-100 flex items-center gap-3">
					<div class="flex-1 bg-gray-50 rounded-2xl px-4 py-2 border border-gray-200">
						<textarea 
							v-model="replyText" 
							:placeholder="__('Type your message...')"
							class="w-full bg-transparent border-none focus:ring-0 text-sm py-1 resize-none h-10 no-scrollbar"
						></textarea>
					</div>
					<button 
						@click="sendReply"
						:disabled="!replyText.trim()"
						class="w-12 h-12 rounded-2xl bg-indigo-600 flex items-center justify-center text-white shadow-lg shadow-indigo-100 active:scale-90 transition-all disabled:opacity-50"
					>
						<Send class="w-5 h-5" />
					</button>
				</div>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { ref, inject } from "vue"
import { useRoute } from "vue-router"
import { IonContent } from "@ionic/vue"
import { Send } from "lucide-vue-next"
import BaseLayout from "@/components/layouts/BaseLayout.vue"

const __ = inject("$translate")
const route = useRoute()
const replyText = ref("")

const ticket = ref({
	id: route.params.id || "TKT-002",
	subject: "Incorrect item received",
	status: "Open",
	date: "Oct 15, 2023",
	messages: [
		{
			sender: "User",
			sender_name: "You",
			time: "10:30 AM",
			content: "I received Panadol instead of Napa Extra. Please check the order and replace it as soon as possible.",
		},
		{
			sender: "Support",
			sender_name: "Support Team",
			time: "11:45 AM",
			content: "Hello! We've received your complaint. Our delivery partner will visit you today to collect the wrong item and deliver the correct one. We're sorry for the mistake.",
		},
		{
			sender: "User",
			sender_name: "You",
			time: "12:00 PM",
			content: "Thank you. What time will they arrive?",
		},
	],
})

const sendReply = () => {
	if (!replyText.value.trim()) return
	
	ticket.value.messages.push({
		sender: "User",
		sender_name: "You",
		time: "Now",
		content: replyText.value,
	})
	replyText.value = ""
}
</script>

<style scoped>
.no-scrollbar::-webkit-scrollbar {
	display: none;
}
</style>
