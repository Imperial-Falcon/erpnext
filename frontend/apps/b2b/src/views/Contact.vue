<template>
	<BaseLayout :pageTitle="__('Contact Support')" :showHeader="false">
		<template #body>
			<div class="flex flex-col h-full overflow-hidden relative" style="background: var(--app-bg);">
				<AppHeader :title="__('Contact Support')" :showBack="true" :isScrolled="true" />

				<div class="absolute inset-0 overflow-hidden pointer-events-none z-0">
					<div class="absolute top-[20%] left-[-50px] w-[300px] h-[300px] bg-brand-primary/10 blur-[80px] rounded-full"></div>
					<div class="absolute bottom-[30%] right-[-50px] w-[250px] h-[250px] bg-brand-secondary/15 blur-[80px] rounded-full"></div>
				</div>

				<ion-content class="transparent-content">
					<div class="p-5 relative z-10">
						<div class="app-card rounded-[1.75rem] p-6 shadow-glass border border-white/40 mb-6 animate-fade-in-up">
							<div class="flex items-center gap-3 mb-6">
								<div class="w-12 h-12 rounded-2xl bg-brand-primary/10 flex items-center justify-center"><MessageCircle class="w-6 h-6 text-brand-primary" /></div>
								<div>
									<h2 class="text-xl font-black text-gray-900 dark:text-gray-100">{{ __("How can we help?") }}</h2>
									<p class="text-[10px] font-black text-gray-400 uppercase tracking-widest">{{ __("Send us a message") }}</p>
								</div>
							</div>
							<form @submit.prevent="submitContact" class="space-y-5">
								<FormControl :label="__('Subject')" v-model="form.subject" :placeholder="__('What is this about?')" required>
									<template #prefix><Tag class="w-4 h-4 text-gray-400 ml-3" /></template>
								</FormControl>
								<FormControl :label="__('Message')" type="textarea" v-model="form.message" :placeholder="__('Describe your issue or question in detail...')" required class="h-48" />
								<button type="submit" :disabled="submitting" class="w-full h-14 bg-gradient-to-tr from-brand-primary to-brand-secondary text-white font-black rounded-[1.2rem] shadow-neon active:scale-[0.98] transition-all disabled:opacity-50">
									{{ submitting ? __("Sending...") : __("Send Message") }}
								</button>
							</form>
						</div>

						<!-- Direct Support -->
						<div class="grid grid-cols-2 gap-4 animate-fade-in-up" style="animation-delay: 50ms">
							<a href="tel:+123456789" class="app-card rounded-[1.5rem] p-5 border border-white/40 shadow-glass flex flex-col items-center text-center gap-3 active:scale-[0.98] transition-all group">
								<div class="w-12 h-12 rounded-xl bg-emerald-500/10 flex items-center justify-center text-emerald-600 group-hover:shadow-neon transition-all">
									<Phone class="w-5 h-5" />
								</div>
								<span class="text-xs font-black text-gray-900 dark:text-gray-100">{{ __("Call Us") }}</span>
							</a>
							<a href="mailto:support@example.com" class="app-card rounded-[1.5rem] p-5 border border-white/40 shadow-glass flex flex-col items-center text-center gap-3 active:scale-[0.98] transition-all group">
								<div class="w-12 h-12 rounded-xl bg-sky-500/10 flex items-center justify-center text-sky-600 group-hover:shadow-neon transition-all">
									<Mail class="w-5 h-5" />
								</div>
								<span class="text-xs font-black text-gray-900 dark:text-gray-100">{{ __("Email Us") }}</span>
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
import AppHeader from "@/components/AppHeader.vue"
import { showSuccessAlert } from "@/utils/dialogs"

const __ = inject("$translate")
const router = useRouter()
const submitting = ref(false)
const form = ref({ subject: "", message: "" })

const submitContact = async () => {
	if (!form.value.subject || !form.value.message) return
	submitting.value = true
	setTimeout(() => {
		submitting.value = false
		showSuccessAlert(__("Message sent successfully! Our support team will get back to you shortly."))
		router.push("/contact-list")
	}, 1500)
}
</script>

<style scoped>
.transparent-content { --background: transparent; }
</style>
