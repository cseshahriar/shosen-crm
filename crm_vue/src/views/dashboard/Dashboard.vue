<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Dashboard</h1>
            </div>

            <div class="column is-6">
                <div class="box has-background-primary">
                    <router-link to="/dashboard/clients" class="navbar-item has-text-black">Clients</router-link>
                </div>
            </div>

            <div class="column is-6">
                <div class="box has-background-info">
                    <router-link to="/dashboard/leads" class="navbar-item has-text-black">Leads</router-link>
                </div>
            </div>

            <div class="column is-6">
                <div class="box has-background-success">
                    <router-link to="/dashboard/team" class="navbar-item has-text-black">Team</router-link>
                </div>
            </div>

            <div class="column is-6">
                <div class="box has-background-warning">
                    <router-link to="/dashboard/my-account" class="navbar-item has-text-black"><strong>My Account</strong></router-link>
                </div>
            </div>


        </div>
    </div>    
</template>

<script>
    export default {
        name: 'Dashboard',
    }
</script>

<style scoped>

</style>