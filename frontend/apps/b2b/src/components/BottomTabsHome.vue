<template>
	<ion-tab-bar
		slot="bottom"
		class="bg-white shadow-md sm:w-96 py-2 pb-2 standalone:pb-safe-bottom"
	>
		<ion-tab-button
			v-for="item in tabItems"
			:key="item.title"
			:tab="item.title"
			:href="item.route"
			:class="[
				'bg-white text-xs space-y-1.5 !hover:border-gray-300 !hover:text-gray-700 transition active:scale-95 relative',
				route.path === item.route
					? 'border-gray-900 text-gray-800 font-semibold'
					: 'text-gray-600 font-normal',
			]"
		>
			<div class="relative">
				<component :is="item.icon" class="h-5 w-5" />
				<!-- Red Badge for Cart -->
				<ion-badge 
					v-if="item.title === 'Cart' && cartCount > 0" 
					color="danger" 
					class="absolute -top-2 -right-3 text-[10px] min-w-[18px] h-[18px] flex items-center justify-center rounded-full border-2 border-white px-1"
				>
					{{ cartCount }}
				</ion-badge>
			</div>
			<div>{{ item.title }}</div>
		</ion-tab-button>
	</ion-tab-bar>
</template>

<script setup>
import { useRoute } from "vue-router"
import { ref } from "vue"
import { IonTabBar, IonTabButton, IonBadge } from "@ionic/vue"
import { PackageSearch, House, BadgePercent, ShoppingCart, User } from 'lucide-vue-next';

const route = useRoute()

// Mock cart count - this would ideally come from a store like Pinia
const cartCount = ref(4)

const tabItems = [
	{
		icon: House,
		title: "Home",
		route: "/home",
	},
	{
		icon: PackageSearch,
		title: "Products",
		route: "/products",
	},
	{
		icon: BadgePercent,
		title: "Offers",
		route: "/offers",
	},
	{
		icon: ShoppingCart,
		title: "Cart",
		route: "/cart",
	},
	{
		icon: User,
		title: "Profile",
		route: "/profile",
	},
]
</script>

<style scoped>
ion-badge {
	--padding-start: 4px;
	--padding-end: 4px;
}
</style>
