<template>
    <div class="layout">
        <div>
            <MovieItem 
                v-for="movie in movies" 
                :key="movie.id"
                :movie="movie"
                @movie-selected="movieSelected($event)"
            />
        </div>
        <MovieDetails :movie="selectedMovie" @rated="rated()"/>
    </div>
</template>

<script>
import MovieItem from './MovieItem'
import MovieDetails from './MovieDetails'

export default ({
    name: "Movies",
    components: { 
        MovieItem,
        MovieDetails
    },
    data() {
        return {
            movies: [],
            selectedMovie: null
        }
    },
    methods: {
        movieSelected(movieId) {
            this.selectedMovie = this.movies.find(movie => movie.id === movieId);
        },
        rated() {
            this.getMovies()
        },
        getMovies() {
            fetch('http://127.0.0.1:8000/core/movies/', {
                method: 'get',
                headers: {
                    'content-type': 'application/json'
                }
            })
            .then(movies => movies.json())
            .then(movies => {
                this.movies = movies;
                if (this.selectedMovie) {
                    this.selectedMovie = this.movies.find(movie => movie.id === this.selectedMovie.id);
                }
            })
            .catch(error => console.log(error))
        }
    },
    created() {
        this.getMovies()
    },
})
</script>

<style scoped>
    .layout {
        display: grid;
        grid-template-columns: 1fr 1fr;
    }
</style>