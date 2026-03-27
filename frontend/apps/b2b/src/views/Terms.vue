<template>
	<BaseLayout :pageTitle="__('Terms & Conditions')" :showHeader="false">
		<template #body>
			<div class="flex flex-col h-full bg-gray-50 dark:bg-black overflow-hidden relative">
				<AppHeader :title="__('Terms & Conditions')" :showBack="true" :isScrolled="true" />

				<div class="absolute inset-0 overflow-hidden pointer-events-none z-0">
					<div class="absolute top-[20%] left-[-50px] w-[300px] h-[300px] bg-brand-primary/10 blur-[80px] rounded-full"></div>
					<div class="absolute bottom-[30%] right-[-50px] w-[250px] h-[250px] bg-brand-secondary/15 blur-[80px] rounded-full"></div>
				</div>

				<ion-content class="transparent-content">
					<div class="p-5 pb-24 relative z-10">
						<div class="app-card rounded-[1.75rem] p-6 shadow-glass border border-white/40 mb-6 relative overflow-hidden animate-fade-in-up">
							<div class="flex items-center gap-3 mb-8">
								<div class="w-12 h-12 rounded-2xl bg-brand-primary/10 flex items-center justify-center"><FileText class="w-6 h-6 text-brand-primary" /></div>
								<div>
									<h2 class="text-xl font-black text-gray-900 dark:text-gray-100">{{ __("Legal Agreement") }}</h2>
									<p class="text-[10px] font-black text-gray-400 uppercase tracking-widest">{{ __("Last Updated: Jan 2024") }}</p>
								</div>
							</div>

							<div class="space-y-8">
								<section v-for="(section, index) in termsSections" :key="index">
									<h3 class="text-sm font-black text-gray-900 dark:text-gray-100 mb-3 flex items-center gap-2">
										<span class="w-6 h-6 rounded-lg bg-brand-primary/10 flex items-center justify-center text-[10px] font-black text-brand-primary">{{ index + 1 }}</span>
										{{ section.title }}
									</h3>
									<p class="text-xs text-gray-500 dark:text-gray-400 leading-relaxed pl-8">{{ section.content }}</p>
								</section>
							</div>
						</div>

						<div class="app-card rounded-[1.5rem] p-6 border border-amber-500/20 shadow-[0_0_15px_rgba(245,158,11,0.08)] flex gap-4 animate-fade-in-up" style="animation-delay: 50ms">
							<AlertCircle class="w-6 h-6 text-amber-500 shrink-0" />
							<div>
								<h4 class="text-sm font-black text-gray-900 dark:text-gray-100 mb-1">{{ __("Important Notice") }}</h4>
								<p class="text-[11px] text-gray-500 dark:text-gray-400 leading-relaxed">{{ __("By using this application, you acknowledge that you have read, understood, and agree to be bound by these terms.") }}</p>
							</div>
						</div>
					</div>
				</ion-content>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { inject } from "vue"
import { IonContent } from "@ionic/vue"
import { FileText, AlertCircle } from "lucide-vue-next"
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import AppHeader from "@/components/AppHeader.vue"

const __ = inject("$translate")
const termsSections = [
	{ title: __("Acceptance of Terms"), content: __("By accessing and using this application, you accept and agree to be bound by the terms and provision of this agreement.") },
	{ title: __("Use License"), content: __("Permission is granted to temporarily download one copy of the materials on Healthy Living's application for personal, non-commercial transitory viewing only.") },
	{ title: __("Privacy Policy"), content: __("Your use of the application is also subject to our Privacy Policy. Please review our Privacy Policy, which also governs the application and informs users of our data collection practices.") },
	{ title: __("Disclaimer"), content: __("The materials on Healthy Living's application are provided on an 'as is' basis. Healthy Living makes no warranties, expressed or implied.") },
	{ title: __("Account Responsibilities"), content: __("If you use this site, you are responsible for maintaining the confidentiality of your account and password and for restricting access to your computer.") }
]
</script>

<style scoped>
.transparent-content { --background: transparent; }
</style>
