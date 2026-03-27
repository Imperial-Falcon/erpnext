<template>
	<BaseLayout :pageTitle="__('Request Medicine')" :showHeader="false">
		<template #body>
			<div class="flex flex-col h-full bg-gray-50 dark:bg-black overflow-hidden relative">
				<AppHeader :title="__('Request Medicine')" :showBack="true" :isScrolled="true" />

				<div class="absolute inset-0 overflow-hidden pointer-events-none z-0">
					<div class="absolute top-[20%] left-[-50px] w-[300px] h-[300px] bg-brand-primary/10 blur-[80px] rounded-full"></div>
					<div class="absolute bottom-[25%] right-[-50px] w-[250px] h-[250px] bg-brand-secondary/15 blur-[80px] rounded-full"></div>
				</div>

				<ion-content class="transparent-content">
					<div class="p-5 relative z-10">
						<div class="app-card rounded-[1.75rem] p-6 shadow-glass border border-white/40 mb-6 animate-fade-in-up">
							<div class="flex items-center gap-3 mb-6">
								<div class="w-12 h-12 rounded-2xl bg-brand-primary/10 flex items-center justify-center"><Pill class="w-6 h-6 text-brand-primary" /></div>
								<div>
									<h2 class="text-xl font-black text-gray-900 dark:text-gray-100">{{ __("Can't find it?") }}</h2>
									<p class="text-[10px] font-black text-gray-400 uppercase tracking-widest">{{ __("Tell us what you need") }}</p>
								</div>
							</div>
							<form @submit.prevent="submitRequest" class="space-y-5">
								<FormControl :label="__('Medicine Name')" v-model="form.medicine_name" :placeholder="__('Enter medicine name')" required>
									<template #prefix><Search class="w-4 h-4 text-gray-400 ml-3" /></template>
								</FormControl>
								<FormControl :label="__('Manufacturer (Optional)')" v-model="form.manufacturer" :placeholder="__('Enter manufacturer')">
									<template #prefix><Factory class="w-4 h-4 text-gray-400 ml-3" /></template>
								</FormControl>
								<div class="grid grid-cols-2 gap-4">
									<FormControl :label="__('Quantity')" type="number" v-model="form.quantity" :placeholder="__('Qty')" required />
									<FormControl :label="__('Unit')" v-model="form.unit" :placeholder="__('Pcs, Box, etc.')" required />
								</div>
								<FormControl :label="__('Additional Message')" type="textarea" v-model="form.message" :placeholder="__('Anything else we should know?')" class="h-32" />
								<button type="submit" :disabled="submitting" class="w-full h-14 bg-gradient-to-tr from-brand-primary to-brand-secondary text-white font-black rounded-[1.2rem] shadow-neon active:scale-[0.98] transition-all disabled:opacity-50">
									{{ submitting ? __("Submitting...") : __("Submit Request") }}
								</button>
							</form>
						</div>

						<div class="rounded-[1.75rem] p-6 text-white relative overflow-hidden bg-gradient-to-br from-brand-primary via-violet-600 to-brand-secondary shadow-neon animate-fade-in-up" style="animation-delay: 50ms">
							<div class="absolute inset-0 bg-[radial-gradient(circle_at_80%_20%,rgba(255,255,255,0.1)_0%,transparent_50%)]"></div>
							<div class="relative flex items-start gap-4">
								<div class="p-3 bg-white/20 rounded-2xl backdrop-blur-md"><Info class="w-6 h-6 text-white" /></div>
								<div>
									<h3 class="font-black mb-1">{{ __("What happens next?") }}</h3>
									<p class="text-sm text-white/80 leading-relaxed">{{ __("Our team will check the availability with our suppliers and get back to you within 24 hours via notifications.") }}</p>
								</div>
							</div>
						</div>
					</div>
				</ion-content>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { ref, inject } from "vue"
import { IonContent } from "@ionic/vue"
import { Pill, Search, Factory, Info } from "lucide-vue-next"
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import AppHeader from "@/components/AppHeader.vue"
import { showSuccessAlert } from "@/utils/dialogs"

const __ = inject("$translate")
const submitting = ref(false)
const form = ref({ medicine_name: "", manufacturer: "", quantity: 1, unit: "Pcs", message: "" })

const submitRequest = async () => {
	if (!form.value.medicine_name) return
	submitting.value = true
	setTimeout(() => {
		submitting.value = false
		showSuccessAlert(__("Your request has been submitted successfully! We'll notify you once we find it."))
		form.value = { medicine_name: "", manufacturer: "", quantity: 1, unit: "Pcs", message: "" }
	}, 1500)
}
</script>

<style scoped>
.transparent-content { --background: transparent; }
</style>
