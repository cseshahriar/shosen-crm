<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
              <h1 class="title">My Account</h1>
            </div>

            <div class="column is-12">
                <router-link to="/dashboard/leads" class="button is-success"><strong>Leads</strong></router-link>
                <button @click="logout()" class="button is-danger">Log out</button>
            </div>

        </div>
    </div>    
</template>

<script>
    import axios from 'axios'
    import {toast} from 'bulma-toast'

    export default {
        name: 'MyAccount',
        methods: {
            async logout() {
                await axios
                    .post('/api/v1/token/logout')
                    .then(response => {
                        console.log('logout')
                    })
                    .catch(
                        error => {
                            console.log(JSON.stringify(error));
                        }
                    )

                    axios.defaults.headers.common['Authorization'] = ''     
                    localStorage.removeItem('token')
                    this.$store.commit('removeToken')
                    this.$router.push('/log-in')
            }
        }
    }
</script>

<style scoped>
</style>