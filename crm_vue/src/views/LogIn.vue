<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Log In</h1>
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input type="text" name="email" v-model="username" class="input">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" name="password" v-model="password" class="input">
                        </div>
                    </div>

                    <div class="notification is-warning" v-if="errors.length">
                        <p v-for="error in errors" :key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Submit</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>    
</template>

<script>
    import axios from 'axios'
    import {toast} from 'bulma-toast'

    export default {
        name: 'LogIn',
        data() {
            return {
                username: '',
                password: '',
                errors: []
            }
        },
        methods: {
            async submitForm() {
                this.$store.commit('setIsLoading', true)

                axios.defaults.headers.common['Authorization'] = '' 
                localStorage.removeItem('token')

                this.errors = []

                // validation
                if(this.username === '') {
                    this.errors.push('The username is missing')
                }

                if(this.password === '') {
                    this.errors.push('The password is missing')
                }

                if(!this.errors.length) {
                    const formData = {
                        username: this.username,
                        password: this.password,
                    }

                    await axios
                    .post('/api/v1/token/login/', formData)
                    .then(response => {
                        const token = response.data.auth_token
                        this.$store.commit('setToken', token)
                        axios.defaults.headers.common['Authorization'] = 'Token ' + token
                        localStorage.setItem('token', token)
                    })
                    .catch(error => {
                        if(error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                        } else if(error.message ) {
                            this.errors.push('Something went wrong. Please try again!')
                        }
                    })

                    await axios
                        .get('/api/v1/users/me')
                        .then(response => {
                            this.$store.commit(
                                'setUser', {
                                    'id': response.data.id,
                                    'username': response.data.username
                                }
                            )
                            localStorage.setItem('username', response.data.username)
                            localStorage.setItem('userid', response.data.id)
                        })
                        .catch(error => {
                            console.log(error)
                        })

                    await axios
                        .get('/api/v1/teams/get_my_team')
                        .then(response => {
                            console.log(response.data)
                            this.$store.commit(
                                'setTeam', {
                                    'id': response.data.id,
                                    'name':response.data.name,
                                    'plan': response.data.plan.name,
                                    'max_leads': response.data.plan.max_leads,
                                    'max_clients': response.data.plan.max_clients,
                                }
                            )
                            this.$router.push('/dashboard/my-account')
                        })
                        .catch(error => {
                            console.log(error)
                        })

                    this.$store.commit('setIsLoading', false)
                }
            }

        }
    }
</script>


<style scoped>

</style>