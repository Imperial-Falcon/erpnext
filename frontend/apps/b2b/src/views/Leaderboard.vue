<template>
	<BaseLayout :pageTitle="__('Leaderboard')" :showHeader="false">
		<template #body>
			<div class="flex flex-col h-full bg-gray-50 dark:bg-black overflow-hidden relative">
				<AppHeader :title="__('Leaderboard')" :showBack="true" :isScrolled="false" customClass="bg-white/70 dark:bg-black/70 backdrop-blur-xl shadow-glass z-50 animate-fade-in-up border-b border-white/20" />

				<!-- Ambient Backdrops -->
				<div class="absolute inset-0 overflow-hidden pointer-events-none z-0">
					<div class="absolute top-[10%] left-[-50px] w-[300px] h-[300px] bg-brand-primary/10 blur-[80px] rounded-full"></div>
					<div class="absolute bottom-[30%] right-[-50px] w-[250px] h-[250px] bg-brand-secondary/15 blur-[80px] rounded-full"></div>
				</div>

				<!-- Tab Switcher -->
				<div class="px-5 pt-4 pb-2 relative z-10 animate-fade-in-up">
					<div class="app-card p-1.5 rounded-[1.2rem] shadow-glass flex border border-white/40">
						<button 
							@click="activeTab = 'regional'"
							class="flex-1 py-2.5 text-xs font-black rounded-xl transition-all"
							:class="activeTab === 'regional' ? 'bg-gradient-to-r from-brand-primary to-brand-secondary text-white shadow-neon' : 'text-gray-500 hover:text-brand-primary'"
						>
							{{ __("Regional") }}
						</button>
						<button 
							@click="activeTab = 'national'"
							class="flex-1 py-2.5 text-xs font-black rounded-xl transition-all"
							:class="activeTab === 'national' ? 'bg-gradient-to-r from-brand-primary to-brand-secondary text-white shadow-neon' : 'text-gray-500 hover:text-brand-primary'"
						>
							{{ __("National") }}
						</button>
					</div>
				</div>

				<ion-content class="transparent-content">
					<div class="pb-[120px]">
						<!-- Top 3 Podium -->
						<div class="px-5 pt-4 pb-12 flex items-end justify-center gap-3 h-[320px] relative animate-fade-in-up z-10">

							<!-- Rank 2 -->
							<div v-if="topThree[1]" class="flex flex-col items-center flex-1 max-w-[100px] animate-fade-in-up" style="animation-delay: 100ms">
								<div class="relative mb-3 group">
									<img :src="topThree[1].avatar" class="w-16 h-16 rounded-[1.2rem] border-2 border-white/50 shadow-glass object-cover group-hover:scale-105 transition-transform" />
									<div class="absolute -bottom-2 -right-2 w-8 h-8 bg-slate-100 dark:bg-slate-800 rounded-lg flex items-center justify-center border font-black text-slate-500 shadow-sm">
										<span class="text-xs">2</span>
									</div>
								</div>
								<span class="text-[10px] font-black text-gray-900 dark:text-gray-100 truncate w-full text-center">{{ topThree[1].name }}</span>
								<span class="text-[10px] font-bold text-brand-primary">{{ topThree[1].points }} pts</span>
								<div class="w-full h-20 app-card border-none bg-white/40 dark:bg-gray-800/40 rounded-t-[2rem] mt-4 shadow-glass flex items-center justify-center backdrop-blur-md">
									<Trophy class="w-6 h-6 text-slate-400" />
								</div>
							</div>

							<!-- Rank 1 -->
							<div v-if="topThree[0]" class="flex flex-col items-center flex-1 max-w-[120px] z-20 animate-fade-in-up">
								<div class="relative mb-4 scale-110 group">
									<Crown class="absolute -top-7 left-1/2 -translate-x-1/2 w-8 h-8 text-yellow-400 drop-shadow-md animate-bounce" />
									<img :src="topThree[0].avatar" class="w-20 h-20 rounded-[1.5rem] border-2 border-white/50 shadow-[0_0_20px_rgba(250,204,21,0.3)] object-cover ring-2 ring-yellow-400/50 group-hover:scale-105 transition-transform" />
									<div class="absolute -bottom-3 -right-2 w-10 h-10 bg-gradient-to-tr from-yellow-400 to-amber-500 rounded-xl flex items-center justify-center border-2 border-white shadow-md text-white">
										<span class="text-sm font-black">1</span>
									</div>
								</div>
								<span class="text-xs font-black text-gray-900 dark:text-gray-100 truncate w-full text-center mb-0.5">{{ topThree[0].name }}</span>
								<span class="text-[11px] font-black bg-clip-text text-transparent bg-gradient-to-r from-brand-primary to-brand-secondary">{{ topThree[0].points }} pts</span>
								<div class="w-full h-28 app-card border-none bg-white/60 dark:bg-gray-800/60 rounded-t-[2rem] mt-4 shadow-glass flex items-center justify-center backdrop-blur-md border border-white/20">
									<Trophy class="w-8 h-8 text-yellow-500" />
								</div>
							</div>

							<!-- Rank 3 -->
							<div v-if="topThree[2]" class="flex flex-col items-center flex-1 max-w-[100px] animate-fade-in-up" style="animation-delay: 200ms">
								<div class="relative mb-3 group">
									<img :src="topThree[2].avatar" class="w-16 h-16 rounded-[1.2rem] border-2 border-white/50 shadow-glass object-cover group-hover:scale-105 transition-transform" />
									<div class="absolute -bottom-2 -right-2 w-8 h-8 bg-amber-100 dark:bg-amber-900/40 rounded-lg flex items-center justify-center border font-black text-amber-600 shadow-sm">
										<span class="text-xs">3</span>
									</div>
								</div>
								<span class="text-[10px] font-black text-gray-900 dark:text-gray-100 truncate w-full text-center">{{ topThree[2].name }}</span>
								<span class="text-[10px] font-bold text-brand-primary">{{ topThree[2].points }} pts</span>
								<div class="w-full h-16 app-card border-none bg-white/40 dark:bg-gray-800/40 rounded-t-[2rem] mt-4 shadow-glass flex items-center justify-center backdrop-blur-md">
									<Trophy class="w-5 h-5 text-amber-600/50" />
								</div>
							</div>
						</div>

						<!-- List of other users -->
						<div class="px-5 space-y-3 mt-4 relative z-10">
							<div 
								v-for="(user, index) in remainingUsers" 
								:key="user.id"
								class="app-card rounded-[1.2rem] p-3 shadow-glass flex items-center gap-4 animate-fade-in border border-white/40"
								:style="`animation-delay: ${index * 50}ms`"
							>
								<span class="w-6 text-xs font-black text-gray-400 pl-2">{{ index + 4 }}</span>
								<img :src="user.avatar" class="w-10 h-10 rounded-xl object-cover shadow-sm" />
								<div class="flex-1">
									<h4 class="text-sm font-black text-gray-900 dark:text-gray-100 leading-none mb-1">{{ user.name }}</h4>
									<p class="text-[10px] font-bold text-gray-500 uppercase tracking-widest">{{ user.region }}</p>
								</div>
								<div class="text-right pr-2">
									<span class="text-sm font-black text-brand-primary block leading-none">{{ user.points }}</span>
									<span class="text-[9px] font-bold text-gray-400 uppercase tracking-tighter">points</span>
								</div>
							</div>
						</div>
					</div>
				</ion-content>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { ref, computed, inject } from "vue"
import { IonContent } from "@ionic/vue"
import { Trophy, Crown } from "lucide-vue-next"
import BaseLayout from "@/components/layouts/BaseLayout.vue"
import AppHeader from "@/components/AppHeader.vue"

const __ = inject("$translate")

const activeTab = ref('regional')

const mockData = {
	regional: [
		{ id: 1, name: "City Pharmacy", points: 2450, avatar: "https://i.pravatar.cc/150?u=1", region: "North District" },
		{ id: 2, name: "Wellness Center", points: 2120, avatar: "https://i.pravatar.cc/150?u=2", region: "South District" },
		{ id: 3, name: "Health First", points: 1980, avatar: "https://i.pravatar.cc/150?u=3", region: "East District" },
		{ id: 4, name: "MediCare Plus", points: 1850, avatar: "https://i.pravatar.cc/150?u=4", region: "West District" },
		{ id: 5, name: "Green Cross", points: 1720, avatar: "https://i.pravatar.cc/150?u=5", region: "Central" },
		{ id: 6, name: "Life Line", points: 1600, avatar: "https://i.pravatar.cc/150?u=6", region: "North District" },
		{ id: 7, name: "Family Health", points: 1450, avatar: "https://i.pravatar.cc/150?u=7", region: "South District" },
	],
	national: [
		{ id: 10, name: "Global Pharma", points: 12450, avatar: "https://i.pravatar.cc/150?u=10", region: "Metropolis" },
		{ id: 11, name: "National Health", points: 11120, avatar: "https://i.pravatar.cc/150?u=11", region: "Capital City" },
		{ id: 12, name: "Apex Medical", points: 9980, avatar: "https://i.pravatar.cc/150?u=12", region: "Industrial Zone" },
		{ id: 13, name: "Elite Wellness", points: 8850, avatar: "https://i.pravatar.cc/150?u=13", region: "Metropolis" },
		{ id: 14, name: "United Care", points: 7720, avatar: "https://i.pravatar.cc/150?u=14", region: "Capital City" },
	]
}

const currentList = computed(() => mockData[activeTab.value])
const topThree = computed(() => currentList.value.slice(0, 3))
const remainingUsers = computed(() => currentList.value.slice(3))
</script>

<style scoped>
@keyframes fadeInUp {
	from {
		opacity: 0;
		transform: translateY(20px);
	}
	to {
		opacity: 1;
		transform: translateY(0);
	}
}

@keyframes fadeIn {
	from { opacity: 0; }
	to { opacity: 1; }
}

.animate-fade-in-up {
	animation: fadeInUp 0.6s cubic-bezier(0.16, 1, 0.3, 1) both;
}

.animate-fade-in {
	animation: fadeIn 0.4s ease-out both;
}

.transparent-content {
	--background: transparent;
}
</style>
