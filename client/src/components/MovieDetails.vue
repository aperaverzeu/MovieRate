<template>
    <div>
        <h2>{{movie.title}}</h2>
        <p>{{movie.description}}</p>
        <font-awesome-icon icon="star" :class="[movie.average_rating > 0 ? 'orange' : '']"/>
        <font-awesome-icon icon="star" :class="[movie.average_rating > 1 ? 'orange' : '']"/>
        <font-awesome-icon icon="star" :class="[movie.average_rating > 2 ? 'orange' : '']"/>
        <font-awesome-icon icon="star" :class="[movie.average_rating > 3 ? 'orange' : '']"/>
        <font-awesome-icon icon="star" :class="[movie.average_rating > 4 ? 'orange' : '']"/>
        ({{movie.ratings_amount}})

        <hr>
        <h2>Rate it!</h2>
        <font-awesome-icon icon="star" class="bigger"
            v-for=" star in stars" :key="star"
            :class="[highlighted > star - 1 ? 'purple' : '']"
            @mouseenter="highlighted = star"
            @mouseleave="highlighted = -1"
            @click="ratingSelected(star)"
        />
    </div>
</template>

<script>
export default ({
    name: "MovieDetails",
    props: ['movie', 'token'],
    data() {
        return {
            stars: [0,1,2,3,4],
            highlighted: 4
        }
    },
    methods: {
        ratingSelected(rate) {
            fetch(`http://127.0.0.1:8000/core/movies/${this.movie.id}/rate_movie/`, {
            method: 'post',
            headers: {
                'Content-Type' : 'application/json',
                'authorization': `Token ${this.token}`
            },
            body: JSON.stringify({stars: rate + 1})
        })
        .then(res => res.json())
        .then(res => {
            this.$emit('updated');
            console.log(res);
        })
        .catch(error => console.log(error))
        },
    }
})
</script>

<style scoped>
    h2 {
        cursor: pointer;
    }
    .orange {
        color: orange;
    }
    .purple {
        color: purple;
    }
    .bigger {
        font-size: 2rem;
    }
</style>
