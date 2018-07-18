<template>
  <nav class="navbar navbar-expand-md navbar-light bg-light">
    <div class="navbar-collapse collapse" id="navbar">
      <ul class="mr-auto navbar-nav">
        <li class="nav-item active" role="presentation">
          <a class="nav-link" href="/sites">Sites</a>
        </li>
        <li class="nav-item" role="presentation">
          <a class="nav-link" href="/summary">Summary</a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script lang="ts">
  import Vue from 'vue'
  export default Vue.extend({
    name: 'Navbar',
  })
</script>