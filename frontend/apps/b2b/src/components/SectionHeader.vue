<template>
	<div class="flex justify-between items-end mb-5 px-5">
		<div class="space-y-1">
			<h2 class="text-lg font-black text-gray-900 dark:text-gray-100 leading-none tracking-tight">{{ title }}</h2>
			<p v-if="subtitle" class="text-[11px] font-bold text-gray-400 dark:text-gray-500 leading-none uppercase tracking-widest">{{ subtitle }}</p>
		</div>
		<button
			v-if="showSeeAll"
			@click="$emit('see-all')"
			class="text-[10px] font-black text-brand-primary bg-brand-primary/10 px-3.5 py-1.5 rounded-full active:scale-95 transition-all tracking-widest uppercase hover:shadow-neon"
		>
			See All
		</button>
	</div>
</template>

<script setup>
defineProps({
	title: String,
	subtitle: String,
	showSeeAll: {
		type: Boolean,
		default: true
	}
})
defineEmits(['see-all'])
</script>
