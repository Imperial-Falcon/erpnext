<template>
	<section class="feature flex flex-col gap-2">
		<div class="flex flex-row gap-1">
			<div class="flex items-center gap-3 bg-white py-3 px-4 rounded-sm">
				<div>
					<PackageSearch size="30" color="#0FA5E9"/>
				</div>
				<div class="text-wrap w-20">
					<h3 class="text-xs font-semibold text-gray-800">Source by Category</h3>
				</div>
			</div>
			<div class="flex items-center gap-3 bg-white py-3 px-4 rounded-sm">
				<div>
					<ScrollText size="30" color="#0FA5E9"/>
				</div>
				<div class="text-wrap w-20">
					<h3 class="text-xs font-semibold text-gray-800">Request for Products</h3>
				</div>
			</div>
			<div class="flex items-center gap-3 bg-white py-3 px-4 rounded-sm">
				<div>
					<Trophy size="30" color="#0FA5E9"/>
				</div>
				<div class="text-wrap w-20">
					<h3 class="text-xs font-semibold text-gray-800">Top Ranking</h3>
				</div>
			</div>
			<div class="flex items-center gap-3 bg-white py-3 px-4 rounded-sm">
				<div>
					<ScrollText size="30" color="#0FA5E9"/>
				</div>
				<div class="text-wrap w-20">
					<h3 class="text-xs font-semibold text-gray-800">Request for Quotation</h3>
				</div>
			</div>
		</div>
		<!-- Top customers section -->
		<div class="grid grid-cols-2 divide-x justify-stretch bg-gradient-to-r from-red-500 to-orange-500 rounded-sm py-4">
			<div class="flex justify-center items-center">
				<div class="flex items-center gap-3 max-w-40">
					<div>
						<TruckElectric size="30" color="#ffffff"/>
					</div>
					<div class="text-wrap">
						<h3 class="text-sm font-semibold text-white">Superfast!</h3>
						<h6 class="text-xs font-light text-white/70">Same day delivery</h6>
					</div>
				</div>
			</div>
			<div class="flex justify-center items-center">
				<div class="flex items-center gap-3 max-w-40">
					<div>
						<DiamondPercent size="30" color="#ffffff"/>
					</div>
					<div class="text-wrap">
						<h3 class="text-sm font-semibold text-white">More Discount!</h3>
						<h6 class="text-xs font-light text-white/70">Buy more get more</h6>
					</div>
				</div>
			</div>
		</div>
	</section>
</template>

<script setup>
import { PackageSearch, ScrollText, Trophy, TruckElectric, DiamondPercent } from 'lucide-vue-next';
</script>
