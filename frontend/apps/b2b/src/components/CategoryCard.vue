<template>
	<div
		class="flex flex-col items-center gap-2.5 transition-transform duration-300 cursor-pointer group animate-fade-in-up min-w-[72px]"
		@click="$emit('select', category)"
	>
		<div class="w-[60px] h-[60px] rounded-[1.25rem] flex items-center justify-center relative overflow-hidden transition-all duration-300 group-active:scale-90"
			:class="category.bgClass || 'app-card'"
		>
			<!-- Hover gradient overlay -->
			<div class="absolute inset-0 bg-gradient-to-br from-brand-primary to-brand-secondary opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
			<!-- Icon glow -->
			<div class="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500 bg-[radial-gradient(circle,rgba(255,255,255,0.2)_0%,transparent_70%)]"></div>
			<component
				:is="category.icon"
				class="w-6 h-6 relative z-10 transition-all duration-300"
				:class="category.iconClass || 'text-gray-600 dark:text-gray-400 group-hover:text-white'"
			/>
		</div>
		<span class="text-[10px] font-black text-gray-700 dark:text-gray-300 tracking-tight text-center leading-tight max-w-[72px]">
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
