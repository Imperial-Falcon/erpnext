<template>
	<div class="relative overflow-hidden pt-4 px-4">
		<div class="flex gap-4 overflow-x-auto no-scrollbar snap-x snap-mandatory">
			<div 
				v-for="(banner, index) in banners" 
				:key="index"
				class="min-w-full snap-center relative h-48 rounded-2xl overflow-hidden group shadow-xl shadow-gray-200/50"
				:class="banner.bgColor"
			>
				<!-- Abstract Background shapes -->
				<div class="absolute -top-10 -right-10 w-40 h-40 bg-white/10 rounded-full blur-3xl group-hover:scale-125 transition-transform duration-700"></div>
				<div class="absolute -bottom-10 -left-10 w-40 h-40 bg-white/10 rounded-full blur-3xl"></div>

				<div class="relative h-full flex items-center p-8 text-white z-10">
					<div class="flex-1 pr-4">
						<span class="inline-block px-3 py-1 bg-white/20 backdrop-blur-md rounded-full text-[10px] font-black uppercase tracking-widest mb-3">
							{{ banner.tag }}
						</span>
						<h2 class="text-2xl font-black leading-tight mb-4 drop-shadow-sm" v-html="banner.title"></h2>
						<button class="px-6 py-2 bg-white text-gray-900 text-xs font-black rounded-full hover:shadow-lg active:scale-95 transition-all">
							{{ banner.cta }}
						</button>
					</div>
					
					<div class="w-32 h-32 relative flex items-center justify-center">
						<div class="absolute inset-0 bg-white/10 rounded-full blur-2xl"></div>
						<img 
							:src="banner.image" 
							:alt="banner.tag" 
							class="w-full h-full object-contain relative z-10 group-hover:scale-110 group-hover:rotate-6 transition-transform duration-500 drop-shadow-2xl"
						/>
					</div>
				</div>
			</div>
		</div>

		<!-- Pagination Dots (Visual only for now) -->
		<div class="flex justify-center gap-1.5 mt-4">
			<div v-for="i in banners.length" :key="i" class="h-1.5 rounded-full transition-all" :class="i === 1 ? 'w-6 bg-indigo-600' : 'w-1.5 bg-gray-300'"></div>
		</div>
	</div>
</template>

<script setup>
const banners = [
	{
		tag: "Summer Offer",
		title: "25% OFF <br/>on All Vitamins",
		cta: "Shop Now",
		bgColor: "bg-indigo-600",
		image: "https://via.placeholder.com/200?text=Vitamins"
	},
	{
		tag: "New Arrival",
		title: "Pure Organic <br/>Honey Series",
		cta: "Explore",
		bgColor: "bg-emerald-600",
		image: "https://via.placeholder.com/200?text=Honey"
	},
	{
		tag: "Special Deal",
		title: "Premium <br/>Personal Care",
		cta: "Get Deals",
		bgColor: "bg-orange-600",
		image: "https://via.placeholder.com/200?text=Care"
	}
]
</script>
