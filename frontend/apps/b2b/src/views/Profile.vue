<template>
	<ion-page>
		<ion-header class="ion-no-border" mode="ios">
			<ion-toolbar class="px-2">
				<ion-title class="text-xl font-black">{{ __("My Profile") }}</ion-title>
				<ion-buttons slot="end">
					<button 
						@click="$router.push('/settings')"
						class="p-2 bg-gray-50 rounded-xl active:scale-90 transition-all mr-2"
					>
						<Settings class="w-5 h-5 text-gray-700" />
					</button>
				</ion-buttons>
			</ion-toolbar>
		</ion-header>

		<ion-content>
			<div class="flex flex-col bg-gray-50/30 pb-24">
				<!-- Profile Header Card -->
				<div class="px-4 pt-6 pb-8">
					<div class="bg-white rounded-[32px] p-6 shadow-xl shadow-gray-200/50 border border-gray-100 flex flex-col items-center text-center relative overflow-hidden">
						<!-- Background Decoration -->
						<div class="absolute -top-10 -right-10 w-32 h-32 bg-indigo-50 rounded-full blur-3xl"></div>
						<div class="absolute -bottom-10 -left-10 w-32 h-32 bg-pink-50 rounded-full blur-3xl"></div>

						<div class="relative mb-4">
							<img
								v-if="user.data.user_image"
								class="h-24 w-24 rounded-3xl object-cover shadow-lg border-4 border-white"
								:src="user.data.user_image"
								:alt="user.data.first_name"
							/>
							<div
								v-else
								class="flex items-center justify-center bg-gradient-to-br from-indigo-500 to-purple-600 text-white text-3xl font-black h-24 w-24 rounded-3xl shadow-lg border-4 border-white uppercase"
							>
								{{ user.data.first_name[0] }}
							</div>
							<button class="absolute -bottom-1 -right-1 p-2 bg-white rounded-xl shadow-md border border-gray-100 text-indigo-600">
								<Camera class="w-4 h-4" />
							</button>
						</div>

						<h2 class="text-xl font-black text-gray-900 leading-tight">
							{{ employee?.data?.employee_name || user.data.first_name + ' ' + user.data.last_name }}
						</h2>
						<p class="text-sm font-bold text-gray-400 mt-1">
							{{ employee?.data?.designation || user.data.email }}
						</p>

						<!-- Mini Stats -->
						<div class="grid grid-cols-3 w-full mt-8 pt-6 border-t border-gray-50">
							<div class="flex flex-col items-center">
								<span class="text-lg font-black text-gray-900">12</span>
								<span class="text-[10px] font-black text-gray-400 uppercase tracking-widest">Orders</span>
							</div>
							<div class="flex flex-col items-center border-x border-gray-50 px-2">
								<span class="text-lg font-black text-gray-900">4</span>
								<span class="text-[10px] font-black text-gray-400 uppercase tracking-widest">Offers</span>
							</div>
							<div class="flex flex-col items-center">
								<span class="text-lg font-black text-gray-900">240</span>
								<span class="text-[10px] font-black text-gray-400 uppercase tracking-widest">Points</span>
							</div>
						</div>
					</div>
				</div>

				<!-- Menu Sections -->
				<div class="px-4 space-y-6">
					<!-- General Section -->
					<div>
						<h3 class="px-4 text-[10px] font-black text-gray-400 uppercase tracking-[0.2em] mb-3">General</h3>
						<div class="bg-white rounded-3xl shadow-sm border border-gray-100 overflow-hidden">
							<div
								v-for="(link, index) in generalLinks"
								:key="link.title"
								@click="handleLinkClick(link)"
								class="flex items-center justify-between p-4 active:bg-gray-50 transition-colors cursor-pointer"
								:class="{ 'border-b border-gray-50': index !== generalLinks.length - 1 }"
							>
								<div class="flex items-center gap-4">
									<div class="w-10 h-10 rounded-2xl flex items-center justify-center bg-gray-50" :class="link.iconColor">
										<component :is="link.icon" class="w-5 h-5" />
									</div>
									<span class="text-sm font-bold text-gray-900">{{ link.title }}</span>
								</div>
								<ChevronRight class="w-5 h-5 text-gray-300" />
							</div>
						</div>
					</div>

					<!-- Support Section -->
					<div>
						<h3 class="px-4 text-[10px] font-black text-gray-400 uppercase tracking-[0.2em] mb-3">Support & Legal</h3>
						<div class="bg-white rounded-3xl shadow-sm border border-gray-100 overflow-hidden">
							<div
								v-for="(link, index) in supportLinks"
								:key="link.title"
								@click="handleLinkClick(link)"
								class="flex items-center justify-between p-4 active:bg-gray-50 transition-colors cursor-pointer"
								:class="{ 'border-b border-gray-50': index !== supportLinks.length - 1 }"
							>
								<div class="flex items-center gap-4">
									<div class="w-10 h-10 rounded-2xl flex items-center justify-center bg-gray-50" :class="link.iconColor">
										<component :is="link.icon" class="w-5 h-5" />
									</div>
									<span class="text-sm font-bold text-gray-900">{{ link.title }}</span>
								</div>
								<ChevronRight class="w-5 h-5 text-gray-300" />
							</div>
						</div>
					</div>

					<!-- Logout -->
					<div class="pt-4">
						<button
							@click="logout"
							class="w-full py-5 bg-red-50 text-red-600 font-black rounded-3xl flex items-center justify-center gap-3 active:scale-[0.98] transition-all border border-red-100 mb-10"
						>
							<LogOut class="w-5 h-5" />
							<span>Log Out</span>
						</button>
					</div>
				</div>
			</div>

			<!-- Keep original modal for info -->
			<ion-modal
				ref="modal"
				:is-open="isInfoModalOpen"
				@didDismiss="closeInfoModal"
				:initial-breakpoint="1"
				:breakpoints="[0, 1]"
			>
				<ProfileInfoModal
					v-if="selectedItem"
					:title="selectedItem.title"
					:data="
						selectedItem.fields?.map((field) => {
							const [label, fieldtype] = getFieldInfo(field)
							return {
								fieldname: field,
								value: employeeDoc.doc[field],
								label: label,
								fieldtype: fieldtype,
							}
						})
					"
				/>
			</ion-modal>
		</ion-content>
	</ion-page>
</template>

<script setup>
import { computed, inject, ref, onMounted, onBeforeUnmount } from "vue"
import { useRouter } from "vue-router"
import { IonModal, IonPage, IonContent, IonHeader, IonToolbar, IonTitle, IonButtons } from "@ionic/vue"
import { 
	Settings, Camera, ChevronRight, ShoppingBag, Box, 
	MessageSquare, Key, Share2, Star, Headphones, LogOut 
} from "lucide-vue-next"
import { createDocumentResource, createResource } from "frappe-ui"

import { showErrorAlert } from "@/utils/dialogs"
import { formatCurrency } from "@/utils/formatters"
import ProfileInfoModal from "@/components/ProfileInfoModal.vue"

const DOCTYPE = "Employee"

const socket = inject("$socket")
const session = inject("$session")
const user = inject("$user")
const employee = inject("$employee")
const __ = inject("$translate")

const router = useRouter()

const generalLinks = [
	{
		icon: ShoppingBag,
		iconColor: "text-indigo-600 bg-indigo-50",
		title: __("My Orders"),
		route: "/orders",
	},
	{
		icon: Box,
		iconColor: "text-emerald-600 bg-emerald-50",
		title: __("My Products"),
		route: "/my-products",
	},
	{
		icon: MessageSquare,
		iconColor: "text-orange-600 bg-orange-50",
		title: __("Request Medicine"),
		route: "/request-medicine",
	},
	{
		icon: Key,
		iconColor: "text-purple-600 bg-purple-50",
		title: __("Change Password"),
		route: "/change-password",
	},
]

const supportLinks = [
	{
		icon: Share2,
		iconColor: "text-blue-600 bg-blue-50",
		title: __("Follow Us"),
		route: "/follow-us",
	},
	{
		icon: Star,
		iconColor: "text-yellow-600 bg-yellow-50",
		title: __("Rate Us"),
	},
	{
		icon: Headphones,
		iconColor: "text-pink-600 bg-pink-50",
		title: __("Contact Support"),
		route: "/contact",
	},
]

const isInfoModalOpen = ref(false)
const selectedItem = ref(null)

const handleLinkClick = (link) => {
	if (link.route) {
		router.push(link.route)
	} else {
		selectedItem.value = link
		// isInfoModalOpen.value = true // Only open if fields exist
	}
}

const closeInfoModal = () => {
	isInfoModalOpen.value = false
	selectedItem.value = null
}

const employeeDoc = createDocumentResource({
	doctype: DOCTYPE,
	name: employee.data.name,
	fields: "*",
	auto: true,
	transform: (data) => {
		data.ctc = formatCurrency(data.ctc, data.salary_currency)
		return data
	},
})

const employeeDocType = createResource({
	url: "hrms.api.get_doctype_fields",
	params: { doctype: DOCTYPE },
	auto: true,
})

const getFieldInfo = (fieldname) => {
	const field = employeeDocType.data.find(
		(field) => field.fieldname === fieldname
	)
	return [__(field?.label, null, "Employee"), field?.fieldtype]
}

const logout = async () => {
	try {
		await session.logout.submit()
	} catch (e) {
		const msg = "An error occurred while attempting to log out!"
		console.error(msg, e)
		showErrorAlert(msg)
	}
}

onMounted(() => {
	socket.emit("doctype_subscribe", DOCTYPE)
	socket.on("list_update", (data) => {
		if (data.doctype === DOCTYPE && data.name === employee.data.name) {
			employeeDoc.reload()
		}
	})
})

onBeforeUnmount(() => {
	socket.emit("doctype_unsubscribe", DOCTYPE)
	socket.off("list_update")
})
</script>

<style scoped>
ion-toolbar {
	--background: transparent;
	--border-width: 0;
}
</style>
