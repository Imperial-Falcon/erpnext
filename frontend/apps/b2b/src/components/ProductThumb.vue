<template>
	<!-- 1. VERTICAL VARIANT (Default) -->
	<div
		v-if="variant === 'vertical'"
		@click="$router.push(`/product/${product.name}`)"
		class="app-card p-3 flex flex-col group h-full cursor-pointer relative overflow-hidden"
	>
		<div class="absolute inset-0 bg-gradient-to-br from-brand-primary/5 to-brand-secondary/5 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
		<div class="aspect-square bg-white/50 dark:bg-gray-800/50 rounded-xl mb-3 overflow-hidden p-3 flex items-center justify-center relative shadow-inner">
			<img :src="product.image" :alt="product.item_name" class="max-w-full max-h-full object-contain group-hover:scale-110 transition-transform duration-500 ease-out" />
			<!-- Discount Badge -->
			<div v-if="discount" class="absolute top-0 left-0 bg-gradient-to-r from-brand-accent to-red-500 text-white text-[10px] font-black px-2 py-1 rounded-br-xl shadow-md">
				{{ discount }}
			</div>
			<button class="absolute top-2 right-2 p-1.5 app-card !rounded-full text-gray-400 hover:text-brand-accent hover:shadow-neon transition-all border-none">
				<Heart class="w-3.5 h-3.5" />
			</button>
		</div>

		<h3 class="text-sm font-bold text-gray-900 dark:text-gray-100 line-clamp-2 leading-tight mb-1 min-h-[2.5rem] relative z-10">
			{{ product.item_name }}
		</h3>
		<p class="text-[10px] text-gray-500 dark:text-gray-400 mb-2 relative z-10">{{ product.manufacturer || product.brand }}</p>

		<div class="mt-auto flex items-center justify-between relative z-10">
			<div class="flex flex-col">
				<span v-if="product.oldPrice || product.mrp" class="text-[10px] text-gray-400 line-through">
					{{ formatCurrency(product.oldPrice || product.mrp, "BDT") }}
				</span>
				<span class="text-sm font-black bg-clip-text text-transparent bg-gradient-to-r from-brand-primary to-brand-secondary">
					{{ formatCurrency(product.price, "BDT") }}
				</span>
			</div>
			<button
				@click.stop="$emit('add-to-cart', product)"
				class="p-2 bg-gradient-to-tr from-brand-primary to-brand-secondary text-white rounded-xl shadow-lg hover:shadow-neon transition-all active:scale-90"
			>
				<Plus class="w-4 h-4" />
			</button>
		</div>
	</div>

	<!-- 2. HORIZONTAL VARIANT (List Style) -->
	<div
		v-else-if="variant === 'horizontal'"
		@click="$router.push(`/product/${product.name}`)"
		class="app-card p-3 flex gap-4 cursor-pointer group"
	>
		<div class="w-24 h-24 bg-white/50 dark:bg-gray-800/50 rounded-xl flex-shrink-0 flex items-center justify-center p-2 relative overflow-hidden shadow-inner">
			<img :src="product.image" :alt="product.item_name" class="max-w-full max-h-full object-contain group-hover:scale-105 transition-transform duration-500" />
			<div v-if="discount" class="absolute top-0 left-0 bg-gradient-to-r from-brand-accent to-red-500 text-white text-[9px] font-black px-1.5 py-0.5 rounded-br-lg shadow-sm">
				{{ discount }}
			</div>
		</div>

		<div class="flex-1 flex flex-col justify-between py-1">
			<div>
				<div class="flex justify-between items-start">
					<h3 class="text-sm font-bold text-gray-900 dark:text-gray-100 line-clamp-1 leading-tight">
						{{ product.item_name }}
					</h3>
					<button class="text-gray-300 dark:text-gray-600 hover:text-brand-accent transition-colors">
						<Heart class="w-4 h-4" />
					</button>
				</div>
				<p class="text-[11px] text-gray-500 dark:text-gray-400 mt-1">{{ product.manufacturer }}</p>
			</div>

			<div class="flex items-end justify-between">
				<div class="flex flex-col">
					<span v-if="product.oldPrice || product.mrp" class="text-[10px] text-gray-400 line-through">
						{{ formatCurrency(product.oldPrice || product.mrp, "BDT") }}
					</span>
					<span class="text-base font-black bg-clip-text text-transparent bg-gradient-to-r from-brand-primary to-brand-secondary">
						{{ formatCurrency(product.price, "BDT") }}
					</span>
				</div>
				<button
					@click.stop="$emit('add-to-cart', product)"
					class="px-4 py-1.5 bg-gradient-to-r from-brand-primary to-brand-secondary text-white text-xs font-bold rounded-lg shadow-md hover:shadow-neon active:scale-95 transition-all"
				>
					Add
				</button>
			</div>
		</div>
	</div>

	<!-- 3. MINIMAL VARIANT (Compact) -->
	<div
		v-else-if="variant === 'minimal'"
		@click="$router.push(`/product/${product.name}`)"
		class="app-card inline-flex flex-col w-32 p-2 flex-shrink-0 group cursor-pointer"
	>
		<div class="aspect-square bg-white/50 dark:bg-gray-800/50 rounded-[0.75rem] mb-2 p-2 flex items-center justify-center relative overflow-hidden shadow-inner">
			<img :src="product.image" :alt="product.item_name" class="max-w-full max-h-full object-contain group-hover:scale-110 transition-transform duration-500 ease-out" />
			<span v-if="discount" class="absolute top-0 left-0 bg-gradient-to-r from-orange-400 to-brand-accent text-white text-[8px] font-bold px-1.5 py-0.5 rounded-br-lg shadow-sm">
				{{ discount }}
			</span>
		</div>
		<h4 class="text-[11px] font-bold text-gray-900 dark:text-gray-100 line-clamp-1 mb-1">{{ product.item_name }}</h4>
		<p class="text-xs font-black bg-clip-text text-transparent bg-gradient-to-r from-brand-primary to-brand-secondary">{{ formatCurrency(product.price, "BDT") }}</p>
	</div>
</template>

<script setup>
import { computed } from 'vue'
import { Plus, Heart } from 'lucide-vue-next'
import { formatCurrency } from '@/utils/formatters'

const props = defineProps({
	product: {
		type: Object,
		required: true
	},
	variant: {
		type: String,
		default: 'vertical', // 'vertical' | 'horizontal' | 'minimal'
		validator: (value) => ['vertical', 'horizontal', 'minimal'].includes(value)
	}
})

defineEmits(['add-to-cart'])

const discount = computed(() => {
	if (props.product.discount_percent) return `${props.product.discount_percent}%`
	if (props.product.discount) return props.product.discount

	const oldPrice = props.product.oldPrice || props.product.mrp
	if (oldPrice && oldPrice > props.product.price) {
		const diff = oldPrice - props.product.price
		const percent = Math.round((diff / oldPrice) * 100)
		return `${percent}%`
	}
	return null
})
</script>
