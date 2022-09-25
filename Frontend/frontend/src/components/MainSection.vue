<template>
    <div class="main-section">
        <div class="main-section__input-wrapper">
            <div  class="main-section__input">   
                <p>Username: </p>
                <input v-model="inputString" type="text" class="username" maxlength="255" minlength="1"/>
            </div>
            <button v-on:click="login">Login/Register</button>
        </div>
    </div>
</template>

<script>
import { backend_url } from '@/constants.js'
import axios from 'axios'

export default {
    name: 'main-section',
    data: function() {
        return {
            inputString: ''
        }
    },
    methods: {
        login: function () {
            //validate
            if (this.inputString.length < 1) {
                console.log('The input cannot be empty.')
            } else if (this.inputString.length > 255) {
                console.log('The input exceed maximum character count of 8000.')
            } else {
                axios({
                    method: 'get',
                    params:{
                        username: this.inputString
                    },
                    url: backend_url + 'room'
                }).then(response => {
                    console.log(response)
                })
                .catch(error => {
                    console.log(error)
                })
            }
        }
    }
}
</script>

<style lang="scss">
    @import '@/assets/scss/_variables.scss';
    .main-section {
        background-color: $color-white;
        height: 35rem;
        max-width: $global-max-width;
        display: block;
        margin: auto;
        border: 1px solid; // dev use only
    }

    .main-section__input-wrapper {
        display: flex; 
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        margin: 15rem auto;
        width: 80%;
        max-width: 30rem;    
        
        @media screen and (max-width: $mobile-width) {
            flex-direction: column;
            justify-content: flex-start;
            margin: 13rem auto;
        }
    }

    .main-section__input {
        width: 80%;
        padding-right: 3rem;
        input {
            width: 100%;
        }

        @media screen and (max-width: $mobile-width) {
            padding-right: 0;
            margin-bottom: 2rem;
        }
    }

    
</style>