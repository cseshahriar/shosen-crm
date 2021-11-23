<template>
<div class="app"> <!-- base.html -->
  <Navbar/>  

  <section class="section">
    <router-view/>
  </section>
  
</div>
</template>

<script>
  import Navbar from '@/components/layout/Navbar'

  export default {
    name: 'App',
    components: {
      Navbar
    }
  }
</script>

<style lang="scss">
@import '../node_modules/bulma';
</style>
