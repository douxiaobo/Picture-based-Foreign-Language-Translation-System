import { createApp } from 'vue'
// import App from './App.vue' 

// createApp(App).mount('#app') 

import App from './App.vue'
import ElementPlus from 'element-plus'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import 'element-plus/dist/index.css'

const app = createApp(App)
for (var [name, comp] of Object.entries(ElementPlusIconsVue)) {
    console.log(name, comp);
    app.component(name, comp);
  }
app.use(ElementPlus)
app.mount('#app')