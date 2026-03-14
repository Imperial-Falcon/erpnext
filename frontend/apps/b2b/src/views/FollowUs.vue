<template>
	<BaseLayout :pageTitle="__('Follow Us')">
		<template #body>
			<div class="flex flex-col h-full bg-gray-50 overflow-hidden">
				<ion-content>
					<div class="p-6 pb-24 text-center">
						<div class="mb-10 pt-4">
							<div class="w-24 h-24 bg-white rounded-[2.5rem] shadow-xl shadow-gray-200/50 border border-gray-50 flex items-center justify-center mx-auto mb-6">
								<Share2 class="w-10 h-10 text-indigo-600" />
							</div>
							<h2 class="text-2xl font-black text-gray-900 mb-2">{{ __("Connect with us") }}</h2>
							<p class="text-gray-500 text-sm px-10">
								{{ __("Follow us on social media for latest updates, offers and health tips.") }}
							</p>
						</div>

						<div class="grid grid-cols-1 gap-4 px-2">
							<a 
								v-for="social in socials" 
								:key="social.name"
								:href="social.url"
								target="_blank"
								class="bg-white rounded-3xl p-5 border border-gray-100 shadow-sm flex items-center justify-between active:scale-[0.98] transition-all group"
							>
								<div class="flex items-center gap-4">
									<div class="w-12 h-12 rounded-2xl flex items-center justify-center shadow-inner" :class="social.bg">
										<component :is="social.icon" class="w-6 h-6" :class="social.color" />
									</div>
									<div class="text-left">
										<h3 class="font-black text-gray-900 leading-none mb-1">{{ social.name }}</h3>
										<p class="text-[10px] font-black text-gray-400 uppercase tracking-widest">{{ social.handle }}</p>
									</div>
								</div>
								<div class="w-10 h-10 rounded-xl bg-gray-50 flex items-center justify-center text-gray-300 group-hover:text-indigo-600 group-hover:bg-indigo-50 transition-colors">
									<ExternalLink class="w-5 h-5" />
								</div>
							</a>
						</div>

						<!-- App Rating -->
						<div class="mt-12 p-8 bg-gradient-to-br from-indigo-600 to-purple-700 rounded-[2.5rem] text-white shadow-xl shadow-indigo-200 relative overflow-hidden text-center">
							<div class="absolute -top-10 -right-10 w-32 h-32 bg-white/10 rounded-full blur-2xl"></div>
							<div class="relative z-10">
								<div class="flex justify-center gap-1 mb-4">
									<Star v-for="i in 5" :key="i" class="w-6 h-6 fill-yellow-400 text-yellow-400" />
								</div>
								<h3 class="text-lg font-black mb-1">{{ __("Love using our app?") }}</h3>
								<p class="text-indigo-100 text-xs mb-6 px-4 leading-relaxed">{{ __("Your feedback helps us improve and serve you better.") }}</p>
								<button class="w-full py-4 bg-white text-indigo-600 font-black rounded-2xl text-sm active:scale-95 transition-all shadow-lg">
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
import { 
	Share2, Facebook, Twitter, Instagram, 
	Linkedin, Youtube, ExternalLink, Star 
} from "lucide-vue-next"
import BaseLayout from "@/components/layouts/BaseLayout.vue"

const __ = inject("$translate")

const socials = [
	{
		name: "Facebook",
		handle: "@healthyliving",
		url: "https://facebook.com",
		icon: Facebook,
		bg: "bg-blue-50",
		color: "text-blue-600"
	},
	{
		name: "Instagram",
		handle: "@healthy_living_app",
		url: "https://instagram.com",
		icon: Instagram,
		bg: "bg-pink-50",
		color: "text-pink-600"
	},
	{
		name: "Twitter",
		handle: "@healthyliving",
		url: "https://twitter.com",
		icon: Twitter,
		bg: "bg-sky-50",
		color: "text-sky-600"
	},
	{
		name: "LinkedIn",
		handle: "healthy-living-b2b",
		url: "https://linkedin.com",
		icon: Linkedin,
		bg: "bg-indigo-50",
		color: "text-indigo-700"
	},
	{
		name: "YouTube",
		handle: "Healthy Living Channel",
		url: "https://youtube.com",
		icon: Youtube,
		bg: "bg-red-50",
		color: "text-red-600"
	}
]
</script>
