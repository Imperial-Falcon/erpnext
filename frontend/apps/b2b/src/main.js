import { createApp } from "vue"
import App from "./App.vue"
import router from "./router"

import { IonicVue } from "@ionic/vue"

/* Core CSS required for Ionic components to work properly */
import "@ionic/vue/css/core.css"

/* Theme variables */
import "./theme/variables.css"

import "./main.css"

const app = createApp(App)
app.use(IonicVue)
app.use(router)

router.isReady().then(() => {
    app.mount('#app')
})