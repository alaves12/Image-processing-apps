<template>
<div>
    <div @dragover.prevent="onDrag('over')"
         @dragleave="onDrag('leave')"
         @drop.stop="onDrop" v-show="!isShowInput" class="flex items-center justify-center">
         
         <label class="inputfile"
                :class="{inputfilebg:isDragOver}">
            <input type="file" name="file" ref="imageUploader" class="hidden" id="name1" @change="onChange"><p class="text-black text-center align-middle">ファイルをドロップ</p>
            <label for="name1" class="origin-center absolute bottom-10 bg-gray-200 hover:bg-gray-400 border border-gray-900 cursor-pointer h-9 px-1 w-auto sm:w-32 text-black rounded flex items-center justify-center">ファイル選択</label>
        </label>
    </div>
    <!-- <div  v-if="isShowInput==false"> -->
    <div  v-show="isShowInput" class="flex items-center justify-center">
         <div class="inputfile bg-white cursor-default hidden sm:flex">
            <div class="absolute flex items-start left-1/4">
                <img id='image' :src="image.src" :height="image.height" :width="image.width" class="transform -translate-x-1/2">
            </div>
            <div class="absolute left-3/4 flex flex-col items-center justify-center">
                <!-- <div class="lloader ease-linear rounded-full border-8 border-t-8 border-gray-200 h-20 w-20  transform -translate-x-1/2" v-show="isLoading"></div> -->
                <div v-show="isLoading" class=" transform -translate-x-1/2 flex flex-col items-center justify-center">
                <!-- <div class="animate-spin mr-3 rounded-full border-t-4 border-blue-500 h-20 w-20"></div> -->
                    <svg class="animate-spin origin-center -ml-1 mr-3 h-36 w-36 text-blue-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                    <div class="text-center text-xl text-blue-600 opacity-80">Processing</div>
                </div>
                <div v-show="!isLoading"> 
                <div class="py-3"><div class="bg-gray-200 hover:bg-gray-400 border border-gray-900 cursor-pointer h-9 w-32 text-black rounded flex items-center justify-center transform -translate-x-1/2" @click="reset"  v-show="isProcessbutton">リセット</div></div>
                <div class="bg-gray-200 hover:bg-gray-400 border border-gray-900 cursor-pointer h-9 w-32 text-black rounded flex items-center justify-center transform -translate-x-1/2" @click="sendimg()" v-show="isProcessbutton">処理</div>
                </div>
            </div>
            <img id="image-out" :src="outputImage.src" :height="outputImage.height" :width="outputImage.width" class="absolute left-3/4 flex transform -translate-x-1/2" v-show="isShowResult">
     
        </div>
        <div class="inputfile bg-white cursor-default sm:hidden h-180">
            <div class="absolute flex items-start top-1/4">
            <img id='image-sm' :src="image.src" :height="image.height" :width="image.width" class="transform -translate-y-1/2">
            </div>
            <img id="image-out-sm" :src="outputImage.src" :height="outputImage.height" :width="outputImage.width" class="absolute top-3/4 flex transform -translate-y-1/2" v-show="isShowResult">

            <div class="absolute top-3/4 block">
                <div v-show="isLoading" class=" transform -translate-y-1/2">
                <!-- <div class="animate-spin mr-3 rounded-full border-t-4 border-blue-500 h-20 w-20"></div> -->
                <svg class="animate-spin origin-center -ml-1 mr-3 h-36 w-36 text-blue-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                <div class="text-center text-blue-600 opacity-80">Processing</div>
                </div>
                <div class="py-3"><div class="bg-gray-200 hover:bg-gray-400 border border-gray-900 cursor-pointer h-9 w-32 text-black rounded flex items-center justify-center transform -translate-y-1/2" @click="reset" v-show="isProcessbutton">リセット</div></div>
                <div class="bg-gray-200 hover:bg-gray-400 border border-gray-900 cursor-pointer h-9 w-32 text-black rounded flex items-center justify-center transform -translate-y-1/2" @click="sendimg()" v-show="isProcessbutton">処理</div>
            </div>
        </div>
    </div>
    <div class="py-3 flex items-center justify-center"  v-show="isShowResult">
        <div class="bg-gray-200 hover:bg-gray-400 border border-gray-900 cursor-pointer h-9 w-32 text-black rounded flex items-center justify-center" @click="reset()">結果をリセット</div>
        <MylistButton :image="outputImage" @click="showSavemodal=true" @showisLogin="isLogin=$event"></MylistButton>
    </div>
    <div v-if="showSavemodal" tabindex="0"
            class="z-40  left-0 top-0 bottom-0 right-0 w-full h-full fixed">
            <div v-click-away="ClickAway" class="z-50 relative p-3 mx-auto my-0 max-w-full" style="width: 500px;" id="modal">
                <div class="bg-white rounded shadow-lg border flex flex-col overflow-hidden px-10 py-10">
                    <span v-if="isLogin" class="text-xl text-gray-800 font-semibold">保存しました</span>
                    <span v-else class="text-xl text-red-600 font-semibold">ログインしてください</span>
            </div>
        </div>
        <div class="z-40 overflow-auto left-0 top-0 bottom-0 right-0 w-full h-full fixed bg-opacity-50"></div>
    </div>
</div>
</template>
<script>
import axios from 'axios';
import MylistButton from '@/components/MylistButton.vue';
axios.defaults.withCredentials = true;
export default {
    name:"ImageForm",
    props:{
      sample:Object,
      formcolor:String
    },
    components: {
        MylistButton,
    },

    data() {
        return {
        isDragOver: false,
        isShowInput: false,
        isShowResult: false,
        isLoading:false,
        isProcessbutton:false,
        errorMessage:"",
        image:{},
        width: window.innerWidth,
        height: window.innerHeight,
        ratio:0,
        output:"",
        outputImage:{},
        showSavemodal:false,
        tweetImage:{},
        inputImage:{},
        user:{},
        isLogin:true
        };
    },
    methods: {
        createJpegFile4Base64(base64, name) {
            // base64のデコード
            let bin = atob(base64.replace(/^.*,/, ''));
            // バイナリデータ化
            let buffer = new Uint8Array(bin.length);
            for (let i = 0; i < bin.length; i++) {
                buffer[i] = bin.charCodeAt(i);
            }
            // ファイルオブジェクト生成(この例ではjpegファイル)
            return new File([buffer.buffer], name, {type: "image/jpeg"});
        },
        sendimg(){
            this.isProcessbutton = false;
            this.isLoading = true;
            axios.defaults.xsrfCookieName = 'csrftoken';
            axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
            let file = this.createJpegFile4Base64(this.image.src, "img");
            console.log(file);
            let formData = new FormData();
            formData.append('yourFile',file);
            // console.log(this.image.src)
            // let data = {image:this.image.src}

            axios.post('https://mysterious-savannah-67626.herokuapp.com/upload', formData).then(res => {
                let insrc = res.data.result[0][0];
                let outsrc = res.data.result[0][1];
                this.tweetImage = {'input':insrc,'output':outsrc}
                const prefix = 'data:image/jpg;base64,';
                this.output = prefix+outsrc;
                let image = new Image();
                image.src = this.output;
                image.width = this.image.width;
                image.height = this.image.width * (1/this.ratio)
                this.outputImage = image;
                this.isLoading = false;
                this.isShowResult = true;
                console.log("output", this.outputImage.width, this.outputImage.height)

            }).catch(e => {
                console.log(axios.defaults.headers)
                console.log(e);
            })
        },
        sendmsg(){
            axios.defaults.headers.post['Content-Type'] = 'application/json';
            console.log(axios.defaults.headers)
            axios.post('http://localhost:8000/res/', {"access_key": "hoge"},).then(res => {
                console.log(res);
            }).catch(e => {
                console.log(e);
            })
        },
        onDrag(type) {
            this.isDragOver = type === "over";
        },
        onDrop(event) {
            event.preventDefault();
            this.isDragOver = false;
            const files = event.dataTransfer.files;
            if (files.length !== 1 || files[0].type.indexOf("image") !== 0) {
                alert("ファイルが複数選択されているか、画像ファイルが選択されていません");
                return;
            }
           
            this.readImage(files[0]);
            this.isShowInput = true;
            this.isProcessbutton = true;

        },
        onChange(event) {
            const files = event.target.files;
            if (files.length !== 1 || files[0].type.indexOf("image") !== 0) {
                alert("ファイルが複数選択されているか、画像ファイルが選択されていません");
                // this.errorMessage="ファイルが複数選択されているか、画像ファイルが選択されていません";
                return;
            }
           
            this.readImage(files[0]);
            this.isShowInput = true;
            this.isProcessbutton = true;
        },
        readImage(file) {
            this.ratio = 0
            let reader = new FileReader();
            reader.onload = this.loadImage;
            reader.readAsDataURL(file);
        },
        loadImage(e) {
            let image = new Image();
            image.src = e.target.result;
            image.onload = this.getinputsize;
            // this.image = image;
        },
        getinputsize(e){
            let image =  new Image();
            image.src = e.target.src ;
            image.width = e.target.naturalWidth;
            image.height = e.target.naturalHeight;
            this.image = image;
            console.log(this.image,"loadedimage")
        },
        removeImage() {
            this.$refs.imageUploader.value = '';
        },
        reset() {
            this.isShowInput=false;
            this.isProcessbutton = false;
            this.removeImage();
            this.isShowResult=false;
        },
        ClickAway(){
            console.log(this.showSavemodal)
            if(this.showSavemodal==true){
                this.showSavemodal = false;
            }
        },
        draw() {
            this.width = window.innerWidth;
            this.height = window.innerHeight;
            let id = 'image';
            let id_out = 'image-out';
            let id_sm = 'image-sm';
            let id_out_sm = 'image-out-sm';
            let img = document.getElementById(id);
            let img_out = document.getElementById(id_out);
            console.log(id,"id")
            console.log(img,"img_tag")
            let s_w = 0
            if (this.width > 639){
                s_w = this.width * 5/12
            } else {
                s_w = this.width * 10/12
                img = document.getElementById(id_sm);
                img_out = document.getElementById(id_out_sm);
            }
            let w = this.image.width;
            let h = this.image.height;
            
            if (this.ratio == 0){
                this.ratio = w/h
            }
            h = 300;
            w = this.ratio*h;
            if (w>(s_w - 50) && (s_w - 50)*(1/this.ratio) <= 300){
                w = s_w - 50;
                h = w*(1/this.ratio);
            }
            this.image.width = w;
            this.image.height = h;
            console.log(w, h, this.ratio);
            img.height = h;
            console.log(h,"height")
            img.width = w;
            img.height = h;
            img_out.width = w;
            img_out.height = h;

            // console.log('\n')
            },
            showimgtag() {
            let img = document.getElementById('image');
            console.log(img, this.isShowInput);
        }
        },
        
        mounted: function () {
            window.addEventListener('resize', this.draw)
            window.addEventListener('resize', this.draw)
        },
        beforeUnmount: function () {
            window.removeEventListener('resize', this.draw)
            window.removeEventListener('resize', this.draw)
        },
        watch: {
            image() {
                // this.image = newValue;
                this.draw();
            },
            sample(newValue, oldValue) {
                
                if (oldValue.src!=newValue.src){this.isShowResult = false;}
                if (this.isLoading==false){
                    this.ratio = 0;
                    this.isShowInput = true;
                    this.isProcessbutton = true;
                    this.image = newValue;
                }
            },
            output() {
                this.draw()
            }
    }
}
</script>

<style>
    .loader {
    border-top-color: #3498db;
    -webkit-animation: spinner 1.5s linear infinite;
    animation: spinner 1.5s linear infinite;
    }

    @-webkit-keyframes spinner {
    0% { -webkit-transform: rotate(0deg); }
    100% { -webkit-transform: rotate(360deg); }
    }

    @keyframes spinner {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
    }

    .inputfile {
        @apply container relative flex w-80 h-80 border-dotted border-black border-2 bg-blue-200 text-white font-bold py-2 px-4 cursor-pointer rounded items-center justify-center;
    }
    @screen sm{
        .inputfile {
            @apply container relative flex w-268 h-80 border-dotted border-black border-2 bg-blue-200 text-white font-bold py-2 px-4 cursor-pointer rounded items-center justify-center;
        }
    }
    .inputfilebg{
        @apply bg-blue-300;
    }
    
        

</style>