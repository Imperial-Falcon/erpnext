<template>
	<ion-page>
		<ion-content :fullscreen="true" class="splash-content" :scroll-y="false">
			<div class="flex flex-col items-center justify-center h-full w-full relative overflow-hidden">
				<!-- Ambient Background -->
				<div class="absolute inset-0 bg-gradient-to-br from-brand-primary via-brand-secondary to-brand-primary-dark"></div>

				<!-- Animated Orbs -->
				<div class="absolute top-[-20%] left-[-15%] w-[400px] h-[400px] bg-white/10 rounded-full blur-3xl animate-morph"></div>
				<div class="absolute bottom-[-15%] right-[-20%] w-[350px] h-[350px] bg-brand-secondary/20 rounded-full blur-3xl animate-morph" style="animation-delay: 2s;"></div>
				<div class="absolute top-[40%] left-[60%] w-[200px] h-[200px] bg-white/5 rounded-full blur-2xl animate-float-slow"></div>

				<!-- Grain overlay for depth -->
				<div class="absolute inset-0 opacity-[0.03]" style="background-image: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHdpZHRoPScyMDAnIGhlaWdodD0nMjAwJz48ZmlsdGVyIGlkPSdhJz48ZmVUdXJidWxlbmNlIHR5cGU9J2ZyYWN0YWxOb2lzZScgYmFzZUZyZXF1ZW5jeT0nLjc1JyBzdGl0Y2hUaWxlcz0nc3RpdGNoJy8+PC9maWx0ZXI+PHJlY3Qgd2lkdGg9JzEwMCUnIGhlaWdodD0nMTAwJScgZmlsdGVyPSd1cmwoI2EpJy8+PC9zdmc+');"></div>

				<!-- Content -->
				<div class="relative z-10 flex flex-col items-center gap-8">
					<!-- Logo Container -->
					<div class="animate-scale-in">
						<div class="w-28 h-28 rounded-[2rem] bg-white/15 backdrop-blur-xl border border-white/20 flex items-center justify-center shadow-float animate-glow-pulse">
							<div class="flex flex-col items-center gap-1">
								<!-- Medicine Cross Icon -->
								<svg class="w-12 h-12 text-white drop-shadow-lg" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
									<rect x="16" y="4" width="16" height="40" rx="4" fill="currentColor" opacity="0.9"/>
									<rect x="4" y="16" width="40" height="16" rx="4" fill="currentColor" opacity="0.9"/>
								</svg>
							</div>
						</div>
					</div>

					<!-- App Name -->
					<div class="text-center animate-fade-in-up stagger-2">
						<h1 class="text-4xl font-black text-white tracking-tight mb-2 drop-shadow-lg">
							MediMart
						</h1>
						<p class="text-sm font-medium text-white/60 tracking-widest uppercase">
							Your Trusted Medicine Partner
						</p>
					</div>

					<!-- Loading Indicator -->
					<div class="animate-fade-in stagger-4 mt-6">
						<div class="flex items-center gap-2">
							<div class="w-2 h-2 rounded-full bg-white/80 animate-bounce-subtle"></div>
							<div class="w-2 h-2 rounded-full bg-white/60 animate-bounce-subtle" style="animation-delay: 150ms;"></div>
							<div class="w-2 h-2 rounded-full bg-white/40 animate-bounce-subtle" style="animation-delay: 300ms;"></div>
						</div>
					</div>
				</div>

				<!-- Bottom Tagline -->
				<div class="absolute bottom-12 left-0 right-0 text-center animate-fade-in stagger-6">
					<p class="text-[11px] font-medium text-white/30 tracking-wider">
						Healthcare for Bangladesh 🇧🇩
					</p>
				</div>

				<!-- Fade-out overlay for transition -->
				<div
					v-if="fadeOut"
					class="absolute inset-0 bg-white dark:bg-gray-950 z-50 transition-opacity duration-500"
					:class="fadeOut ? 'opacity-100' : 'opacity-0'"
				></div>
			</div>
		</ion-content>
	</ion-page>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { IonPage, IonContent } from '@ionic/vue'

const router = useRouter()
const fadeOut = ref(false)

onMounted(() => {
	// Stay on splash for 2.5s, then fade out and navigate
	setTimeout(() => {
		fadeOut.value = true
		setTimeout(() => {
			router.replace('/home')
		}, 500)
	}, 2500)
})
</script>

<style scoped>
.splash-content {
	--background: transparent;
}
</style>
