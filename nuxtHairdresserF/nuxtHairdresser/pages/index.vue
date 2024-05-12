<template>
    <Navbar/>
    <div>
        <h2>Home</h2>
        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Nemo ad officiis fugit fuga recusandae dicta dolor nobis cupiditate. Magni dicta excepturi odit perferendis maxime voluptates id, distinctio eligendi eveniet laboriosam.</p>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta repellendus minima molestiae suscipit tenetur voluptate, veniam dolorum quaerat accusamus ex dolore quisquam officia voluptatem nulla quod sequi eum velit qui!</p>
    </div>
    <div :style="{ backgroundImage: 'url(\'hairdressing-equipment-with-copy-space.jpg\')'}"></div>
</template>

<script setup>
import navbar from '~/components/navbar.vue';
</script>
<style  scoped>

h2{
    margin-bottom: 20px;
    font-size: 36px;
}
p{
    margin: 20px 0;

}
</style>