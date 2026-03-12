<template>
	<ion-page>
		<ion-tabs>
			<ion-router-outlet></ion-router-outlet>
			<BottomTabsHome />
		</ion-tabs>
	</ion-page>
</template>

<script setup>
import { IonTabs, IonPage, IonRouterOutlet } from "@ionic/vue"
import BottomTabsHome from "@/components/BottomTabsHome.vue"
</script>