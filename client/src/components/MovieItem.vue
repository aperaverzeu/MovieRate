<template>
    <div>
        <h2 @click="$emit('movie-selected', movie.id)">{{movie.title}}</h2>
    </div>
</template>

<script>
export default ({
    name: "MovieItem",
    props: ['movie']
})
</script>

<style scoped>
    h2 {
        cursor: pointer;
    }
</style>
