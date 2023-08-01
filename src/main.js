import './assets/main1.css'

import { createApp } from 'vue'
// import App from './App.vue' 

// createApp(App).mount('#app') 

import App1 from './App1.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

createApp(App1).mount('#app1')

const app=createApp(App1)
app.use(ElementPlus)
app.mount('#app1')