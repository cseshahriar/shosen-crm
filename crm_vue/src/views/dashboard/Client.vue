<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ client.name }}</h1>

                <div class="buttons">
                    <!-- lead edit problem -->
                    <!-- <button @click="deleteLead" class="button is-danger">Delete</button> -->
                </div>
            </div>

            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Details</h2>
                    <p><strong>Name: </strong>{{ client.name }}</p>
                    <p><strong>Created at: </strong>{{ client.created_at }}</p>
                    <p><strong>Modified at: </strong>{{ client.modified_at }}</p>
                </div>
            </div>

            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Contact information</h2>
                    <p><strong>Contact person: </strong>{{ client.contact_person }}</p>
                    <p><strong>Email: </strong>{{ client.email }}</p>
                    <p><strong>Phone: </strong>{{ client.phone }}</p>
                    <p><strong>Website: </strong>{{ client.website }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'Client',
        data() {
            return {
                client: {}
            }
        },
        mounted() {
            this.getClient()
        },
        methods: {
            async deleteClient() {
                this.$store.commit('setIsLoading', true)
                const clientID = this.$route.params.id
                await axios
                    .post(`/api/v1/clients/${clientID}/`)
                    .then(response => {
                        console.log(response.data)
                        this.$router.push('/dashboard/clients')
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            },

            async getClient() {
                this.$store.commit('setIsLoading', true)
                const clientID = this.$route.params.id
                await axios
                    .get(`/api/v1/clients/${clientID}/`)
                    .then(response => {
                        this.client = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            },
        }
    }
</script>