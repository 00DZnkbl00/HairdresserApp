<template>
<div>
        <header class="shadow-sm bg-white">
            <nav class="container mx-auto p-4 flex justify-between">
                <Nuxt-link to="/" class="font-bold" >Nuxt HAIR</Nuxt-link>
                <ul class="flex gap-4">
                    <li><NuxtLink to="/" class="btn">Home</NuxtLink></li>
                    <li><NuxtLink to="/about" class="btn">About</NuxtLink></li>
                </ul>
            </nav>
        </header>
        <div class="container mx-auto p-4">
            <slot/>
        </div>
    </div>
</template>

<style scoped>
.router-link-exact-active{
    color: rgba(240, 183, 13, 0.9);
}
</style>