<template>
	<div class="bg-white relative rounded-sm border-gray-200 p-2 flex flex-col gap-2">
		<!-- Discount Badge -->
		<div
			v-if="product.discount_percent"
			class="absolute top-0 left-0 right-0 flex justify-center">
			<div class="bg-red-100 text-red-500 text-2xs text-center font-semibold px-2 py-1 rounded-b-sm z-10">
				{{ product.discount_percent }}%
			</div>
		</div>
		<!-- Product Image -->
		<div class="flex justify-center aspect-h-1 aspect-w-1">
			<img
				:src="product.image"
				:alt="product.item_name"
				class="h-full w-full object-contain"
			/>
		</div>
		<!-- Product Name -->
		<h3 class="text-sm font-semibold text-gray-800 leading-snug line-clamp-2 flex-1">
			{{ product.item_name }}
		</h3>
		<!-- Weight -->
		<h6 class="text-xs text-gray-600 line-clamp-2">{{ product.manufacturer }}</h6>
		<!-- Price + Button -->
		<div class="flex items-end justify-between" v-if="product.stock_qty > 0">
			<!-- Price -->
			<div>
				<p v-if="product.mrp" class="text-xs text-gray-400 line-through">{{ formatCurrency(product.mrp, "BDT") }}</p>
				<p class="text-sm font-semibold text-gray-900">{{ formatCurrency(product.price, "BDT") }}</p>
			</div>

			<!-- Add Button -->
			<button
				class="p-1 font-semibold text-sm rounded-sm bg-green-500 transition"
			>
				<Plus color="#ffffff" />
			</button>
		</div>
		<div
			v-if="product.stock_qty <= 0"
			class="text-2xs py-0.5 rounded-sm text-gray-500 bg-gray-50 text-center">Out of Stock</div>
	</div>
</template>
<script setup>
import { formatCurrency } from '@/utils/formatters'
import { Plus } from 'lucide-vue-next'

defineProps({
    product: Object
})
</script>
