<template>
	<BaseLayout :pageTitle="__('Contact Support')">
		<template #body>
			<div class="flex flex-col h-full bg-gray-50 overflow-hidden">
				<ion-content>
					<div class="p-6">
						<div class="bg-white rounded-3xl p-6 shadow-xl shadow-gray-200/50 border border-gray-100 mb-6">
							<div class="flex items-center gap-3 mb-6">
								<div class="w-12 h-12 rounded-2xl bg-indigo-50 flex items-center justify-center text-indigo-600">
									<MessageCircle class="w-6 h-6" />
								</div>
								<div>
									<h2 class="text-xl font-black text-gray-900">{{ __("How can we help?") }}</h2>
									<p class="text-xs font-bold text-gray-400 uppercase tracking-widest">{{ __("Send us a message") }}</p>
								</div>
							</div>

							<form @submit.prevent="submitContact" class="space-y-5">
								<FormControl
									:label="__('Subject')"
									v-model="form.subject"
									:placeholder="__('What is this about?')"
									required
								>
									<template #prefix>
										<Tag class="w-4 h-4 text-gray-400 ml-3" />
									</template>
								</FormControl>

								<FormControl
									:label="__('Message')"
									type="textarea"
									v-model="form.message"
									:placeholder="__('Describe your issue or question in detail...')"
									required
									class="h-48"
								/>

								<Button
									variant="solid"
									theme="indigo"
									size="lg"
									class="w-full !rounded-2xl h-14 font-black shadow-lg shadow-indigo-200 active:scale-[0.98] transition-all"
									:loading="submitting"
									type="submit"
								>
									{{ __("Send Message") }}
								</Button>
							</form>
						</div>

						<!-- Direct Support -->
						<div class="grid grid-cols-2 gap-4">
							<a href="tel:+123456789" class="bg-white rounded-2xl p-4 border border-gray-100 shadow-sm flex flex-col items-center text-center gap-2 active:bg-gray-50 transition-colors">
								<div class="w-10 h-10 rounded-xl bg-green-50 flex items-center justify-center text-green-600">
									<Phone class="w-5 h-5" />
								</div>
								<span class="text-xs font-black text-gray-900">{{ __("Call Us") }}</span>
							</a>
							<a href="mailto:support@example.com" class="bg-white rounded-2xl p-4 border border-gray-100 shadow-sm flex flex-col items-center text-center gap-2 active:bg-gray-50 transition-colors">
								<div class="w-10 h-10 rounded-xl bg-blue-50 flex items-center justify-center text-blue-600">
									<Mail class="w-5 h-5" />
								</div>
								<span class="text-xs font-black text-gray-900">{{ __("Email Us") }}</span>
							</a>
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
import { MessageCircle, Tag, Phone, Mail } from "lucide-vue-next"
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import { showSuccessAlert } from "@/utils/dialogs"

const __ = inject("$translate")
const router = useRouter()
const submitting = ref(false)

const form = ref({
	subject: "",
	message: "",
})

const submitContact = async () => {
	if (!form.value.subject || !form.value.message) return
	
	submitting.value = true
	// Mock API call
	setTimeout(() => {
		submitting.value = false
		showSuccessAlert(__("Message sent successfully! Our support team will get back to you shortly."))
		router.push("/contact-list")
	}, 1500)
}
</script>
