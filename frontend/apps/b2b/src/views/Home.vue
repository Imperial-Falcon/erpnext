<template>
	<BaseLayout>
		<template #body>
			<div class="page-content">
				<!-- Header massage bar -->
				<div class="w-full p-2">
					<div class="text-white text-center py-2 text-sm font-medium rounded-sm bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500">
						Free delivery on orders above ৳500!
					</div>
				</div>
				<!-- <ion-searchbar placeholder="Search Product or Brand.."></ion-searchbar> -->
				<!--product thumb  -->
				<div class="bg-gray-100 flex items-center justify-center min-h-screen">
					<!-- Card -->
					<div class="relative w-64 bg-white rounded shadow-sm border border-gray-200 p-4">

						<!-- Discount Badge -->
						<div class="absolute top-0 left-4 bg-blue-500 text-white text-xs font-semibold px-2 py-1 rounded-b-sm z-10">
						8%<br>OFF
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
						<p class="text-sm text-gray-500 mt-1">Popular pharmaceuticals Ltd.</p>

						<!-- Price + Button -->
						<div class="flex items-center justify-between mt-3">

						<!-- Price -->
						<div>
							<p class="text-lg font-semibold text-gray-900">৳101</p>
							<p class="text-sm text-gray-400 line-through">৳110</p>
						</div>

						<!-- Add Button -->
						<button
							class="border border-green-600 text-green-600 font-semibold text-sm px-4 py-1.5 rounded-sm hover:bg-green-50 transition"
						>
							ADD
						</button>

						</div>

					</div>
				</div>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import BaseLayout from "@/components/layouts/BaseLayout.vue"
</script>
