import Main from '@src/components/Main'
import Summary from '@src/components/Summary'
import Site from '@src/components/Site'
import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

interface IRoute {
  component: typeof Vue
  name: string
  path: string
}

const route = (path: string, name: string, component: typeof Vue): IRoute => ({
  component,
  name,
  path,
})

const router = new VueRouter({
  mode: 'history',
  routes: [
    route('/sites/:id', 'site', Site),
    route('/summary', 'summary', Summary),
    route('/sites', 'main', Main),
    route('/', 'main', Main),
  ],
})

export default router
