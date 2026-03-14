<template>
	<div 
		class="flex flex-col items-center gap-3 active:scale-90 transition-all cursor-pointer group"
		@click="$emit('select', category)"
	>
		<div class="w-16 h-16 rounded-2xl bg-white shadow-lg shadow-gray-100 flex items-center justify-center p-4 border border-gray-50 group-hover:bg-indigo-50 group-hover:border-indigo-100 transition-colors">
			<component :is="category.icon" class="w-7 h-7 text-gray-700 group-hover:text-indigo-600 transition-colors" />
		</div>
		<span class="text-[11px] font-black text-gray-900 tracking-tight text-center leading-tight">
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
