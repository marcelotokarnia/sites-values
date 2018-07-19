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

const average = 'average', sum = 'sum', sites = 'sites', site = 'site', main = 'main'

const router = new VueRouter({
  mode: 'history',
  routes: [
    route('/sites/:id', site, Site),
    route('/summary-average', average, Summary),
    route('/summary', sum, Summary),
    route('/sites', sites, Main),
    route('/', main, Main),
  ],
})

export default router

export { average, main, site, sites, sum }