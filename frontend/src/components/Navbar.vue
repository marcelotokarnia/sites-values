<template>
  <nav class="navbar navbar-expand-md navbar-light bg-light">
    <div class="navbar-collapse collapse" id="navbar">
      <ul class="mr-auto navbar-nav">
        <li :class="`nav-item ${active === 'sites' ? 'active' : ''}`" role="presentation">
          <a class="nav-link" href="/sites">Sites</a>
        </li>
        <li :class="`nav-item ${active === 'summary' ? 'active' : ''}`" role="presentation">
          <a class="nav-link" href="/summary">Summary</a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script lang="ts">
  import Vue from 'vue'
  import { average, main, site, sites, sum } from '@src/vue-router'
  export default Vue.extend({
    name: 'Navbar',
    data() {
      const route = this.$route.name
      return {
        active: route === average || route === sum ?
          'summary' :
          route === main || route === sites || route === site ?
            'sites' :
            '',
        route
      }
    }
  })
</script>

<style scoped lang="stylus">
  nav
    margin-bottom 20px
    border 1px solid rgb(231, 231, 231)
</style>