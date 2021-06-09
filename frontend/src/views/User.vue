<template>
    <div class="h-full flex items-center justify-center">
    <!-- <div class="w-1/12 h-auto"></div> -->
    <div class="w-268 h-auto blockr">
    <div class="text-base sm:text-3xl text-black font-bold relative text-center m-5">
        {{user.displayName}} さんのマイリスト
    </div>
    <div class="md:w-264 sm:w-180 w-120 ml-auto mr-auto"><MyList></MyList></div>
    </div>
    <!-- <div class="w-1/12 h-auto"></div> -->
    </div>
</template>
<script>
import firebase from 'firebase/app'
import MyList from'@/components/MyList.vue'
export default {
    name:"User",
    components:{
        MyList
    },
    data(){
        return {
            user:{}
        }
    },
    created(){
        firebase.auth().onAuthStateChanged(user => {
        this.user = user ? user : {};
        })
    },
    methods:{

    }
}
</script>