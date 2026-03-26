<template>
	<div 
		class="flex flex-col items-center gap-3 transition-transform duration-300 cursor-pointer group animate-fade-in-up"
		@click="$emit('select', category)"
	>
		<div class="w-16 h-16 rounded-[1.25rem] app-card flex items-center justify-center p-4 relative overflow-hidden">
			<div class="absolute inset-0 bg-gradient-to-br from-brand-primary to-brand-secondary opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
			<component :is="category.icon" class="w-7 h-7 text-gray-700 dark:text-gray-300 group-hover:text-white transition-colors duration-300 relative z-10" />
		</div>
		<span class="text-[11px] font-black text-gray-900 dark:text-gray-100 tracking-tight text-center leading-tight">
			{{ category.name }}
		</span>
	</div>
</template>

<script setup>
defineProps({
	category: Object
})
defineEmits(['select'])
</script>
