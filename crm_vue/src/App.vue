<template>
<div class="app"> <!-- base.html -->
  <Navbar/>  

  <div class="is-loading-bar has-text-center" v-bind:class="{'is-loading': $store.state.isLoading}">
    <div class="lds-dual-ring"></div>
  </div>

  <section class="section">
    <router-view/>
  </section>
  
</div>
</template>

<script>
  import axios from "axios"
  import Navbar from '@/components/layout/Navbar'

  export default {
    name: 'App',
    components: {
      Navbar
    },
    beforeCreate() {
        this.$store.commit('initializeStore')

        console.log('beforecreate user', this.$store.state.user)
        console.log('beforecreate team', this.$store.state.team)

        if (this.$store.state.token) {
            axios.defaults.headers.common['Authorization'] = "Token " + this.$store.state.token
        } else {
            axios.defaults.headers.common['Authorization'] = ""
        }
        
        // if don't have a team than redirect to add a new team
        if(!this.$store.state.team.id) {
          this.$router.push('/dashboard/add-team')
        }
    },
  }
</script>

<style lang="scss">
@import '../node_modules/bulma';
.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: "";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height:0;
  overflow: hidden;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}
</style>
