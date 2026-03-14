<template>
	<BaseLayout :pageTitle="__('About Us')">
		<template #body>
			<div class="flex flex-col h-full bg-gray-50 overflow-hidden">
				<ion-content>
					<div class="p-6 pb-24">
						<div class="bg-white rounded-[2rem] p-8 shadow-xl shadow-gray-200/50 border border-gray-100 mb-8 text-center relative overflow-hidden">
							<div class="absolute -top-10 -right-10 w-32 h-32 bg-indigo-50 rounded-full blur-3xl"></div>
							<div class="absolute -bottom-10 -left-10 w-32 h-32 bg-purple-50 rounded-full blur-3xl"></div>
							
							<div class="w-20 h-20 bg-indigo-600 rounded-[2.5rem] flex items-center justify-center mx-auto mb-6 shadow-lg shadow-indigo-200 relative z-10">
								<HeartPulse class="w-10 h-10 text-white" />
							</div>
							
							<h1 class="text-3xl font-black text-gray-900 mb-2 relative z-10">Healthy Living</h1>
							<p class="text-indigo-600 font-bold uppercase tracking-widest text-xs mb-8 relative z-10">{{ __("Your Health, Our Priority") }}</p>
							
							<div class="text-gray-500 text-sm leading-relaxed space-y-4 text-left relative z-10">
								<p>
									{{ __("Welcome to Healthy Living, your premier B2B partner for all your pharmaceutical and healthcare needs. We are dedicated to providing the highest quality medicines and wellness products to pharmacies, clinics, and hospitals worldwide.") }}
								</p>
								<p>
									{{ __("Our mission is to bridge the gap between healthcare providers and essential medical supplies through innovative technology and a robust supply chain.") }}
								</p>
							</div>
						</div>

						<!-- Stats -->
						<div class="grid grid-cols-2 gap-4 mb-8">
							<div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm text-center">
								<div class="text-2xl font-black text-gray-900 mb-1">10k+</div>
								<div class="text-[10px] font-black text-gray-400 uppercase tracking-widest">{{ __("Products") }}</div>
							</div>
							<div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm text-center">
								<div class="text-2xl font-black text-gray-900 mb-1">500+</div>
								<div class="text-[10px] font-black text-gray-400 uppercase tracking-widest">{{ __("Partners") }}</div>
							</div>
						</div>

						<!-- Mission/Values -->
						<div class="space-y-4 mb-8">
							<h3 class="px-2 text-[10px] font-black text-gray-400 uppercase tracking-[0.2em] mb-3">{{ __("Our Core Values") }}</h3>
							
							<div v-for="value in values" :key="value.title" class="bg-white rounded-2xl p-5 border border-gray-100 shadow-sm flex items-start gap-4 active:scale-[0.98] transition-all">
								<div class="w-12 h-12 rounded-xl flex items-center justify-center shrink-0 shadow-sm" :class="value.color">
									<component :is="value.icon" class="w-6 h-6" />
								</div>
								<div>
									<h4 class="font-black text-gray-900 mb-1">{{ value.title }}</h4>
									<p class="text-xs text-gray-500 leading-relaxed">{{ value.description }}</p>
								</div>
							</div>
						</div>

						<!-- Contact Banner -->
						<div class="bg-indigo-600 rounded-2xl p-6 text-white shadow-xl shadow-indigo-200 flex flex-col items-center text-center">
							<h3 class="text-lg font-black mb-2">{{ __("Have questions?") }}</h3>
							<p class="text-xs text-indigo-100 mb-6">{{ __("Our support team is here to help you 24/7.") }}</p>
							<button 
								@click="$router.push('/contact')"
								class="px-8 py-3 bg-white text-indigo-600 font-black rounded-xl text-sm active:scale-95 transition-all"
							>
								{{ __("Contact Us") }}
							</button>
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
import { HeartPulse, ShieldCheck, Zap, Users } from "lucide-vue-next"
import BaseLayout from "@/components/layouts/BaseLayout.vue"

const __ = inject("$translate")

const values = [
	{
		title: __("Trust & Integrity"),
		description: __("We uphold the highest standards of ethics and professionalism in all our dealings."),
		icon: ShieldCheck,
		color: "bg-blue-50 text-blue-600"
	},
	{
		title: __("Innovation"),
		description: __("Leveraging technology to make healthcare more accessible and efficient."),
		icon: Zap,
		color: "bg-amber-50 text-amber-600"
	},
	{
		title: __("Customer Success"),
		description: __("Our partners' growth and satisfaction are at the heart of everything we do."),
		icon: Users,
		color: "bg-indigo-50 text-indigo-600"
	}
]
</script>
