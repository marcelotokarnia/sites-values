<template>
  <div class="container">
    <h1>Site Details - {{site.name}}</h1>
    <table class="table">
      <thead>
        <tr><td><strong>Date</strong></td>
        <td><strong>A Value</strong></td><td><strong>B Value</strong></td></tr>
      </thead>

      <tbody>
        <tr v-for="value in site.values" :key="value.id">
          <td v-html="value.date" />
          <td v-html="value.a"/>
          <td v-html="value.b"/>
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
  import {AxiosPromise} from 'axios'
  export default Vue.extend({
    data(): IModel {
      return {
        site: {id: 1, name: 'Demo Site', values: [
          {id: 1, date: new Date(2015, 1, 1), a: 12, b: 16},
          {id: 2, date: new Date(2015, 1, 3), a: 20, b: 100},
          {id: 3, date: new Date(2015, 1, 10), a: 20, b: 80},
        ]},
      }
    },
    name: 'Site',
  })
</script>

<style>

</style>
