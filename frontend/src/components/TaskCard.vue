<template>
    <div class="p-5 max-w-sm mx-auto rounded-xl shadow-md flex items-center justify-center space-x-4" :class="{dehze:taskclass.dehaze}">
    <div class="flex-shrink-0">
    </div>
    <div>
        <div class="text-center pb-2 text-xl font-medium text-black">{{title}}</div>
        <p class="text-gray-500">{{discription}}</p>
    </div>
    </div>
</template>
<script>
export default {
    name:'TaskCard',
    props:["title","discription"],
    data(){
        return {
            taskclass:{
            dehaze: true,
            backlight: false,
        }
        }
    }
}
</script>
<style>
    .dehze {
        @apply bg-indigo-200;
    }
</style>