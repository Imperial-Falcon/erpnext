<template>
	<ion-tab-bar
		slot="bottom"
		class="glass-tab-bar sm:w-96 py-1.5 standalone:pb-safe-bottom"
	>
		<ion-tab-button
			v-for="item in tabItems"
			:key="item.title"
			:tab="item.title"
			:href="item.route"
			class="relative bg-transparent transition-all duration-300"
			:class="[
				route.path === item.route
					? 'text-brand-primary'
					: 'text-gray-400 dark:text-gray-500',
			]"
		>
			<div class="relative flex flex-col items-center gap-1">
				<!-- Active indicator pill -->
				<div
					class="absolute -top-1.5 w-8 h-1 rounded-full transition-all duration-500 ease-out"
					:class="route.path === item.route ? 'bg-gradient-to-r from-brand-primary to-brand-secondary scale-100 opacity-100' : 'scale-0 opacity-0'"
				></div>

				<!-- Icon Container -->
				<div
					class="relative p-1.5 rounded-xl transition-all duration-300"
					:class="route.path === item.route ? 'bg-brand-primary/10 dark:bg-brand-primary/15' : ''"
				>
					<component
						:is="item.icon"
						class="h-5 w-5 transition-all duration-300"
						:class="route.path === item.route ? 'text-brand-primary scale-110' : 'text-gray-400 dark:text-gray-500'"
					/>
					<!-- Cart Badge -->
					<span
						v-if="item.title === 'Cart' && cartCount > 0"
						class="absolute -top-1.5 -right-2 min-w-[18px] h-[18px] flex items-center justify-center rounded-full text-[10px] font-black text-white px-1 border-2 border-white dark:border-gray-900 shadow-sm"
						style="background: linear-gradient(135deg, #f43f5e, #f97316);"
					>
						{{ cartCount }}
					</span>
				</div>

				<!-- Label -->
				<span
					class="text-[10px] transition-all duration-300"
					:class="route.path === item.route ? 'font-black text-brand-primary' : 'font-medium text-gray-400 dark:text-gray-500'"
				>
					{{ item.title }}
				</span>
			</div>
		</ion-tab-button>
	</ion-tab-bar>
</template>

<script setup>
import { useRoute } from "vue-router"
import { ref } from "vue"
import { IonTabBar, IonTabButton } from "@ionic/vue"
import { House, PackageSearch, BadgePercent, ShoppingCart, User } from 'lucide-vue-next'

const route = useRoute()

// Mock cart count — should come from a store
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
	--background: rgba(255, 255, 255, 0.78);
	backdrop-filter: blur(28px);
	-webkit-backdrop-filter: blur(28px);
	--border: none;
	border-top: 1px solid rgba(5, 150, 105, 0.06);
	box-shadow: 0 -8px 32px rgba(0, 0, 0, 0.04), 0 -2px 8px rgba(5, 150, 105, 0.03);
}

@media (prefers-color-scheme: dark) {
	ion-tab-bar.glass-tab-bar {
		--background: rgba(3, 7, 18, 0.82);
		border-top: 1px solid rgba(5, 150, 105, 0.08);
		box-shadow: 0 -8px 32px rgba(0, 0, 0, 0.3), 0 -2px 8px rgba(5, 150, 105, 0.05);
	}
}

ion-tab-button {
	--color: inherit;
	--color-selected: inherit;
	--background: transparent;
	--background-focused: transparent;
	--padding-top: 6px;
	--padding-bottom: 4px;
}
</style>
