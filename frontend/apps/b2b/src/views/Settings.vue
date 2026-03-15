<template>
	<BaseLayout :pageTitle="__('Settings')">
		<template #body>
			<div class="flex flex-col h-full bg-gray-50 dark:bg-black overflow-hidden">
				<ion-content>
					<div class="p-6 pb-24 space-y-8">
						<!-- Account Section -->
						<section>
							<h3 class="px-4 text-[10px] font-black text-gray-400 uppercase tracking-[0.2em] mb-3">{{ __("Account Settings") }}</h3>
							<div class="bg-white dark:bg-gray-900 rounded-3xl shadow-sm border border-gray-100 dark:border-gray-800 overflow-hidden">
								<div 
									@click="$router.push('/profile')"
									class="flex items-center justify-between p-4 border-b border-gray-50 dark:border-gray-800 active:bg-gray-50 dark:active:bg-gray-800 transition-colors cursor-pointer"
								>
									<div class="flex items-center gap-4">
										<div class="w-10 h-10 rounded-2xl flex items-center justify-center bg-indigo-50 dark:bg-indigo-900/30 text-indigo-600 dark:text-indigo-400">
											<User class="w-5 h-5" />
										</div>
										<span class="text-sm font-bold text-gray-900 dark:text-gray-100">{{ __("Profile Information") }}</span>
									</div>
									<ChevronRight class="w-5 h-5 text-gray-300 dark:text-gray-700" />
								</div>
								<div 
									@click="$router.push('/change-password')"
									class="flex items-center justify-between p-4 active:bg-gray-50 dark:active:bg-gray-800 transition-colors cursor-pointer"
								>
									<div class="flex items-center gap-4">
										<div class="w-10 h-10 rounded-2xl flex items-center justify-center bg-purple-50 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400">
											<Lock class="w-5 h-5" />
										</div>
										<span class="text-sm font-bold text-gray-900 dark:text-gray-100">{{ __("Change Password") }}</span>
									</div>
									<ChevronRight class="w-5 h-5 text-gray-300 dark:text-gray-700" />
								</div>
							</div>
						</section>

						<!-- Preferences Section -->
						<section>
							<h3 class="px-4 text-[10px] font-black text-gray-400 uppercase tracking-[0.2em] mb-3">{{ __("Preferences") }}</h3>
							<div class="bg-white dark:bg-gray-900 rounded-3xl shadow-sm border border-gray-100 dark:border-gray-800 overflow-hidden">
								<!-- Notifications Toggle -->
								<div class="flex items-center justify-between p-4 border-b border-gray-50 dark:border-gray-800">
									<div class="flex items-center gap-4">
										<div class="w-10 h-10 rounded-2xl flex items-center justify-center bg-orange-50 dark:bg-orange-900/30 text-orange-600 dark:text-orange-400">
											<Bell class="w-5 h-5" />
										</div>
										<div class="flex flex-col">
											<span class="text-sm font-bold text-gray-900 dark:text-gray-100">{{ __("Push Notifications") }}</span>
											<span class="text-[10px] text-gray-400">{{ __("Receive alerts & updates") }}</span>
										</div>
									</div>
									<label class="relative inline-flex items-center cursor-pointer">
										<input type="checkbox" v-model="settings.notifications" class="sr-only peer">
										<div class="w-11 h-6 bg-gray-200 dark:bg-gray-700 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-indigo-600"></div>
									</label>
								</div>

								<!-- Language Selection -->
								<div class="flex items-center justify-between p-4 border-b border-gray-50 dark:border-gray-800 active:bg-gray-50 dark:active:bg-gray-800 transition-colors cursor-pointer">
									<div class="flex items-center gap-4">
										<div class="w-10 h-10 rounded-2xl flex items-center justify-center bg-blue-50 dark:bg-blue-900/30 text-blue-600 dark:text-blue-400">
											<Globe class="w-5 h-5" />
										</div>
										<div class="flex flex-col">
											<span class="text-sm font-bold text-gray-900 dark:text-gray-100">{{ __("Language") }}</span>
											<span class="text-[10px] text-gray-400">{{ __("Default app language") }}</span>
										</div>
									</div>
									<div class="flex items-center gap-2">
										<span class="text-xs font-bold text-indigo-600 dark:text-indigo-400">{{ settings.language }}</span>
										<ChevronRight class="w-5 h-5 text-gray-300 dark:text-gray-700" />
									</div>
								</div>

								<!-- Theme Selection -->
								<div class="flex items-center justify-between p-4">
									<div class="flex items-center gap-4">
										<div class="w-10 h-10 rounded-2xl flex items-center justify-center bg-amber-50 dark:bg-amber-900/30 text-amber-600 dark:text-amber-400">
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
										<div class="w-11 h-6 bg-gray-200 dark:bg-gray-700 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-indigo-600"></div>
									</label>
								</div>
							</div>
						</section>

						<!-- More Section -->
						<section>
							<h3 class="px-4 text-[10px] font-black text-gray-400 uppercase tracking-[0.2em] mb-3">{{ __("More") }}</h3>
							<div class="bg-white dark:bg-gray-900 rounded-3xl shadow-sm border border-gray-100 dark:border-gray-800 overflow-hidden">
								<div 
									v-for="item in moreLinks" 
									:key="item.title"
									@click="$router.push(item.route)"
									class="flex items-center justify-between p-4 border-b border-gray-50 dark:border-gray-800 last:border-0 active:bg-gray-50 dark:active:bg-gray-800 transition-colors cursor-pointer"
								>
									<div class="flex items-center gap-4">
										<div class="w-10 h-10 rounded-2xl flex items-center justify-center bg-gray-50 dark:bg-gray-800 text-gray-600 dark:text-gray-400">
											<component :is="item.icon" class="w-5 h-5" />
										</div>
										<span class="text-sm font-bold text-gray-900 dark:text-gray-100">{{ item.title }}</span>
									</div>
									<ChevronRight class="w-5 h-5 text-gray-300 dark:text-gray-700" />
								</div>
							</div>
						</section>

						<!-- App Version -->
						<div class="text-center pb-10">
							<p class="text-[10px] font-black text-gray-300 uppercase tracking-widest">Version 2.4.0 (Build 120)</p>
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
import { 
	User, Lock, Bell, Globe, Moon, Sun, 
	ChevronRight, Shield, FileText, HelpCircle, Info, Trophy 
} from "lucide-vue-next"
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import { useDarkMode } from "@/utils/theme"

const __ = inject("$translate")
const { darkMode } = useDarkMode()

const settings = ref({
	notifications: true,
	language: "English",
})

const moreLinks = [
	{ title: __("Leaderboard"), icon: Trophy, route: "/leaderboard" },
	{ title: __("About Us"), icon: Info, route: "/about" },
	{ title: __("Terms of Service"), icon: FileText, route: "/terms" },
	{ title: __("Help Center"), icon: HelpCircle, route: "/contact" },
	{ title: __("Privacy Policy"), icon: Shield, route: "/privacy" }
]
</script>
