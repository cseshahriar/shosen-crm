<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Team</h1> 

                <hr>
                <p><strong>Plan: {{ $store.state.team.plan }} </strong></p>
                <p><strong>Max Leads: {{ $store.state.team.max_leads }} </strong></p>
                <p><strong>Max Clients: {{ $store.state.team.max_clients }} </strong></p>
                <hr>
                <p>
                    <router-link :to="{name: 'Plans'}" class="button is-info" style="margin-bottom:10px">Change plan</router-link>
                </p>

                <template v-if="team.created_by.id === parseInt($store.state.user.id)">
                    <router-link :to="{'name': 'AddMember'}" class="button is-primary">Add Member</router-link>
                </template>
            </div>

            <div class="column is-12">
                <h2 class="subtitle">Members</h2>
                
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Username</th>
                            <th>Full Name</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="member in team.members" :key="member.id">
                            <td>{{ member.username }}</td>
                            <td>{{ member.first_name }} {{ member.last_name }}</td>
                        </tr>
                    </tbody>
                </table>

            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'

export default {
    name: 'Team',
    data() {
        return {
            team: {
                members: [],
                created_by: {},
            }
        }
    },
    mounted() {
        this.getTeam()
    },
    methods: {
        async getTeam() {
            this.$store.commit('setIsLoading', true)

            await axios
                .get("/api/v1/teams/get_my_team/")
                .then(response => {
                    console.log('response', response.data)
                    this.team = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>

<style scoped>

</style>
