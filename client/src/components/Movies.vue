<template>
    <div class="layout">
        <div>
            <MovieItem 
                v-for="movie in movies" 
                :key="movie.id"
                :movie="movie"
                @movie-selected="movieSelected($event)"
                @movie-delete="movieDelete($event)"
                @movie-edit="movieEdit($event)"
            />
            <button @click="addNewMovie()">New Movie</button>
        </div>
        <MovieDetails v-if="selectedMovie" :movie="selectedMovie" @updated="updated()"/>
        <MovieEdit v-if="editedMovie" :movie="editedMovie" @updated="updated()"/>
    </div>
</template>

<script>
import MovieItem from './MovieItem'
import MovieDetails from './MovieDetails'
import MovieEdit from './MovieEdit'

export default ({
    name: "Movies",
    components: { 
        MovieItem,
        MovieDetails,
        MovieEdit
    },
    data() {
        return {
            movies: [],
            selectedMovie: null,
            editedMovie: null,
        }
    },
    methods: {
        movieSelected(movieId) {
            this.editedMovie = null;
            this.selectedMovie = this.movies.find(movie => movie.id === movieId);
        },
        movieDelete(movieId) {
            fetch(`http://127.0.0.1:8000/core/movies/${movieId}/rate_movie/`, {
                method: 'delete',
                headers: {
                    'content-type': 'application/json'
                }
            })
            .then(() => this.movies = this.movies.filter(movie => movie.id !== movieId))
            .catch(error => console.log(error))
        },
        movieEdit(movieId) {
            this.selectedMovie = null;
            this.editedMovie = this.movies.find(movie => movie.id === movieId);
        },
        addNewMovie() {
            this.selectedMovie = null;
            this.editedMovie = {title: '', description: ''};
        },
        updated() {
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