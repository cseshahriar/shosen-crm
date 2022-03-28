<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Clients</h1>
                <router-link to="/dashboard/clients/add" class="button is-info">Add Client</router-link>
                <hr>
                <form @submit.prevent="getLeads">
                    <div class="field has-addons">
                        <div class="control">
                            <input type="text" class="input" v-model="query">
                        </div>
                        <div class="control">
                            <button class="button is-success">Search</button>
                        </div>
                    </div>
                </form>
            </div>

            <div class="column is-12">
                <template v-if="clients.length">
                    <table class="table is-fullwidth">
                        <thead>
                            <tr>
                                <th>Company</th>
                                <th>Contact person</th>
                                <th>Action</th>
                            </tr>
                        </thead>

                        <tbody>
                            <tr
                                v-for="client in clients"
                                v-bind:key="client.id">
                                    <td>{{ client.name }}</td>
                                    <td>{{ client.contact_person }}</td>
                                    <td>
                                        <div class="buttons">
                                            <router-link :to="{ name: 'Client', params: { id: client.id }}">Detail </router-link> &nbsp;
                                            <router-link :to="{ name: 'EditClient', params: { id: client.id }}"> Edit</router-link>
                                        </div>
                                    </td>
                            </tr>
                        </tbody>
                    </table>
                </template>

                <template v-else>
                    <p>You don't have any clients yet...</p>
                </template>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'Clients',
        data() {
            return {
                clients: [],
            }
        },
        mounted() {
            this.getClients()
        },
        methods: {
            async getClients() {
                
                this.$store.commit('setIsLoading', true)

                await axios
                    .get(`/api/v1/clients/`)
                    .then(response => {
                        console.log(response.data)
                        this.clients = response.data
                    })

                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>