import Vue from 'vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import './globals.styl'
import App from '@src/components/App.vue'
import router from './vue-router'

const v = new Vue({
    components: {
        App,
    },
    el: '#app',
    router,
    template: `<App />`,
})
