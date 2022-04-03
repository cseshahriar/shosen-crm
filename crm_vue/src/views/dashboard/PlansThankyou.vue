<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Thank you</h1> 
            </div>

            <div class="column is-12">
                <h1 class="title">Thank you for subscribbing to a plan!</h1> 
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'

export default {
    name: 'PlansThankyou',
    data() {
        return {
            plans:[]
        }
    },
    mounted() {},
    methods: {}
}
</script>

<style scoped>

</style>
