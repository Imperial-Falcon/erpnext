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
				'bg-white text-xs space-y-1.5 !hover:border-gray-300 !hover:text-gray-700 transition active:scale-95',
				route.path === item.route
					? 'border-gray-900 text-gray-800 font-semibold'
					: 'text-gray-600 font-normal',
			]"
		>
			<component :is="item.icon" class="h-5 w-5" />
			<div>{{ item.title }}</div>
		</ion-tab-button>
	</ion-tab-bar>
</template>

<script setup>
import { useRoute } from "vue-router"

import { IonTabBar, IonTabButton } from "@ionic/vue"
import { PackageSearch, House, BadgePercent, ShoppingCart, User } from 'lucide-vue-next';

const route = useRoute()

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
