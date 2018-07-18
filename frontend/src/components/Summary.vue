<template>
  <div class="container">
    <h1>Sites</h1>
    <ul class="list-group">
      <li v-for="site in sites" :key="site.id" class="list-group-item">
        <a :href="`/sites/${site.id}`" v-html="site.name" />
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
  interface IModel {
  }

  import Vue from 'vue'
  import axios from 'axios'
  import {AxiosPromise} from 'axios'
  export default Vue.extend({
    data(): IModel {
      return {
        sites: [{id: 1, name: 'Demo Site'},{id: 2, name: 'ABC Site'},{id: 3, name: 'XYZ Site'}]
      }
    },
    methods: {
    },
    name: 'Main',
  })
</script>

<style>

</style>
