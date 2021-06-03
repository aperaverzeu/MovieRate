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
    props: ['movie', 'token'],
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
            if (this.movie.id) {
                fetch(`http://127.0.0.1:8000/core/movies/${this.movie.id}/`, {
                    method: 'put',
                    headers: {
                        'Content-Type' : 'application/json',
                        'authorization': `Token ${this.token}`
                    },
                    body: JSON.stringify({title: this.localMovie.title, 
                                          description: this.localMovie.description, 
                                          genre: this.localMovie.genre}) 
                    
                })
                .then(res => res.json())
                .then(res => {
                    this.$emit('updated');
                    console.log(res);
                })
                .catch(error => console.log(error))
            } else {
                fetch(`http://127.0.0.1:8000/core/movies/`, {
                    method: 'post',
                    headers: {
                        'Content-Type' : 'application/json',
                        'authorization': `Token ${this.token}`
                    },
                    body: JSON.stringify({title: this.localMovie.title, 
                                          description: this.localMovie.description, 
                                          genre: [1]}) 
                    
                })
                .then(res => res.json())
                .then(res => {
                    this.$emit('updated');
                    console.log(res);
                })
                .catch(error => console.log(error))
            }
        }
    }
})
</script>
