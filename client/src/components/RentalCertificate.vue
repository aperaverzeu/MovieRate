<template>
    <div v-if="certificate && certificate.number">
        <h4>Rental Certificate: </h4>
        <p>Number: {{certificate.number}}</p>
        <p>Country: {{certificate.country}}</p>
        <button>Update Certificate</button>
    </div>
    <div v-else>
        <p>No rental certificate</p>
        <button>Add Certificate</button>
    </div>
</template>

<script>
export default ({
    name: "Movies",
    props: ['movie', 'token'],
    data() {
        return {
            certificate: null
        }
    }, 
    methods: {
        getCertificate() {
            if (this.movie.id) {
                fetch(`http://127.0.0.1:8000/core/rental_certificates/${this.movie.id}/`, {
                    method: 'get',
                    headers: {
                        'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
                        'authorization': `Token ${this.token}`
                        }
                })
                .then(certificate => certificate.json())
                .then(certificate => {
                    this.certificate = certificate;
                })
                .catch(error => {
                    this.certificate = null;
                    console.log(error);
                })
            }
            
        }
    },
    watch: { 
        movie: function(newValue, oldValue) {
            if (newValue !== oldValue) {
                this.getCertificate()
            }
        }
    },
    created() {
        this.getCertificate()
    }
})
</script>
