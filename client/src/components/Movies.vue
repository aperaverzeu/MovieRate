<template>
    <div class="layout">
        <div>
            <h4 v-for="movie in movies" :key="movie">{{movie}}</h4>
        </div>
        <h3>Movie Details</h3>
    </div>
</template>

<script>
export default ({
    name: "Movies",
    data() {
        return {
            movies: []
        }
    },
    created() {
        fetch('http://127.0.0.1:8000/core/movies/', {
            method: 'GET',
            headers: {
                'Authotization': 'Token b68e3fbe50dfd520a001accce477608677f5df28'
            }
        })
        .then(movies => movies.json())
        .then(movies => this.movies = movies)
        .catch(error => console.log(error))
    }
})
</script>

<style scoped>
    .layout {
        display: grid;
        grid-template-columns: 1fr 1fr;
    }
</style>