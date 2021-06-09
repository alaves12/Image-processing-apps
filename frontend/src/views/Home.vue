<template>
  <div class="flex flex-wrap flex-row">
    <div class="w-1/12"></div>
    <div class="w-10/12 flex flex-col items-center justify-center">
      <div class="text-gray-800 text-3xl font-bold">画像処理アプリ</div>
      <div class="text-gray-600 text-2xl font-semibold py-5">使用したい機能をクリックしてください</div>
      <router-link to="/dehaze"><TaskCard task="dehaze" title="霧除去" discription="霧がかった画像から霧を除去することが出来ます。"></TaskCard></router-link>
    </div>
    <div class="w-1/12"></div>
  </div>
</template>

<script>
// @ is an alias to /src
import TaskCard from '@/components/TaskCard.vue'
export default {
  name: 'Home',
  components: {
    TaskCard
  }
}
</script>