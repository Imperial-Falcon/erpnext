import { createRouter, createWebHistory } from "@ionic/vue-router"
import TabbedViewHome from "../views/TabbedViewHome.vue"

const routes = [
	{
		path: "/",
		redirect: "/home",
	},
	{
		path: "/",
		component: TabbedViewHome,
		children: [
			{
				path: "",
				redirect: "/home",
			},
			{
				path: "/home",
				name: "Home",
				component: () => import("@/views/Home.vue"),
			},
			{
				path: "/products",
				name: "Products",
				component: () => import("@/views/Products.vue"),
			},
			{
				path: "/offers",
				name: "Offers",
				component: () => import("@/views/Offers.vue"),
			},
			{
				path: "/cart",
				name: "Cart",
				component: () => import("@/views/Cart.vue"),
			},
			{
				path: "/profile",
				name: "Profile",
				component: () => import("@/views/Profile.vue"),
			},
		],
	},
]

const router = createRouter({
	history: createWebHistory("/b2b"),
	routes,
})

export default router