<template>
	<ion-tab-bar
		slot="bottom"
		class="glass-tab-bar sm:w-96 py-2 pb-2 standalone:pb-safe-bottom"
	>
		<ion-tab-button
			v-for="item in tabItems"
			:key="item.title"
			:tab="item.title"
			:href="item.route"
			:class="[
				'text-xs space-y-1.5 transition-all active:scale-90 relative bg-transparent',
				route.path === item.route
					? 'text-brand-primary font-black drop-shadow-sm'
					: 'text-gray-400 dark:text-gray-500 font-medium',
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
ion-tab-bar.glass-tab-bar {
	--background: rgba(255, 255, 255, 0.7);
	backdrop-filter: blur(24px);
	--border: none;
	border-top: 1px solid rgba(255, 255, 255, 0.3);
	box-shadow: 0 -4px 30px rgba(0, 0, 0, 0.05);
}

@media (prefers-color-scheme: dark) {
	ion-tab-bar.glass-tab-bar {
		--background: rgba(10, 10, 10, 0.7);
		border-top: 1px solid rgba(255, 255, 255, 0.05);
		box-shadow: 0 -4px 30px rgba(0, 0, 0, 0.3);
	}
}

ion-badge {
	--padding-start: 4px;
	--padding-end: 4px;
}
</style>
