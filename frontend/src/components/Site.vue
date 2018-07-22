<template>
  <div class="container">
    <h1>Site Details - {{loading ? '' : site.name}}</h1>
    <table class="table" >
      <thead>
        <tr><td><strong>Date</strong></td>
        <td><strong>A Value</strong></td><td><strong>B Value</strong></td></tr>
      </thead>

      <tbody v-if="site">
        <tr v-for="value in site.values" :key="value.id">
          <td v-html="parseDate(value.date)" />
          <td v-html="value.a.toFixed(2)"/>
          <td v-html="value.b.toFixed(2)"/>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script lang="ts">
  interface IValue {
    a: number
    b: number
    date: number
    id: number
  }

  interface IModel {
    site?: {
      id: number
      name: string
      values: IValue[]
    }
    loading: boolean
  }

  import Vue from 'vue'
  import axios from 'axios'
  const moment = require('moment')
  import {AxiosPromise} from 'axios'
  export default Vue.extend({
    created() {
      this.fetchData()
    },
    data(): IModel {
      return {
        site: undefined,
        loading: false,
      }
    },
    methods: {
      parseDate(dt: number) {
        return moment(dt).format("MMM[.] D[,] YYYY")
      },
      fetchData() {
        this.loading = true
        axios(`/api/sites/${this.$route.params.id}/?format=json&detailed`)
          .then(({data}) => {
            this.loading = false
            this.site = data
          }).catch(()=> {
            this.loading = false
          })
      },
    },
    name: 'Site',
    watch: {
      '$route': 'fetchData'
    },
  })
</script>

<style>

</style>
