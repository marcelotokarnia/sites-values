<template>
  <div class="container">
    <h1>Sites</h1>
    <ul class="list-group" v-if="sites">
      <li v-for="site in sites" :key="site.id" class="list-group-item">
        <a :href="`/sites/${site.id}`" v-html="site.name" />
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
  interface ISite {
    id: number
    name: string
  }
  interface IModel {
    loading: boolean
    sites?: ISite[]
  }

  import Vue from 'vue'
  import axios from 'axios'
  import {AxiosPromise} from 'axios'
  export default Vue.extend({
    created() {
      this.fetchData()
    },
    data(): IModel {
      return {
        loading: false,
        sites: undefined,
      }
    },
    methods: {
      fetchData(){
        axios(`/api/sites/?format=json`)
          .then(({data}) => {
            this.sites = data
          })
      }
    },
    name: 'Main',
  })
</script>

<style>

</style>
