import './main.css'

import { Button, frappeRequest, resourcesPlugin, setConfig } from 'frappe-ui'

import App from './App.vue'
import { createApp } from 'vue'
import router from './router'

let app = createApp(App)

setConfig('resourceFetcher', frappeRequest)

app.use(router)
app.use(resourcesPlugin)

app.component('Button', Button)
app.mount('#app')
