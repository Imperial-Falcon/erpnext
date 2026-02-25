import { createRouter, createWebHistory } from 'vue-router'

const routes = [
	{
		path: '/',
		name: 'Home',
		component: () => import('@/views/Home.vue'),
	},
]

let router = createRouter({
	history: createWebHistory('/b2b'),
	routes,
})

export default router
