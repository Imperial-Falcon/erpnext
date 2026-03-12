<template>
	<ion-page>
		<ion-header class="ion-no-border" :translucent="true">
			<ion-toolbar>
				<ion-title>{{ props.pageTitle || "Doctoverse B2B" }}</ion-title>
			</ion-toolbar>
		</ion-header>

		<ion-content class="ion-no-padding">
			<div class="flex flex-col h-screen w-screen sm:w-96">
				<slot name="body"></slot>
			</div>
		</ion-content>
	</ion-page>
</template>

<script setup>
import { IonHeader, IonContent, IonPage, IonTitle, IonToolbar } from "@ionic/vue"
import { inject } from "vue"

const props = defineProps({
	pageTitle: {
		type: String,
		required: false,
		default: "",
	},
})
</script>
