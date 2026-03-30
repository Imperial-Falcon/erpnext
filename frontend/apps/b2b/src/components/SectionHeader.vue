<template>
	<div class="flex justify-between items-end mb-5 px-5">
		<div class="space-y-1">
			<h2 class="text-lg font-extrabold text-gray-900 dark:text-gray-100 leading-none tracking-tight">{{ title }}</h2>
			<p v-if="subtitle" class="text-[11px] font-medium text-gray-400 dark:text-gray-500 leading-none tracking-wide">{{ subtitle }}</p>
		</div>
		<button
			v-if="showSeeAll"
			@click="$emit('see-all')"
			class="text-[10px] font-bold text-brand-primary bg-brand-primary/8 dark:bg-brand-primary/15 px-3.5 py-1.5 rounded-full active:scale-95 transition-all duration-300 tracking-widest uppercase hover:bg-brand-primary/15 dark:hover:bg-brand-primary/25"
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
