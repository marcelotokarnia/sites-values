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

      <tbody>
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
  interface IModel {
  }

  import Vue from 'vue'
  import axios from 'axios'
  import { average, sum } from '@src/vue-router'
  import {AxiosPromise} from 'axios'
  export default Vue.extend({
    data(): IModel {
      return {
        average,
        mode: this.$route.name,
        sites: [
          {id: 1, name: 'Demo Site', sum: {a: 52, b: 196}, average: {a: 17.33, b: 65.33}},
          {id: 2, name: 'ABC Site', sum: {a: 5, b: 15}, average: {a: 5, b: 15}},
          {id: 3, name: 'XYZ Site', sum: {a: 10, b: 30}, average: {a: 5, b: 15}}
        ],
        sum,
      }
    },
    methods: {
    },
    name: 'Summary',
  })
</script>

<style>

</style>
