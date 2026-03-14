<template>
	<div class="flex justify-between items-end mb-4 px-4">
		<div class="space-y-1">
			<h2 class="text-xl font-black text-gray-900 leading-none tracking-tight">{{ title }}</h2>
			<p v-if="subtitle" class="text-xs font-medium text-gray-400 leading-none">{{ subtitle }}</p>
		</div>
		<button v-if="showSeeAll" @click="$emit('see-all')" class="text-xs font-black text-indigo-600 active:opacity-60 bg-indigo-50 px-3 py-1 rounded-full transition-all">
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
