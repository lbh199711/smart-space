<template>
    <div class="main-section">
        <div v-if="userId == null" class="main-section__input-wrapper">
            <div  class="main-section__input">   
                <p>Username: </p>
                <input v-model="inputString" type="text" class="username" maxlength="255" minlength="1"/>
            </div>
            <button v-on:click="login">Login/Register</button>
        </div>
        <div v-else class="main-section__display-wrapper">
            <div  class="main-section__display-section-wrapper ">   
                <h3>Rooms: </h3>
                <div class="main-section__display-list" v-for="(room,index) in rooms" :key="room.id" :class="{'green': room.occupied}">
                    <p class="top-row">
                        {{index}}
                        <button class="delete" v-on:click="deleteRoom(e, room.id)">X</button>
                    </p>
                    <p>Id: {{room.id}}</p>
                    <p>Name: {{room.room_name}}</p>
                    <p>Occupancy: {{room.occupied}}</p>
                </div>
            </div>

            <div class="main-section__display-section-wrapper">
                <h3>Update: </h3>
                <div  class="main-section__update">   
                    <input v-model="updateRoomId" type="int" class="main-section__update-input" placeholder="Id"/>
                    <input v-model="updateRoomTemp" type="float" class="main-section__update-input" placeholder="Temperature"/>
                    <input v-model="updateRoomHum" type="float" class="main-section__update-input" placeholder="Humidity"/>
                    <input v-model="updateRoomCo2" type="float" class="main-section__update-input" placeholder="Co2"/>
                    <input v-model="updateRoomLight" type="float" class="main-section__update-input" placeholder="Luminosity"/>
                    <button v-on:click="updateRoom">Update Room</button>
                </div>
            </div>

            <div class="main-section__display-section-wrapper">
                <h3>Create: </h3>
                <div  class="main-section__create">   
                    <input v-model="newRoomName" type="text" class="username" maxlength="80" minlength="1" placeholder="Room Name"/>
                    <button v-on:click="createRoom">Create Room</button>
                </div>
            </div>
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
            newRoomName: '',
            inputString: '',
            userId: null,
            rooms: [],

            //update
            updateRoomId: null,
            updateRoomCo2: null,
            updateRoomLight: null,
            updateRoomHum: null,
            updateRoomTemp: null
        }
    },
    methods: {
        login: function () {
            //validate
            if (this.inputString.length < 1) {
                console.log('The input cannot be empty.')
            } else {
                axios({
                    method: 'get',
                    params:{
                        username: this.inputString
                    },
                    url: backend_url + 'room'
                }).then(response => {
                    console.log(response)
                    if (response.data && response.data.user_id && response.data.rooms){
                        this.userId = response.data.user_id
                        this.rooms = response.data.rooms
                    }
                })
                .catch(error => {
                    console.log(error)
                })
            }
        },
        createRoom: function () {
            //validate
            if (this.newRoomName.length < 1) {
                console.log('The input cannot be empty.')
            } else {
                axios({
                    method: 'post',
                    data:{
                        user_id: this.userId,
                        room_name: this.newRoomName
                    },
                    url: backend_url + 'room'
                }).then(response => {
                    console.log(response)
                    if (response.data && response.data.rooms){
                        this.rooms = this.rooms.concat(response.data.rooms)
                    }
                })
                .catch(error => {
                    console.log(error)
                })
            }
        },
        updateRoom: function () {
            //validate
            if (this.newRoomId == 0) {
                console.log('The input cannot be 0.')
            } else {
                axios({
                    method: 'put',
                    data:{
                        room_id: this.updateRoomId,
                        temp: this.updateRoomTemp,
                        co2: this.updateRoomCo2,
                        light: this.updateRoomLight,
                        humidity: this.updateRoomHum
                    },
                    url: backend_url + 'room'
                }).then(response => {
                    console.log(response)
                    if (response.data && response.data.rooms){
                        var updatedRoom = response.data.rooms[0]

                        for (var i = 0; i < this.rooms.length; i++){
                            if (this.rooms[i].id == updatedRoom.id){
                                this.rooms[i] = updatedRoom
                            }
                        }
                    }
                })
                .catch(error => {
                    console.log(error)
                })
            }
        },
        deleteRoom: function (e, room_id) {
            //validate
            axios({
                method: 'delete',
                data:{
                    room_id: room_id,
                },
                url: backend_url + 'room'
            }).then(response => {
                console.log(response)
                if (response.data){
                    for (var i = 0; i < this.rooms.length; i++){
                        if (this.rooms[i].id == room_id){
                            this.rooms.splice(i, 1);
                        }
                    }
                }
            })
            .catch(error => {
                console.log(error)
            })
        }
    }
}
</script>

<style lang="scss">
    @import '@/assets/scss/_variables.scss';
    .main-section {
        background-color: $color-white;
        min-height: 20rem;
        max-width: $global-max-width;
        display: block;
        margin: auto;
        width: $global-width;
        max-width: $global-max-width;
        padding: 2rem $global-side-padding 1.75rem;

        @media screen and (max-width: $mobile-width) {
            padding: 2rem $global-side-padding-mobile 1.75rem;
            width: $global-width-mobile;
        }
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
    .main-section__display-section-wrapper {
        display: flex;
        flex-wrap: wrap;
        margin-bottom: 1rem;

        h3 {
            width: 100%;
        }

        input {
            margin: 1rem 0.5rem;
        }

        &.flex-column{
            flex-direction: column;
        }
    }

    .main-section__display-list {
        margin: 1rem 2rem;
        width: 16rem;
        border: solid 2px $color-secondary;
        border-radius: 5%;

        p {
            padding: 1rem 2rem;
        }

        &.green {
            color: $color-elf-green;
        }

        .top-row {
            display: flex;
            justify-content: space-between;
            font-weight: bold;
        }

        .delete {
            padding: 0.1rem 0.35rem;
            border-radius: 20%;
            background-color: $color-warning;
        }
    }
</style>