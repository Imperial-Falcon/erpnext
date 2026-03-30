<template>
	<BaseLayout :pageTitle="__('Settings')" :showHeader="false">
		<template #body>
			<div class="flex flex-col h-full overflow-hidden relative" style="background: var(--app-bg);">
				<AppHeader :title="__('Settings')" :showBack="true" :isScrolled="true" />

				<!-- Ambient Backdrops -->
				<div class="absolute inset-0 overflow-hidden pointer-events-none z-0">
					<div class="absolute top-[20%] left-[-50px] w-[300px] h-[300px] bg-brand-primary/10 blur-[80px] rounded-full"></div>
					<div class="absolute bottom-[30%] right-[-50px] w-[250px] h-[250px] bg-brand-secondary/15 blur-[80px] rounded-full"></div>
				</div>

				<ion-content class="transparent-content">
					<div class="p-5 pb-24 space-y-6 relative z-10">
						<!-- Account Section -->
						<section class="animate-fade-in-up">
							<h3 class="px-2 text-[10px] font-black text-gray-400 uppercase tracking-[0.2em] mb-3">{{ __("Account Settings") }}</h3>
							<div class="app-card rounded-[1.5rem] shadow-glass border border-white/40 overflow-hidden">
								<div
									@click="$router.push('/profile')"
									class="flex items-center justify-between p-4 border-b border-gray-100 dark:border-gray-800 active:bg-gray-50/50 dark:active:bg-gray-800/50 transition-colors cursor-pointer"
								>
									<div class="flex items-center gap-4">
										<div class="w-10 h-10 rounded-2xl flex items-center justify-center bg-violet-500/10 text-violet-600">
											<User class="w-5 h-5" />
										</div>
										<span class="text-sm font-bold text-gray-900 dark:text-gray-100">{{ __("Profile Information") }}</span>
									</div>
									<ChevronRight class="w-5 h-5 text-gray-300 dark:text-gray-600" />
								</div>
								<div
									@click="$router.push('/change-password')"
									class="flex items-center justify-between p-4 active:bg-gray-50/50 dark:active:bg-gray-800/50 transition-colors cursor-pointer"
								>
									<div class="flex items-center gap-4">
										<div class="w-10 h-10 rounded-2xl flex items-center justify-center bg-purple-500/10 text-purple-600">
											<Lock class="w-5 h-5" />
										</div>
										<span class="text-sm font-bold text-gray-900 dark:text-gray-100">{{ __("Change Password") }}</span>
									</div>
									<ChevronRight class="w-5 h-5 text-gray-300 dark:text-gray-600" />
								</div>
							</div>
						</section>

						<!-- Preferences Section -->
						<section class="animate-fade-in-up" style="animation-delay: 50ms">
							<h3 class="px-2 text-[10px] font-black text-gray-400 uppercase tracking-[0.2em] mb-3">{{ __("Preferences") }}</h3>
							<div class="app-card rounded-[1.5rem] shadow-glass border border-white/40 overflow-hidden">
								<div class="flex items-center justify-between p-4 border-b border-gray-100 dark:border-gray-800">
									<div class="flex items-center gap-4">
										<div class="w-10 h-10 rounded-2xl flex items-center justify-center bg-orange-500/10 text-orange-500">
											<Bell class="w-5 h-5" />
										</div>
										<div class="flex flex-col">
											<span class="text-sm font-bold text-gray-900 dark:text-gray-100">{{ __("Push Notifications") }}</span>
											<span class="text-[10px] text-gray-400">{{ __("Receive alerts & updates") }}</span>
										</div>
									</div>
									<label class="relative inline-flex items-center cursor-pointer">
										<input type="checkbox" v-model="settings.notifications" class="sr-only peer">
										<div class="w-11 h-6 bg-gray-200 dark:bg-gray-700 rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-brand-primary peer-checked:shadow-neon"></div>
									</label>
								</div>
								<div class="flex items-center justify-between p-4 border-b border-gray-100 dark:border-gray-800 active:bg-gray-50/50 dark:active:bg-gray-800/50 transition-colors cursor-pointer">
									<div class="flex items-center gap-4">
										<div class="w-10 h-10 rounded-2xl flex items-center justify-center bg-sky-500/10 text-sky-600">
											<Globe class="w-5 h-5" />
										</div>
										<div class="flex flex-col">
											<span class="text-sm font-bold text-gray-900 dark:text-gray-100">{{ __("Language") }}</span>
											<span class="text-[10px] text-gray-400">{{ __("Default app language") }}</span>
										</div>
									</div>
									<div class="flex items-center gap-2">
										<span class="text-xs font-black text-brand-primary">{{ settings.language }}</span>
										<ChevronRight class="w-5 h-5 text-gray-300 dark:text-gray-600" />
									</div>
								</div>
								<div class="flex items-center justify-between p-4">
									<div class="flex items-center gap-4">
										<div class="w-10 h-10 rounded-2xl flex items-center justify-center bg-amber-500/10 text-amber-500">
											<Moon v-if="darkMode" class="w-5 h-5" />
											<Sun v-else class="w-5 h-5" />
										</div>
										<div class="flex flex-col">
											<span class="text-sm font-bold text-gray-900 dark:text-gray-100">{{ __("Dark Mode") }}</span>
											<span class="text-[10px] text-gray-400">{{ __("Adjust visual appearance") }}</span>
										</div>
									</div>
									<label class="relative inline-flex items-center cursor-pointer">
										<input type="checkbox" v-model="darkMode" class="sr-only peer">
										<div class="w-11 h-6 bg-gray-200 dark:bg-gray-700 rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-brand-primary peer-checked:shadow-neon"></div>
									</label>
								</div>
							</div>
						</section>

						<!-- More Section -->
						<section class="animate-fade-in-up" style="animation-delay: 100ms">
							<h3 class="px-2 text-[10px] font-black text-gray-400 uppercase tracking-[0.2em] mb-3">{{ __("More") }}</h3>
							<div class="app-card rounded-[1.5rem] shadow-glass border border-white/40 overflow-hidden">
								<div
									v-for="item in moreLinks"
									:key="item.title"
									@click="$router.push(item.route)"
									class="flex items-center justify-between p-4 border-b border-gray-100 dark:border-gray-800 last:border-0 active:bg-gray-50/50 dark:active:bg-gray-800/50 transition-colors cursor-pointer"
								>
									<div class="flex items-center gap-4">
										<div class="w-10 h-10 rounded-2xl flex items-center justify-center bg-gray-100/50 dark:bg-gray-800/50 text-gray-500 dark:text-gray-400">
											<component :is="item.icon" class="w-5 h-5" />
										</div>
										<span class="text-sm font-bold text-gray-900 dark:text-gray-100">{{ item.title }}</span>
									</div>
									<ChevronRight class="w-5 h-5 text-gray-300 dark:text-gray-600" />
								</div>
							</div>
						</section>

						<!-- App Version -->
						<div class="text-center pb-6 animate-fade-in-up" style="animation-delay: 150ms">
							<p class="text-[10px] font-black text-gray-300 dark:text-gray-700 uppercase tracking-widest">Version 2.4.0 (Build 120)</p>
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
import { User, Lock, Bell, Globe, Moon, Sun, ChevronRight, Shield, FileText, HelpCircle, Info, Trophy } from "lucide-vue-next"
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import AppHeader from "@/components/AppHeader.vue"
import { useDarkMode } from "@/utils/theme"

const __ = inject("$translate")
const { darkMode } = useDarkMode()
const settings = ref({ notifications: true, language: "English" })

const moreLinks = [
	{ title: __("Leaderboard"), icon: Trophy, route: "/leaderboard" },
	{ title: __("About Us"), icon: Info, route: "/about" },
	{ title: __("Terms of Service"), icon: FileText, route: "/terms" },
	{ title: __("Help Center"), icon: HelpCircle, route: "/contact" },
	{ title: __("Privacy Policy"), icon: Shield, route: "/privacy" }
]
</script>

<style scoped>
.transparent-content { --background: transparent; }
</style>
