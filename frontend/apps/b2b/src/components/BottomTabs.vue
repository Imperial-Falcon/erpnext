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
			<component :is="item.icon" class="h-5 w-5" />
			<div>{{ item.title }}</div>
		</ion-tab-button>
	</ion-tab-bar>
</template>

<script setup>
import { useRoute } from "vue-router"

import { IonTabBar, IonTabButton, IonLabel } from "@ionic/vue"

import HomeIcon from "@/components/icons/HomeIcon.vue"
import LeaveIcon from "@/components/icons/LeaveIcon.vue"
import ExpenseIcon from "@/components/icons/ExpenseIcon.vue"
import SalaryIcon from "@/components/icons/SalaryIcon.vue"
import AttendanceIcon from "@/components/icons/AttendanceIcon.vue"
import { inject } from "vue"

const __ = inject("$translate")

const route = useRoute()

const tabItems = [
	{
		icon: HomeIcon,
		title: __("Home"),
		route: "/home",
	},
	{
		icon: AttendanceIcon,
		title: __("Attendance"),
		route: "/dashboard/attendance",
	},
	{
		icon: LeaveIcon,
		title: __("Leaves"),
		route: "/dashboard/leaves",
	},
	{
		icon: ExpenseIcon,
		title: __("Expenses"),
		route: "/dashboard/expense-claims",
	},
	{
		icon: SalaryIcon,
		title: __("Salary"),
		route: "/dashboard/salary-slips",
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
</style>
