<template>
  <div>
    <Navbar />
    <router-view />
  </div>
</template>

<script lang="ts">
  import Vue from 'vue'
  import Main from '@src/components/Main.vue'
  import Navbar from '@src/components/Navbar.vue'
  import Temperature from '@src/components/Temperature.vue'
  export default Vue.extend({
    name: 'App',
    components: {
      Main,
      Navbar,
    }
  })
</script>

<style>
</style>