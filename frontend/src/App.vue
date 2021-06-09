<template>
<div>
  <Navbar></Navbar>
  <div class="p-10">
  </div>
  <div class="">
    <router-view/>
  </div>
</div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
export default {
  components:{
    Navbar
  },
  methods : {
    createTitleDesc : function(routeInstance){
         // タイトルを設定
        if(routeInstance.meta.title){
            var setTitle = routeInstance.meta.title + ' | 完全無料でできるディープラーニングを用いた画像処理アプリ';
            document.title = setTitle;
        } else {
            document.title = 'title is not set'
        }

        // メタタグdescription設定
        if(routeInstance.meta.desc){
            var setDesc = routeInstance.meta.desc + ' | 屋外で撮影した写真が逆光や霧によって劣化してしまったことはありませんか？　そういった画像をディープラーニングを用いて画像処理を行い綺麗にします';
            document.querySelector("meta[name='description']").setAttribute('content', setDesc)
        } else {
            document.querySelector("meta[name='description']").setAttribute('content', 'description is not set')
        }
    } 
  },
  mounted : function(){
      var routeInstance = this.$route;
      this.createTitleDesc(routeInstance);
  },
  watch: { 
      '$route' (routeInstance) {
          this.createTitleDesc(routeInstance);
      }
  }
}
</script>
