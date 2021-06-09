<template>
  <div>
    <Processing title="霧除去" discription="霧がかった画像から霧を除去することが出来ます。" task="dehaze"></Processing>
  </div>
</template>

<script>
// @ is an alias to /src
import Processing from '@/components/Processing.vue'
export default {
  name: 'Dehaze',
  components: {
    Processing
  }
}
</script>