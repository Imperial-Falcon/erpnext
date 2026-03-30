<template>
	<BaseLayout :pageTitle="__('About Us')" :showHeader="false">
		<template #body>
			<div class="flex flex-col h-full overflow-hidden relative" style="background: var(--app-bg);">
				<AppHeader :title="__('About Us')" :showBack="true" :isScrolled="true" />

				<div class="absolute inset-0 overflow-hidden pointer-events-none z-0">
					<div class="absolute top-[15%] left-[-50px] w-[300px] h-[300px] bg-brand-primary/10 blur-[80px] rounded-full"></div>
					<div class="absolute bottom-[25%] right-[-50px] w-[250px] h-[250px] bg-brand-secondary/15 blur-[80px] rounded-full"></div>
				</div>

				<ion-content class="transparent-content">
					<div class="p-5 pb-24 relative z-10">
						<div class="app-card rounded-[1.75rem] p-8 shadow-glass border border-white/40 mb-6 text-center relative overflow-hidden animate-fade-in-up">
							<div class="absolute -top-10 -right-10 w-32 h-32 bg-brand-primary/5 rounded-full blur-3xl"></div>
							<div class="absolute -bottom-10 -left-10 w-32 h-32 bg-brand-secondary/5 rounded-full blur-3xl"></div>

							<div class="w-20 h-20 bg-gradient-to-tr from-brand-primary to-brand-secondary rounded-[2.5rem] flex items-center justify-center mx-auto mb-6 shadow-neon relative z-10">
								<HeartPulse class="w-10 h-10 text-white" />
							</div>
							<h1 class="text-3xl font-black text-gray-900 dark:text-gray-100 mb-2 relative z-10">Healthy Living</h1>
							<p class="font-black uppercase tracking-widest text-xs mb-8 relative z-10 bg-clip-text text-transparent bg-gradient-to-r from-brand-primary to-brand-secondary">{{ __("Your Health, Our Priority") }}</p>
							<div class="text-gray-500 dark:text-gray-400 text-sm leading-relaxed space-y-4 text-left relative z-10">
								<p>{{ __("Welcome to Healthy Living, your premier B2B partner for all your pharmaceutical and healthcare needs. We are dedicated to providing the highest quality medicines and wellness products to pharmacies, clinics, and hospitals worldwide.") }}</p>
								<p>{{ __("Our mission is to bridge the gap between healthcare providers and essential medical supplies through innovative technology and a robust supply chain.") }}</p>
							</div>
						</div>

						<!-- Stats -->
						<div class="grid grid-cols-2 gap-4 mb-6 animate-fade-in-up" style="animation-delay: 50ms">
							<div class="app-card rounded-[1.5rem] p-6 border border-white/40 shadow-glass text-center">
								<div class="text-2xl font-black bg-clip-text text-transparent bg-gradient-to-r from-brand-primary to-brand-secondary mb-1">10k+</div>
								<div class="text-[10px] font-black text-gray-400 uppercase tracking-widest">{{ __("Products") }}</div>
							</div>
							<div class="app-card rounded-[1.5rem] p-6 border border-white/40 shadow-glass text-center">
								<div class="text-2xl font-black bg-clip-text text-transparent bg-gradient-to-r from-brand-primary to-brand-secondary mb-1">500+</div>
								<div class="text-[10px] font-black text-gray-400 uppercase tracking-widest">{{ __("Partners") }}</div>
							</div>
						</div>

						<!-- Core Values -->
						<div class="space-y-3 mb-6 animate-fade-in-up" style="animation-delay: 100ms">
							<h3 class="px-2 text-[10px] font-black text-gray-400 uppercase tracking-[0.2em] mb-3">{{ __("Our Core Values") }}</h3>
							<div v-for="(value, index) in values" :key="value.title" class="app-card rounded-[1.5rem] p-5 border border-white/40 shadow-glass flex items-start gap-4 active:scale-[0.98] transition-all" :style="`animation-delay: ${100 + index * 50}ms`">
								<div class="w-12 h-12 rounded-xl flex items-center justify-center shrink-0" :class="value.color">
									<component :is="value.icon" class="w-6 h-6" />
								</div>
								<div>
									<h4 class="font-black text-gray-900 dark:text-gray-100 mb-1">{{ value.title }}</h4>
									<p class="text-xs text-gray-500 dark:text-gray-400 leading-relaxed">{{ value.description }}</p>
								</div>
							</div>
						</div>

						<!-- Contact Banner -->
						<div class="rounded-[1.75rem] p-6 text-white shadow-neon flex flex-col items-center text-center relative overflow-hidden bg-gradient-to-br from-brand-primary via-violet-600 to-brand-secondary animate-fade-in-up" style="animation-delay: 200ms">
							<div class="absolute inset-0 bg-[radial-gradient(circle_at_80%_20%,rgba(255,255,255,0.1)_0%,transparent_50%)]"></div>
							<h3 class="relative text-lg font-black mb-2">{{ __("Have questions?") }}</h3>
							<p class="relative text-xs text-white/80 mb-6">{{ __("Our support team is here to help you 24/7.") }}</p>
							<button @click="$router.push('/contact')" class="relative px-8 py-3 bg-white text-brand-primary font-black rounded-xl text-sm active:scale-95 transition-all shadow-lg">
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
import AppHeader from "@/components/AppHeader.vue"

const __ = inject("$translate")
const values = [
	{ title: __("Trust & Integrity"), description: __("We uphold the highest standards of ethics and professionalism in all our dealings."), icon: ShieldCheck, color: "bg-sky-500/10 text-sky-600" },
	{ title: __("Innovation"), description: __("Leveraging technology to make healthcare more accessible and efficient."), icon: Zap, color: "bg-amber-500/10 text-amber-500" },
	{ title: __("Customer Success"), description: __("Our partners' growth and satisfaction are at the heart of everything we do."), icon: Users, color: "bg-brand-primary/10 text-brand-primary" }
]
</script>

<style scoped>
.transparent-content { --background: transparent; }
</style>
