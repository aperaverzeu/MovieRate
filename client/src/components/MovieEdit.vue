<template>
    <div>
        <label for="title">Title</label><br/>
        <input type="text" placeholder="title" id="title" v-model="localMovie.title"><br/>
        <label for="description">Description</label><br/>
        <textarea id="description" placeholder="description" v-model="localMovie.description"></textarea><br/>
        <button @click="saveMovie()">Save Movie</button>
    </div>
</template>

<script>

export default ({
    name: "MovieEdit",
    props: ['movie'],
    data() {
        return {
            localMovie: {...this.movie}
        } 
    },
    watch: {
        movie: function(newValue, oldValue) {
            if (newValue !== oldValue) {
                this.localMovie = {...this.movie}
            }
        }
    },
    methods: {
        saveMovie() {
            fetch(`http://127.0.0.1:8000/core/movies/${this.movie.id}/rate_movie/`, {
                method: 'put',
                headers: {
                    'content-type': 'application/json'
                },
                body: JSON.stringify({title: this.localMovie.title, description: this.localMovie.description}) 
                
            })
            .then(resp => resp.json())
            .then(resp => {
                this.$emit('updated');
                console.log(resp);
            })
            .catch(error => console.log(error))
        }
    }
})
</script>
