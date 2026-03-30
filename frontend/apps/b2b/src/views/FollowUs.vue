<template>
	<BaseLayout :pageTitle="__('Follow Us')" :showHeader="false">
		<template #body>
			<div class="flex flex-col h-full overflow-hidden relative" style="background: var(--app-bg);">
				<AppHeader :title="__('Follow Us')" :showBack="true" :isScrolled="true" />

				<div class="absolute inset-0 overflow-hidden pointer-events-none z-0">
					<div class="absolute top-[15%] left-[-50px] w-[300px] h-[300px] bg-brand-primary/10 blur-[80px] rounded-full"></div>
					<div class="absolute bottom-[25%] right-[-50px] w-[250px] h-[250px] bg-brand-secondary/15 blur-[80px] rounded-full"></div>
				</div>

				<ion-content class="transparent-content">
					<div class="p-5 pb-24 text-center relative z-10">
						<div class="mb-8 pt-2 animate-fade-in-up">
							<div class="w-20 h-20 app-card rounded-full shadow-glass border border-white/40 flex items-center justify-center mx-auto mb-5">
								<Share2 class="w-9 h-9 text-brand-primary" />
							</div>
							<h2 class="text-2xl font-black text-gray-900 dark:text-gray-100 mb-2">{{ __("Connect with us") }}</h2>
							<p class="text-gray-500 text-sm px-8">{{ __("Follow us on social media for latest updates, offers and health tips.") }}</p>
						</div>

						<div class="grid grid-cols-1 gap-3 px-1">
							<a
								v-for="(social, index) in socials"
								:key="social.name"
								:href="social.url"
								target="_blank"
								class="app-card rounded-[1.5rem] p-5 border border-white/40 shadow-glass flex items-center justify-between active:scale-[0.98] transition-all group animate-fade-in-up"
								:style="`animation-delay: ${index * 50}ms`"
							>
								<div class="flex items-center gap-4">
									<div class="w-12 h-12 rounded-2xl flex items-center justify-center" :class="social.bg">
										<component :is="social.icon" class="w-6 h-6" :class="social.color" />
									</div>
									<div class="text-left">
										<h3 class="font-black text-gray-900 dark:text-gray-100 leading-none mb-1">{{ social.name }}</h3>
										<p class="text-[10px] font-black text-gray-400 uppercase tracking-widest">{{ social.handle }}</p>
									</div>
								</div>
								<div class="w-10 h-10 rounded-xl app-card flex items-center justify-center text-gray-300 dark:text-gray-600 group-hover:text-brand-primary group-hover:shadow-neon transition-all">
									<ExternalLink class="w-5 h-5" />
								</div>
							</a>
						</div>

						<!-- App Rating -->
						<div class="mt-10 p-8 rounded-[1.75rem] text-white shadow-neon relative overflow-hidden text-center bg-gradient-to-br from-brand-primary via-violet-600 to-brand-secondary animate-fade-in-up" style="animation-delay: 300ms">
							<div class="absolute inset-0 bg-[radial-gradient(circle_at_80%_20%,rgba(255,255,255,0.1)_0%,transparent_50%)]"></div>
							<div class="relative z-10">
								<div class="flex justify-center gap-1 mb-4">
									<Star v-for="i in 5" :key="i" class="w-6 h-6 fill-yellow-400 text-yellow-400" />
								</div>
								<h3 class="text-lg font-black mb-1">{{ __("Love using our app?") }}</h3>
								<p class="text-white/70 text-xs mb-6 px-4 leading-relaxed">{{ __("Your feedback helps us improve and serve you better.") }}</p>
								<button class="w-full py-4 bg-white text-brand-primary font-black rounded-[1.2rem] text-sm active:scale-95 transition-all shadow-lg">
									{{ __("Rate us on Store") }}
								</button>
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
import { Share2, Facebook, Twitter, Instagram, Linkedin, Youtube, ExternalLink, Star } from "lucide-vue-next"
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import AppHeader from "@/components/AppHeader.vue"

const __ = inject("$translate")
const socials = [
	{ name: "Facebook", handle: "@healthyliving", url: "https://facebook.com", icon: Facebook, bg: "bg-blue-500/10", color: "text-blue-600" },
	{ name: "Instagram", handle: "@healthy_living_app", url: "https://instagram.com", icon: Instagram, bg: "bg-pink-500/10", color: "text-pink-600" },
	{ name: "Twitter", handle: "@healthyliving", url: "https://twitter.com", icon: Twitter, bg: "bg-sky-500/10", color: "text-sky-500" },
	{ name: "LinkedIn", handle: "healthy-living-b2b", url: "https://linkedin.com", icon: Linkedin, bg: "bg-indigo-500/10", color: "text-indigo-700" },
	{ name: "YouTube", handle: "Healthy Living Channel", url: "https://youtube.com", icon: Youtube, bg: "bg-red-500/10", color: "text-red-600" }
]
</script>

<style scoped>
.transparent-content { --background: transparent; }
</style>
