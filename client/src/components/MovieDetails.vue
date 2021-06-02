<template>
    <div v-if="movie">
        <h2>{{movie.title}}</h2>
        <p>{{movie.description}}</p>
    </div>
</template>

<script>
export default ({
    name: "MovieDetails",
    props: ['movie']
})
</script>

<style scoped>
    h2 {
        cursor: pointer;
    }
</style>
