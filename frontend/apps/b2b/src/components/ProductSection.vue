<template>
	<div class="bg-red-200">
		<div class="header flex items-center justify-between px-3 py-3">
			<div class="title">
				<h2 class="text-lg font-semibold text-gray-800">Top Deals</h2>
				<h6 class="text-xs font-light text-gray-600">Score the lowest prices on Doctoverse B2B</h6>
			</div>
			<div>
				<ArrowRight color="#383838" />
			</div>
		</div>
		<div class="body px-3 pb-3 grid grid-cols-3 gap-1">
			<ProductThumb />
			<ProductThumb />
			<ProductThumb />
		</div>
	</div>
</template>

<script setup>
import ProductThumb from '@/components/ProductThumb.vue';
import { ArrowRight } from 'lucide-vue-next';
</script>
