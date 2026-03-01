<template>
	<BaseLayout>
		<template #body>
			<div class="page-content">
				<!-- Hero banner -->
				<section class="hero-banner">
					<img
						src="https://picsum.photos/320/180"
						alt="Hero Banner"
						class="w-full h-auto object-cover"
					/>
				</section>
				<section class="w-full p-2 flex flex-col gap-4">
					<!-- Header massage bar -->
					<div class="text-white text-center py-2 text-sm font-medium rounded-sm bg-gradient-to-r from-cyan-500 to-blue-500">
						1$ off for all products
					</div>
					<!-- Main nav bar -->
					<nav class="text-sm text-gray-500 flex items-center gap-4 justify-center">
						<a href="#" class="hover:underline underline-offset-8 decoration-blue-500 decoration-2">Today's</a>
						<a href="#" class="hover:underline underline-offset-8 decoration-blue-500 decoration-2">Categories</a>
						<a href="#" class="hover:underline underline-offset-8 decoration-blue-500 decoration-2">Menufacturers</a>
						<a href="#" class="hover:underline underline-offset-8 decoration-blue-500 decoration-2">Top Offers</a>
					</nav>
					<!-- Search bar -->
					<div class="font-medium rounded-sm border-2 border-blue-500 flex justify-between py-2 px-3 text-gray-500 items-center">
						<h4 class="text-sm">Search products</h4>
						<button class="text-sm">
							<Search size="18"/>
						</button>
					</div>
					<!-- Features section -->
					<div class="flex flex-row gap-1">
						<div class="flex items-center gap-3 bg-white py-3 px-4 rounded-sm">
							<div>
								<ScrollText size="30"/>
							</div>
							<div class="text-wrap w-20">
								<h3 class="text-xs text-gray-600">Request for Products</h3>
							</div>
						</div>
						<div class="flex items-center gap-3 bg-white py-3 px-4 rounded-sm">
							<div>
								<Trophy size="30"/>
							</div>
							<div class="text-wrap w-20">
								<h3 class="text-xs text-gray-600">Top Ranking</h3>
							</div>
						</div>
						<div class="flex items-center gap-3 bg-white py-3 px-4 rounded-sm">
							<div>
								<ScrollText size="30"/>
							</div>
							<div class="text-wrap w-20">
								<h3 class="text-xs text-gray-600">Request for Quotation</h3>
							</div>
						</div>
					</div>
					<!-- Top customers section -->
					<div class="grid grid-cols-2 divide-x justify-stretch">
						<div>
							<div class="flex items-center gap-3 flex-1">
								<div>
									<ScrollText size="30"/>
								</div>
								<div class="">
									<h3 class="text-xs text-gray-600">Request for Products</h3>
								</div>
							</div>
						</div>
						<div>
							<div class="flex items-center gap-3 flex-1">
								<div>
									<Trophy size="30"/>
								</div>
								<div class="">
									<h3 class="text-xs text-gray-600">Top Ranking</h3>
								</div>
							</div>
						</div>
					</div>
				</section>
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
import { Search, ScrollText, Trophy } from 'lucide-vue-next';
</script>
