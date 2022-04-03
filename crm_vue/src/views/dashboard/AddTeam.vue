<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add Team</h1> 
                 <form @submit.prevent="submitForm">

                    <div class="field">
                        <label>Team name</label>
                        <div class="control">
                            <input type="text" class="input" v-model="name">
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
    name: 'AddTeam',
    data() {
        return {
            name: '',
            errors: [],
        }
    },
    methods: {
        async submitForm() {
            this.$store.commit('setIsLoading', true)
            const team = {
                name : this.name,
            }
            
            if(this.name === '') {
                    this.errors.push('The name is required')
            }

            if(!this.errors.length) {
                await axios
                    .post('/api/v1/teams/', team)
                    .then(response => {
                        toast({
                            message: 'The team was added',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                        
                        this.$store.commit('setItem', {'id': response.data.id, 'name': response.data.name})

                        this.$router.push('/dashboard')
                    })
                    .catch(error => {
                        console.log(error)
                    })
            }

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>

<style scoped>

</style>
