<template>
	<BaseLayout :pageTitle="__('Leaderboard')">
		<template #body>
			<div class="flex flex-col h-full bg-gray-50 overflow-hidden">
				<!-- Tab Switcher -->
				<div class="px-6 pt-4 pb-2 bg-white border-b border-gray-100">
					<div class="bg-gray-100 p-1 rounded-2xl flex">
						<button 
							@click="activeTab = 'regional'"
							class="flex-1 py-2.5 text-xs font-black rounded-xl transition-all"
							:class="activeTab === 'regional' ? 'bg-white text-indigo-600 shadow-sm' : 'text-gray-500'"
						>
							{{ __("Regional") }}
						</button>
						<button 
							@click="activeTab = 'national'"
							class="flex-1 py-2.5 text-xs font-black rounded-xl transition-all"
							:class="activeTab === 'national' ? 'bg-white text-indigo-600 shadow-sm' : 'text-gray-500'"
						>
							{{ __("National") }}
						</button>
					</div>
				</div>

				<ion-content>
					<div class="pb-24">
						<!-- Top 3 Podium -->
						<div class="px-6 pt-8 pb-12 bg-gradient-to-b from-white to-gray-50 flex items-end justify-center gap-2 h-72 relative">
							<!-- Background decoration -->
							<div class="absolute top-10 left-1/2 -translate-x-1/2 w-64 h-64 bg-indigo-50 rounded-full blur-3xl opacity-50"></div>

							<!-- Rank 2 -->
							<div v-if="topThree[1]" class="flex flex-col items-center flex-1 max-w-[100px] animate-fade-in-up" style="animation-delay: 100ms">
								<div class="relative mb-3">
									<img :src="topThree[1].avatar" class="w-16 h-16 rounded-2xl border-4 border-white shadow-lg object-cover" />
									<div class="absolute -bottom-2 -right-2 w-8 h-8 bg-slate-200 rounded-lg flex items-center justify-center border-2 border-white shadow-sm">
										<span class="text-xs font-black text-slate-600">2</span>
									</div>
								</div>
								<span class="text-[10px] font-black text-gray-900 truncate w-full text-center">{{ topThree[1].name }}</span>
								<span class="text-[10px] font-bold text-indigo-600">{{ topThree[1].points }} pts</span>
								<div class="w-full h-16 bg-white rounded-t-2xl mt-4 border-x border-t border-gray-100 shadow-sm flex items-center justify-center">
									<Trophy class="w-5 h-5 text-slate-300" />
								</div>
							</div>

							<!-- Rank 1 -->
							<div v-if="topThree[0]" class="flex flex-col items-center flex-1 max-w-[120px] z-10 animate-fade-in-up">
								<div class="relative mb-4 scale-110">
									<Crown class="absolute -top-6 left-1/2 -translate-x-1/2 w-8 h-8 text-yellow-400 drop-shadow-sm" />
									<img :src="topThree[0].avatar" class="w-20 h-20 rounded-[2rem] border-4 border-white shadow-2xl object-cover ring-4 ring-yellow-400/20" />
									<div class="absolute -bottom-2 -right-2 w-10 h-10 bg-yellow-400 rounded-xl flex items-center justify-center border-2 border-white shadow-md">
										<span class="text-sm font-black text-white">1</span>
									</div>
								</div>
								<span class="text-xs font-black text-gray-900 truncate w-full text-center">{{ topThree[0].name }}</span>
								<span class="text-xs font-bold text-indigo-600">{{ topThree[0].points }} pts</span>
								<div class="w-full h-24 bg-white rounded-t-3xl mt-4 border-x border-t border-gray-100 shadow-xl flex items-center justify-center">
									<Trophy class="w-8 h-8 text-yellow-400" />
								</div>
							</div>

							<!-- Rank 3 -->
							<div v-if="topThree[2]" class="flex flex-col items-center flex-1 max-w-[100px] animate-fade-in-up" style="animation-delay: 200ms">
								<div class="relative mb-3">
									<img :src="topThree[2].avatar" class="w-16 h-16 rounded-2xl border-4 border-white shadow-lg object-cover" />
									<div class="absolute -bottom-2 -right-2 w-8 h-8 bg-amber-600 rounded-lg flex items-center justify-center border-2 border-white shadow-sm">
										<span class="text-xs font-black text-white">3</span>
									</div>
								</div>
								<span class="text-[10px] font-black text-gray-900 truncate w-full text-center">{{ topThree[2].name }}</span>
								<span class="text-[10px] font-bold text-indigo-600">{{ topThree[2].points }} pts</span>
								<div class="w-full h-12 bg-white rounded-t-2xl mt-4 border-x border-t border-gray-100 shadow-sm flex items-center justify-center">
									<Trophy class="w-5 h-5 text-amber-600/30" />
								</div>
							</div>
						</div>

						<!-- List of other users -->
						<div class="px-6 space-y-3 mt-4">
							<div 
								v-for="(user, index) in remainingUsers" 
								:key="user.id"
								class="bg-white rounded-2xl p-4 border border-gray-100 shadow-sm flex items-center gap-4 animate-fade-in"
								:style="`animation-delay: ${index * 50}ms`"
							>
								<span class="w-6 text-xs font-black text-gray-400">{{ index + 4 }}</span>
								<img :src="user.avatar" class="w-10 h-10 rounded-xl object-cover border border-gray-50" />
								<div class="flex-1">
									<h4 class="text-sm font-black text-gray-900 leading-none mb-1">{{ user.name }}</h4>
									<p class="text-[10px] font-bold text-gray-400 uppercase tracking-widest">{{ user.region }}</p>
								</div>
								<div class="text-right">
									<span class="text-sm font-black text-gray-900 block leading-none">{{ user.points }}</span>
									<span class="text-[9px] font-bold text-indigo-600 uppercase tracking-tighter">points</span>
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
</style>
