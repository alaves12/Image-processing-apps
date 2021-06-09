<template>
    <div>
        <div v-for="(image, index) in mylist" :key="index" class="mylist">
            <div class="h-auto text-center">
                <img :src="image.content" width="256" class="ml-auto mr-auto mb-1">
                <button @click="showmodal(index);showDeleteModal=true" class="bg-red-500 hover:bg-red-400 text-white font-medium py-1 px-2 m-1 border border-red-400 rounded shadow">
                    <!-- <span class="text-red-500 font-bold">削除</span>     -->
                    削除
                </button>
                <button @click="showimage(index);showImageModal=true" class="bg-white hover:bg-gray-100 text-gray-800 font-medium py-1 px-2 m-1 border border-gray-400 rounded shadow">
                    <!-- <span class="text-red-500 font-bold">拡大</span>     -->
                    拡大
                </button>
            </div>
        </div>

        <div v-show="showDeleteModal" tabindex="0"
            class="z-40  left-0 top-0 bottom-0 right-0 w-full h-full fixed">
            <div @v-click-away="ClickAway" class="z-50 relative p-3 mx-auto my-0 max-w-full"
                style="width: 500px;" id="modal">
                <div class="bg-white rounded shadow-lg border flex flex-col overflow-hidden px-10 py-10">
                    <div class="text-center">
                        <span
                            class="material-icons border-4 rounded-full p-4 text-red-500 font-bold border-red-500 text-4xl">
                            注意
                        </span>
                    </div>
                    <div class="text-center pt-3 m-5 text-2xl text-gray-700">本当に削除しますか？</div>
                    <div class="text-center font-light text-gray-700 mb-8">
                        この操作は元に戻すことができません
                    </div>
                    <div class="flex justify-center">
                        <button @click="showDeleteModal=false"
                            class="bg-gray-300 text-gray-900 rounded hover:bg-gray-200 px-6 py-2 focus:outline-none mx-1">Cancel</button>
                        <button @click="deleteimage()"
                            class="bg-red-500 text-gray-200 rounded hover:bg-red-400 px-6 py-2 focus:outline-none mx-1">Delete</button>
                    </div>
                </div>
            </div>
            <div class="z-40 overflow-auto left-0 top-0 bottom-0 right-0 w-full h-full fixed bg-opacity-50"></div>
        </div>

        <div v-show="showImageModal" tabindex="0"
            class="z-40  left-0 top-0 bottom-0 right-0 w-full h-full fixed">
            <div @v-click-away="ClickAway" class="z-50 relative p-3 mx-auto my-0 max-w-full"
                style="width: 500px;" id="modal">
                <div class="bg-white rounded shadow-lg border flex flex-col overflow-hidden px-10 py-10">
                    <img :src="showimgsrc" alt="">
                    <div class="flex justify-center">
                        <button @click="showImageModal=false"
                            class="bg-gray-300 text-gray-900 rounded hover:bg-gray-200 px-6 py-2 focus:outline-none mx-1 mt-2">閉じる</button>
                    </div>
                </div>
            </div>
            <div class="z-40 overflow-auto left-0 top-0 bottom-0 right-0 w-full h-full fixed bg-opacity-50"></div>
        </div>

        <div>
            <div>

            </div>
        </div>
    </div>
</template>

<script>
import firebase from 'firebase/app'
export default {
    // props:{
    //     user:{
    //         type:Object,
    //         required:false
    //     }
    // },
    name:"MyList",
    data(){
        return {
            mylist:[],
            user:{},
            showDeleteModal:false,
            showImageModal:false,
            deleteindex:'',
            showindex:'',
            showimgsrc:''
        }
    },
    created(){
        firebase.auth().onAuthStateChanged(user => {
        this.user = user ? user : {};
        console.log(this.user);
        const imageref = 'users/' + this.user.uid + '/image';
        var imagelist = firebase.database().ref(imageref);
        imagelist.on("value", (data)=>{
            // console.log(data.val());
            this.mylist = data.val();
            console.log(this.mylist);
        });
        })
    },
    methods:{
        ClickAway(){
            console.log(this.showDeleteModal)
            if(this.showDeleteModal==true){
                this.showDeleteModal = false;
            }
        },
        showmodal(index){
            this.deleteindex = index
        },
        showimage(index){
            this.showimgsrc = this.mylist[index].content
        },
        deleteimage(){
            delete this.mylist[this.deleteindex];

            console.log(this.mylist,"delted")
            this.showDeleteModal = false;
            const imageref = 'users/' + this.user.uid + '/image';
            var imagelist = firebase.database().ref(imageref);
            imagelist.set(this.mylist)
        }
        
    }
}
</script>
<style>
    /* Do this instead: */
    .mylist {
    @apply inline-block relative items-center justify-center w-80 p-3 mr-20 ml-20 mt-3 mb-3 border border-black shadow-lg;
    }
    @screen  sm{
    .mylist {
        @apply m-4;
    }
    }


</style>