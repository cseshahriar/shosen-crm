<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1>Lead</h1>

                <div class="buttons">
                    <button @click="deleteLead" class="button is-small is-danger">Delete</button>
                </div>
            </div>

            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Details</h2>

                    <p><strong>Status: </strong>{{ lead.status }}</p>
                    <p><strong>Priority: </strong>{{ lead.priority }}</p>
                    <p><strong>Confidence: </strong>{{ lead.confidence }}</p>
                    <p><strong>Estimated value: </strong>{{ lead.estimated_value }}</p>
                    <p><strong>Created at: </strong>{{ lead.created }}</p>
                    <p><strong>Modified at: </strong>{{ lead.updated }}</p>
                </div>
            </div>

            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Contact Information</h2>

                    <p><strong>Contact person: </strong>{{ lead.contact_person }}</p>
                    <p><strong>Email: </strong>{{ lead.email }}</p>
                    <p><strong>Phone: </strong>{{ lead.phone }}</p>
                    <p><strong>Website: </strong>{{ lead.website }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import {toast} from 'bulma-toast'

    export default {
        name: 'Lead',
        data() {
            return {
                lead: {}
            }
        },
        mounted() {
            this.getLead()
        },
        methods: {
            async getLead() {
                this.$store.commit('setIsLoading', true)
                const leadID = this.$route.params.id
                await axios
                    .get(`/api/v1/leads/${leadID}/`)
                    .then(response => {
                        this.lead = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            },
            async deleteLead() {
                console.log('deleteLead')

                this.$store.commit('setIsLoading', true)
                const leadID = this.$route.params.id
                await axios
                    .post(`/api/v1/leads/delete_lead/${leadID}/`)
                    .then(response => {
                        this.$router.push('/dashboard/leads')
                        toast({
                            message: 'Lead has been deleted',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'top-right'
                        })
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            },
        }
    }
</script>

<style scoped>
.btn-edit {
    float: right;
}
</style>