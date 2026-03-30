<template>
	<ion-page>
		<ion-content class="ion-padding">
			<div class="flex h-screen w-screen flex-col justify-center overflow-hidden relative" style="background: var(--app-bg);">
				<!-- Ambient Backdrops -->
				<div class="absolute inset-0 overflow-hidden pointer-events-none z-0">
					<div class="ambient-orb top-[-100px] left-[-80px] w-[350px] h-[350px] bg-brand-primary/15 animate-pulse-subtle"></div>
					<div class="ambient-orb bottom-[-50px] right-[-50px] w-[300px] h-[300px] bg-brand-secondary/15"></div>
					<div class="ambient-orb top-[40%] right-[20%] w-[200px] h-[200px] bg-brand-primary-light/8 animate-float"></div>
				</div>

				<div class="relative z-10 flex flex-col mx-auto gap-4 items-center animate-fade-in-up">
					<div class="w-20 h-20 bg-gradient-to-tr from-brand-primary to-brand-secondary rounded-[1.5rem] flex items-center justify-center shadow-neon animate-glow-pulse">
						<!-- Medicine Cross Icon -->
						<svg class="w-10 h-10 text-white drop-shadow-lg" viewBox="0 0 48 48" fill="none">
							<rect x="16" y="4" width="16" height="40" rx="4" fill="currentColor" opacity="0.9"/>
							<rect x="4" y="16" width="40" height="16" rx="4" fill="currentColor" opacity="0.9"/>
						</svg>
					</div>
					<div class="text-2xl font-extrabold text-gray-900 dark:text-gray-100 text-center leading-tight">
						{{ __("Login to MediMart") }}
					</div>
					<p class="text-xs font-medium text-gray-400 tracking-widest uppercase">{{ __("Your Trusted Medicine Partner") }}</p>
				</div>

				<div class="relative z-10 mx-auto mt-10 w-full px-8 sm:w-96 animate-fade-in-up" style="animation-delay: 0.1s">
					<form class="flex flex-col space-y-4" @submit.prevent="submit">
						<Input
							:label="__('Email')"
							:placeholder="__('johndoe@mail.com')"
							v-model="email"
							type="text"
							autocomplete="username"
						/>
						<Input
							:label="__('Password')"
							type="password"
							placeholder="••••••"
							v-model="password"
							autocomplete="current-password"
						/>
						<ErrorMessage :message="errorMessage" />
						<Button
							:loading="session.login.loading"
							variant="solid"
							class="disabled:bg-gray-700 disabled:text-white !mt-6 !rounded-[1.2rem] !h-14 !font-black !shadow-neon !bg-gradient-to-tr !from-brand-primary !to-brand-secondary"
						>
							{{ __("Login") }}
						</Button>
					</form>

					<template v-if="authProviders.data?.length">
						<div class="text-center text-xs font-bold text-gray-400 my-6 uppercase tracking-widest">{{ __("or") }}</div>
						<div class="space-y-3">
							<a
								v-for="provider in authProviders.data"
								:key="provider.name"
								class="flex items-center justify-center gap-3 app-card border border-white/40 shadow-glass h-12 text-sm font-bold text-gray-700 dark:text-gray-300 rounded-[1.2rem] active:scale-[0.98] transition-all"
								:href="provider.auth_url"
							>
								<img class="h-5 w-5" :src="provider.icon" :alt="provider.provider_name" />
								<span>{{ __("Login with") }} {{ provider.provider_name }}</span>
							</a>
						</div>
					</template>
				</div>
			</div>

			<Dialog v-model="resetPassword.showDialog">
				<template #body-title>
					<h2 class="text-lg font-black">{{ __("Reset Password") }}</h2>
				</template>
				<template #body-content>
					<p>{{ __("Your password has expired. Please reset your password to continue") }}</p>
				</template>
				<template #actions>
					<a
						class="inline-flex items-center justify-center gap-2 transition-colors text-white bg-gradient-to-tr from-brand-primary to-brand-secondary h-10 text-sm px-4 rounded-xl font-black"
						:href="resetPassword.link"
						target="_blank"
					>
						{{ __("Go to Reset Password page") }}
					</a>
				</template>
			</Dialog>

			<Dialog v-model="otp.showDialog">
				<template #body-title>
					<h2 class="text-lg font-black">{{ __("OTP Verification") }}</h2>
				</template>
				<template #body-content>
					<p class="mb-4" v-if="otp.verification.prompt">{{ otp.verification.prompt }}</p>
					<form class="flex flex-col space-y-4" @submit.prevent="submit">
						<Input :label="__('OTP Code')" type="text" placeholder="000000" v-model="otp.code" autocomplete="one-time-code" />
						<ErrorMessage :message="errorMessage" />
						<Button :loading="session.otp.loading" variant="solid" class="disabled:bg-gray-700 disabled:text-white !mt-6 !rounded-[1.2rem] !h-14 !font-black">
							{{ __("Verify") }}
						</Button>
					</form>
				</template>
			</Dialog>
		</ion-content>
	</ion-page>
</template>

<script setup>
import { IonPage, IonContent } from "@ionic/vue"
import { inject, reactive, ref } from "vue"
import { Input, Button, ErrorMessage, Dialog, createResource } from "frappe-ui"
import DoctoverseOfficeLogo from "@/components/icons/DoctoverseOfficeLogo.vue"

const email = ref(null)
const password = ref(null)
const errorMessage = ref("")
const resetPassword = reactive({ showDialog: false, link: "" })
const otp = reactive({ showDialog: false, tmp_id: "", code: "", verification: {} })
const session = inject("$session")
const __ = inject("$translate")

async function submit(e) {
	try {
		let response
		if (otp.showDialog) { response = await session.otp(otp.tmp_id, otp.code) }
		else { response = await session.login(email.value, password.value) }
		if (response.message === "Password Reset") { resetPassword.showDialog = true; resetPassword.link = response.redirect_to }
		else { resetPassword.showDialog = false; resetPassword.link = "" }
		if (response.verification) {
			if (response.verification.setup) { otp.showDialog = true; otp.tmp_id = response.tmp_id; otp.verification = response.verification }
			else { window.open("/login?redirect-to=" + encodeURIComponent(window.location.pathname), "_blank") }
		}
	} catch (error) { errorMessage.value = error.messages.join("\n") }
}

const authProviders = createResource({ url: "hrms.api.oauth.oauth_providers", auto: true })
</script>
