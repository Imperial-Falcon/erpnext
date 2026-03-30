<template>
	<div
		class="px-5 transition-all duration-500 ease-out z-50 sticky top-0"
		:class="[
			isScrolled
				? 'backdrop-blur-2xl shadow-glass py-3 border-b'
				: 'bg-transparent pt-12 pb-4',
			isScrolled && !customClass
				? 'bg-white/75 dark:bg-gray-950/75 border-brand-primary/5'
				: '',
			customClass
		]"
	>
		<div class="relative flex items-center justify-between min-h-[40px]">
			<!-- Left Area: Back Button or Custom -->
			<div class="flex items-center gap-2 z-10 w-1/4">
				<button
					v-if="showBack"
					@click="$router.go(-1)"
					class="p-2 app-card !rounded-xl shadow-sm active:scale-90 transition-all duration-300 hover:shadow-glass"
				>
					<ChevronLeft class="w-5 h-5 text-gray-700 dark:text-gray-300" />
				</button>
				<slot name="left"></slot>
			</div>

			<!-- Center Area: Title and Subtitle -->
			<div class="absolute inset-0 flex flex-col items-center justify-center pointer-events-none">
				<div class="flex flex-col items-center animate-fade-in-up">
					<span v-if="subtitle" class="text-[10px] font-bold uppercase tracking-[0.2em] text-brand-primary/70 leading-none mb-1">
						{{ subtitle }}
					</span>
					<h1
						class="text-lg font-extrabold leading-none whitespace-nowrap tracking-tight"
						:class="titleClass ? titleClass : 'text-transparent bg-clip-text bg-gradient-to-r from-brand-primary to-brand-secondary'"
					>
						{{ title }}
					</h1>
				</div>
			</div>

			<!-- Right Area: Slot for icons -->
			<div class="flex items-center justify-end gap-2 z-10 w-1/4">
				<slot name="actions"></slot>
			</div>
		</div>
		<slot name="bottom"></slot>
	</div>
</template>

<script setup>
import { ChevronLeft } from 'lucide-vue-next'

defineProps({
	title: {
		type: String,
		required: true
	},
	subtitle: {
		type: String,
		default: ''
	},
	showBack: {
		type: Boolean,
		default: true
	},
	isScrolled: {
		type: Boolean,
		default: true
	},
	customClass: {
		type: String,
		default: ''
	},
	titleClass: {
		type: String,
		default: ''
	}
})
</script>
