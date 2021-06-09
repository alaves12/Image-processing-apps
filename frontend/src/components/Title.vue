<template>
    <div>
        <div class="text-3xl text-black font-bold text-center">
            {{name}}
        </div>
        <div class="p-5 text-xl text-black text-center">
            {{discription}}
        </div>
    </div>
</template>
<script>
export default {
    name:'Tilte',
    props:{
        name:String,
        discription:String
    }
}
</script>