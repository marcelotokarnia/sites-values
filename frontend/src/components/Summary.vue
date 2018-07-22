<template>
  <div class="container">
    <h1>Summary</h1>
    <a href="/summary">
      <button :class="`btn btn-primary ${mode === sum ? 'active': ''}`">
        Sum
      </button>
    </a>
    <a href="summary-average">
      <button :class="`btn btn-primary ${mode === average ? 'active': ''}`">
        Average
      </button>
    </a>
    <table class="table">
      <thead>
        <tr>
          <td><strong>Site</strong></td>
          <td><strong>A Value</strong></td><td><strong>B Value</strong></td>
        </tr>
      </thead>

      <tbody v-if="sites">
        <tr v-for="site in sites" :key="site.id">
          <td v-html="site.name" />
          <td v-html="site[mode].a" />
          <td v-html="site[mode].b" />
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script lang="ts">
  interface IValueSum {
    a: number
    b: number
  }
  interface ISiteSum {
    id: number
    name: string
    sum?: IValueSum
    average?: IValueSum
  }
  interface IModel {
    average: string
    sum: string
    mode?: string
    sites?: ISiteSum[]
  }

  import Vue from 'vue'
  import axios from 'axios'
  import { average, sum } from '@src/vue-router'
  import {AxiosPromise} from 'axios'
  export default Vue.extend({
    created() {
      this.fetchData()
    },
    data(): IModel {
      return {
        average,
        mode: this.$route.name,
        sites: undefined,
        sum,
      }
    },
    watch: {
      '$route': 'fetchData'
    },
    methods: {
      fetchData() {
        this.sites = undefined
        if (this.$route.name === sum) {
          axios('api/sites-summary').then(({data}) => {
            this.sites = data
          })
        } else {
          axios('api/sites-summary-average').then(({data}) => {
            this.sites = data
          })
        }
      }
    },
    name: 'Summary',
  })
</script>

<style>

</style>
