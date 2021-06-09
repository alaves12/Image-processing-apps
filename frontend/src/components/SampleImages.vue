<template>
<div>
    <div>
        <div class="text-3xl text-black font-bold text-center pt-10">
            サンプル画像
        </div>
        <div class="p-5 text-xl text-black text-center">
            サンプル画像を用いて、処理結果がどのようになるのかみることが出来ます。
            <p class="p-3">処理したいサンプル画像をクリック</p>
        </div>
    </div>
    <div class="sm:flex justify-center items-center text-center">
        <div class="inline-block px-5 py-5" v-for="(obj, index) in imagesList" :key="index">
            <img :src="obj" alt="sample" width="256" height="256" @click="sendimage($event);activate(index)" :class="{activestyle :isactive[index]}">
            <!-- <button class="h-auto w-10" @click="showimg">ボタン</button> -->
        </div>
    </div>
</div>
</template>

<script>
export default {
    name: "SampleImages",
    props:{
        task:String,
    },
    data() {
        return {
            imagesDir:{
                dehaze:[require('@/assets/dehaze/sample1.jpg'),require('@/assets/dehaze/sample2.jpg'),require('@/assets/dehaze/sample3.jpg')]
            },
            base64Image:"",
            isactive:[false,false,false]
        }
    },
    emits: ['showsample'],
    methods:{
        getSource(){
            let k = this.task;
            let dir = this.imagesDir[k];
            return dir+'/sample1.jpg'
        },
        showimg(){
            let img = document.getElementById("image");
            console.log(img);
        },
        toBase64Url(e, callback){
            let xhr = new XMLHttpRequest();
            xhr.onload = function() {
                let reader = new FileReader();
                reader.onloadend = function() {
                callback(e,reader.result);
                }
                reader.readAsDataURL(xhr.response);
            };
            xhr.open('GET', e.target.src);
            xhr.responseType = 'blob';
            xhr.send();
        },
        activate(index){
            console.log(index);
            this.isactive = [false,false,false];
            this.isactive[index] = true;
        },
        // sendimage(e){
        //     let image = new Image();
        //     this.toBase64Url(e.target.src)
        //     console.log("base64",this.base64Image)
        //     image.src = e.target.src;
        //     image.width = e.target.width;
        //     image.height = e.target.height;
        //     this.$emit('showsample', image);
        // },
        sendimage(e){
            console.log(e)
            this.toBase64Url(e,this.send64image);
        },
        send64image(e,base64url){
            let image = new Image();
            image.src = base64url;
            image.width = e.target.width;
            image.height = e.target.height;
            this.$emit('showsample', image);
        }
    },

    computed:{
        imagesList:{
            get: function(){
            let k = this.task;
            let dir = this.imagesDir[k];
            return dir
        }
        }
    },
}
</script>
<style>
    .activestyle {
        @apply border-yellow-300 border-8;
    }
    

</style>