<template>
	<BaseLayout :pageTitle="__('Terms & Conditions')">
		<template #body>
			<div class="flex flex-col h-full bg-gray-50 overflow-hidden">
				<ion-content>
					<div class="p-6 pb-24">
						<div class="bg-white rounded-3xl p-6 shadow-xl shadow-gray-200/50 border border-gray-100 mb-6 relative overflow-hidden">
							<div class="flex items-center gap-3 mb-8">
								<div class="w-12 h-12 rounded-2xl bg-indigo-50 flex items-center justify-center text-indigo-600">
									<FileText class="w-6 h-6" />
								</div>
								<div>
									<h2 class="text-xl font-black text-gray-900">{{ __("Legal Agreement") }}</h2>
									<p class="text-[10px] font-black text-gray-400 uppercase tracking-widest">{{ __("Last Updated: Jan 2024") }}</p>
								</div>
							</div>

							<div class="space-y-8">
								<section v-for="(section, index) in termsSections" :key="index">
									<h3 class="text-sm font-black text-gray-900 mb-3 flex items-center gap-2">
										<span class="w-6 h-6 rounded-lg bg-gray-100 flex items-center justify-center text-[10px]">{{ index + 1 }}</span>
										{{ section.title }}
									</h3>
									<p class="text-xs text-gray-500 leading-relaxed pl-8">
										{{ section.content }}
									</p>
								</section>
							</div>
						</div>

						<div class="bg-amber-50 rounded-2xl p-6 border border-amber-100 flex gap-4">
							<AlertCircle class="w-6 h-6 text-amber-600 shrink-0" />
							<div>
								<h4 class="text-sm font-black text-amber-900 mb-1">{{ __("Important Notice") }}</h4>
								<p class="text-[11px] text-amber-700 leading-relaxed">
									{{ __("By using this application, you acknowledge that you have read, understood, and agree to be bound by these terms.") }}
								</p>
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

const __ = inject("$translate")

const termsSections = [
	{
		title: __("Acceptance of Terms"),
		content: __("By accessing and using this application, you accept and agree to be bound by the terms and provision of this agreement. In addition, when using these particular services, you shall be subject to any posted guidelines or rules applicable to such services.")
	},
	{
		title: __("Use License"),
		content: __("Permission is granted to temporarily download one copy of the materials (information or software) on Healthy Living's application for personal, non-commercial transitory viewing only.")
	},
	{
		title: __("Privacy Policy"),
		content: __("Your use of the application is also subject to our Privacy Policy. Please review our Privacy Policy, which also governs the application and informs users of our data collection practices.")
	},
	{
		title: __("Disclaimer"),
		content: __("The materials on Healthy Living's application are provided on an 'as is' basis. Healthy Living makes no warranties, expressed or implied, and hereby disclaims and negates all other warranties including, without limitation, implied warranties or conditions of merchantability.")
	},
	{
		title: __("Account Responsibilities"),
		content: __("If you use this site, you are responsible for maintaining the confidentiality of your account and password and for restricting access to your computer, and you agree to accept responsibility for all activities that occur under your account or password.")
	}
]
</script>
