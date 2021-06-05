<template>
    <div>
        <h2>{{movie.title}}</h2>
        <p>{{movie.description}}</p>
        <div class="genres-container">
            <span v-for="genre in movie.genres" :key="genre.id" class="genre">{{genre.name}}</span>
        </div>
        <button type="button" class="collapsible" @click="open = !open">Rental Certificate</button>
        <div class="content" :class="[open ? 'display-block' : 'display-none']">
            <RentalCertificate v-if="isAdmin" :token="token" :movie="movie"/>
        </div>
        <div class="mb-2"></div>
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
import RentalCertificate from './RentalCertificate.vue'

export default ({
    name: "MovieDetails",
    components: {
        RentalCertificate
    },
    props: ['movie', 'token', 'isAdmin'],
    data() {
        return {
            stars: [0,1,2,3,4],
            highlighted: 4,
            open: false
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
    .genres-container {
        margin-bottom: 1.5rem;
    }
    .genre {
        padding: 0.5rem 0.2rem;
        border: 1px solid black;
    }
    .collapsible {
        background-color: rgb(124, 124, 124);
        color: white;
        cursor: pointer;
        padding: 18px;
        width: 100%;
        border: none;
        text-align: left;
        outline: none;
        font-size: 15px;
    }

    .active, .collapsible:hover {
        background-color: #555;
    }

    .content {
        padding: 0 18px;
        display: none;
        overflow: hidden;
        background-color: #f1f1f1;
    }

    .mb-2 {
        margin-bottom: 2rem;
    }

    .display-none {
        display: none;
    }

    .display-block {
        display: block;
    }
</style>
