<template>
    
    <div class="h-screen flex flex-wrap flex-row">
    <div class="w-1/12"></div>
    <div class="w-10/12 text-center">
    <Title :name="title" :discription="discription"></Title>
    <ImageForm :sample="image"></ImageForm>
    <SampleImages :task="task" @showsample="image=$event"></SampleImages>
    </div>
    <div class="w-1/12"></div>
    </div>

</template>
<script>
import Title from '@/components/Title.vue'
import ImageForm from '@/components/ImageForm.vue'
import SampleImages from '@/components/SampleImages.vue'
export default {
    name:'Processing',
    props:{
        title:String,
        discription:String,
        task:String
    },
    data() {
        return {
            image : {},
        }
    },
    components:{
        Title,
        ImageForm,
        SampleImages
    }
}
</script>