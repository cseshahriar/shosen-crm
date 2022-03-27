<template>
    <nav class="navbar is-dark">
        <div class="navbar-brand">
            <router-link to="/" class="navbar-item">
                <strong>Shosen CRM</strong>
            </router-link>
        </div>

        <div class="navbar-menu">

            <div class="navbar-end">
                <template v-if="$store.state.isAuthenticated">
                    <router-link to="/dashboard/clients" class="navbar-item">Clients</router-link>
                    <router-link to="/dashboard/leads" class="navbar-item">Leads</router-link>
                    <router-link to="/dashboard/team" class="navbar-item">Team</router-link>
                    <router-link to="/dashboard/my-account" class="navbar-item"><strong>My Account</strong></router-link>
                    <button @click="logout()" class="button is-small is-danger btn-logout">Log out</button>
                </template>

                <div class="navbar-item">
                    <div class="buttons">
                        <template v-if="!$store.state.isAuthenticated">
                            <router-link to="/sign-up" class="button is-success"><strong>Sign Up</strong></router-link>
                            <router-link to="/log-in" class="button is-light"><strong>Log In</strong></router-link>
                        </template>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
    import axios from 'axios'
    import {toast} from 'bulma-toast'
    export default {
        name: 'Navbar',
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
.btn-logout {
    margin-top: 12px;
}
</style>
