<template>
	<div class="bg-white relative rounded-sm border-gray-200 p-2">
		<!-- Discount Badge -->
		<div class="absolute top-0 left-0 right-0 flex justify-center">
			<div class="bg-red-100 text-red-500 text-2xs text-center font-semibold px-2 py-1 rounded-b-sm z-10">
				8% - 12%
			</div>
		</div>
		<!-- Product Image -->
		<div class="flex justify-center mt-2 mb-2 aspect-h-1 aspect-w-1">
			<img
				src="https://cdn.grofers.com/cdn-cgi/image/f=auto,fit=scale-down,q=70,metadata=none,w=270/da/cms-assets/cms/product/669a9b3f-7d5e-434e-bec2-f976bc976916.png"
				alt="Pringles"
				class="h-full w-full object-contain"
			/>
		</div>
		<!-- Product Name -->
		<h3 class="text-sm font-semibold text-gray-800 leading-snug line-clamp-2">
			Coconut Hookah Coal Cubes by Stash Pro
		</h3>
		<!-- Weight -->
		<p class="text-xs font-light text-gray-500 mt-1 line-clamp-2">Popular pharmaceuticals Ltd.</p>
		<!-- Price + Button -->
		<div class="flex items-end justify-between mt-3 ">
			<!-- Price -->
			<div>
				<p class="text-xs text-gray-400 line-through">৳110</p>
				<p class="text-base font-semibold text-gray-900">৳101</p>
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
</script>
