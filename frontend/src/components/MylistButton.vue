<template>
    <div>
    <button class="flex items-center justify-center h-9 w-40 m-3 rounded bg-indigo-200 hover:bg-indigo-300 border-2 border-blue-400" @click="saveimage">
        <div class="text-black">
            マイリストに保存
        </div>
    </button>
    </div>
</template>
<script>
import firebase from 'firebase/app'
export default {
    name:"MylistButton",
    props: {
        image:{
            type:Object,
            // default:{},
            required:false
        }
    },
    data(){
        return {
            user:{uid:false},
            isuser:false
        }
    },
    created(){
        firebase.auth().onAuthStateChanged(user => {
            this.user = user ? user : {uid:false};
        })
    },
    methods:{
        saveimage(){
            this.$emit('showisLogin',true);
            if(this.user.uid==false){
                this.$emit('showisLogin',false);
            }else{
            console.log(this.user,"user");
            const imageref = 'users/' + this.user.uid + '/image';
            var imagelist = firebase.database().ref(imageref);
            imagelist.push({
                content:this.image.src
            });
            imagelist.on("value", (data)=>{
                console.log(data.val());
            });
            }
        },
        senderr(){
            this.$emit('showisLogin',false);
        }
    }

}
</script>
