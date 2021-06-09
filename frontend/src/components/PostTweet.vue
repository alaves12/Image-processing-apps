<template>
    <div>
        <button @click="twitterShare" class="bg-blue-500 hover:bg-blue-400 text-white text-base px-2 py-1 rounded flex items-center justify-center">ツイッターでシェアする</button>
    </div>
</template>

<script>
import axios from 'axios';
import functions  from 'firebase'
export default {
  name:"PostTweet",
  // props(){
  //     return{image:{
  //             type:Array,
  //             required:false
  //           }}
  // },
  props:['image'],
  methods:{
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
    twitterShare(){
      axios.defaults.xsrfCookieName = 'csrftoken';
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
      let inputfile = this.createJpegFile4Base64(this.image.input, "input");
      let outputfile = this.createJpegFile4Base64(this.image.output, "output")
      let formData = new FormData();
      formData.append('files',inputfile);
      formData.append('files',outputfile);

      axios.post('http://localhost:8000/twitter', formData).then(res => {
        console.log(res.data.url)

        }).catch(e => {
            console.log(axios.defaults.headers)
            console.log(e);
      });
      const tweet = functions.httpsCallable('note')
      tweet(formData).then(result => {
        console.log(result);
      }).catch(err=>{
        console.log(err)
      });

    },


  }
}
</script>
