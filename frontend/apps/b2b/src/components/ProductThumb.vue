<template>
	<div class="bg-white relative rounded-sm border-gray-200 p-2 flex flex-col">
		<!-- Discount Badge -->
		<div
			v-if="product.discount_percent"
			class="absolute top-0 left-0 right-0 flex justify-center">
			<div class="bg-red-100 text-red-500 text-2xs text-center font-semibold px-2 py-1 rounded-b-sm z-10">
				{{ product.discount_percent }}%
			</div>
		</div>
		<!-- Product Image -->
		<div class="flex justify-center mt-2 mb-2 aspect-h-1 aspect-w-1">
			<img
				:src="product.image"
				:alt="product.item_name"
				class="h-full w-full object-contain"
			/>
		</div>
		<!-- Product Name -->
		<h3 class="text-sm font-semibold text-gray-800 leading-snug line-clamp-2">
			{{ product.item_name }}
		</h3>
		<!-- Weight -->
		<h6 class="text-xs font-light text-gray-500 mt-1 line-clamp-2">{{ product.manufacturer }}</h6>
		<!-- Price + Button -->
		<div class="flex items-end justify-between mt-3 ">
			<!-- Price -->
			<div>
				<p class="text-xs text-gray-400 line-through">৳{{ product.mrp }}</p>
				<p class="text-base font-semibold text-gray-900">৳{{ product.price }}</p>
			</div>

			<!-- Add Button -->
			<button
				class="p-1 font-semibold text-sm rounded-sm bg-green-500 transition"
			>
				<Plus color="#ffffff" />
			</button>
		</div>
	</div>
</template>
<script setup>
import { Plus } from 'lucide-vue-next'

defineProps({
    product: Object
})
</script>
