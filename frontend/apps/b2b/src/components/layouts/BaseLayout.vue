<template>
	<ion-page>
		<ion-header class="ion-no-border" :translucent="true">
			<ion-toolbar class="dark:bg-gray-900">
				<ion-buttons slot="start" v-if="props.showBackButton">
					<ion-back-button default-href="/home" text="" class="text-gray-900 dark:text-gray-100"></ion-back-button>
				</ion-buttons>
				<ion-title class="dark:text-gray-100">{{ props.pageTitle || "Doctoverse B2B" }}</ion-title>
				<ion-buttons slot="end">
					<slot name="actions"></slot>
				</ion-buttons>
			</ion-toolbar>
		</ion-header>

		<ion-content class="ion-no-padding">
			<div class="flex flex-col h-screen w-screen sm:w-96 bg-white dark:bg-black">
				<slot name="body"></slot>
			</div>
		</ion-content>
	</ion-page>
</template>

<script setup>
import { IonHeader, IonContent, IonPage, IonTitle, IonToolbar, IonButtons, IonBackButton } from "@ionic/vue"
import { inject } from "vue"

const props = defineProps({
	pageTitle: {
		type: String,
		required: false,
		default: "",
	},
	showBackButton: {
		type: Boolean,
		default: true,
	}
})
</script>
