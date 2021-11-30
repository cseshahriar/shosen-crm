<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1>Lead 
                    <router-link to="/" class="button is-primary is-small btn-edit">Edit</router-link>
                </h1>
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
          
        }
    }
</script>

<style scoped>
.btn-edit {
    float: right;
}
</style>