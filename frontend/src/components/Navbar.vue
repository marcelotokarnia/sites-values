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
        active: [average, sum].includes(route) ?
          'summary' :
          [main, sites, site].includes(route) ?
            'sites' :
            '',
        route
      }
    }
  })
</script>