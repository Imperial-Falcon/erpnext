<template>
	<BaseLayout :pageTitle="__('Request Medicine')">
		<template #body>
			<div class="flex flex-col h-full bg-gray-50 overflow-hidden">
				<ion-content>
					<div class="p-6">
						<div class="bg-white rounded-3xl p-6 shadow-xl shadow-gray-200/50 border border-gray-100 mb-6">
							<div class="flex items-center gap-3 mb-6">
								<div class="w-12 h-12 rounded-2xl bg-indigo-50 flex items-center justify-center text-indigo-600">
									<Pill class="w-6 h-6" />
								</div>
								<div>
									<h2 class="text-xl font-black text-gray-900">{{ __("Can't find it?") }}</h2>
									<p class="text-xs font-bold text-gray-400 uppercase tracking-widest">{{ __("Tell us what you need") }}</p>
								</div>
							</div>

							<form @submit.prevent="submitRequest" class="space-y-5">
								<FormControl
									:label="__('Medicine Name')"
									v-model="form.medicine_name"
									:placeholder="__('Enter medicine name')"
									required
								>
									<template #prefix>
										<Search class="w-4 h-4 text-gray-400 ml-3" />
									</template>
								</FormControl>

								<FormControl
									:label="__('Manufacturer (Optional)')"
									v-model="form.manufacturer"
									:placeholder="__('Enter manufacturer')"
								>
									<template #prefix>
										<Factory class="w-4 h-4 text-gray-400 ml-3" />
									</template>
								</FormControl>

								<div class="grid grid-cols-2 gap-4">
									<FormControl
										:label="__('Quantity')"
										type="number"
										v-model="form.quantity"
										:placeholder="__('Qty')"
										required
									/>
									<FormControl
										:label="__('Unit')"
										v-model="form.unit"
										:placeholder="__('Pcs, Box, etc.')"
										required
									/>
								</div>

								<FormControl
									:label="__('Additional Message')"
									type="textarea"
									v-model="form.message"
									:placeholder="__('Anything else we should know?')"
									class="h-32"
								/>

								<Button
									variant="solid"
									theme="indigo"
									size="lg"
									class="w-full !rounded-2xl h-14 font-black shadow-lg shadow-indigo-200 active:scale-[0.98] transition-all"
									:loading="submitting"
									type="submit"
								>
									{{ __("Submit Request") }}
								</Button>
							</form>
						</div>

						<!-- Info Card -->
						<div class="bg-indigo-600 rounded-3xl p-6 text-white relative overflow-hidden">
							<div class="absolute -top-10 -right-10 w-32 h-32 bg-white/10 rounded-full blur-2xl"></div>
							<div class="relative flex items-start gap-4">
								<div class="p-3 bg-white/20 rounded-2xl backdrop-blur-md">
									<Info class="w-6 h-6 text-white" />
								</div>
								<div>
									<h3 class="font-black mb-1">{{ __("What happens next?") }}</h3>
									<p class="text-sm text-indigo-100 leading-relaxed">
										{{ __("Our team will check the availability with our suppliers and get back to you within 24 hours via notifications.") }}
									</p>
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
import { showErrorAlert, showSuccessAlert } from "@/utils/dialogs"

const __ = inject("$translate")
const submitting = ref(false)

const form = ref({
	medicine_name: "",
	manufacturer: "",
	quantity: 1,
	unit: "Pcs",
	message: "",
})

const submitRequest = async () => {
	if (!form.value.medicine_name) return
	
	submitting.value = true
	// Mock API call
	setTimeout(() => {
		submitting.value = false
		showSuccessAlert(__("Your request has been submitted successfully! We'll notify you once we find it."))
		form.value = {
			medicine_name: "",
			manufacturer: "",
			quantity: 1,
			unit: "Pcs",
			message: "",
		}
	}, 1500)
}
</script>
