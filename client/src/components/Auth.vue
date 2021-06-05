<template>
    <div>
        <label for="username">Username</label><br/>
        <input type="text" placeholder="username" id="username" v-model="username"><br/>
        <label for="password">Password</label><br/>
        <input type="password" placeholder="password" id="password" v-model="password"><br/>
        <button @click="login()" v-if="loginMode">Login</button>
        <button @click="register()" v-else>Register</button>

        <p @click="loginMode = false" v-if="loginMode">Don't have an account? Register here</p>
        <p @click="loginMode = true" v-else>You already have an account. Login here</p>
    </div>
</template>

<script>
export default ({
    name: 'Auth',
    data() {
        return {
            username: '',
            password: '',
            token: '',
            loginMode: true
        }
    },
    methods: {
        login() {
          fetch(`http://127.0.0.1:8000/auth/`, {
                method: 'post',
                headers: {
                    'content-type': 'application/json'
                },
                body: JSON.stringify({username: this.username, password: this.password}) 
            })
            .then(res => res.json())
            .then(res => {
                this.token = res.token;
                this.$cookie.set('auth-token', this.token, { expires: '1M' });
                this.$router.push("/");
            })
            .catch(error => console.log(error))
        },
        register() {
            console.log(this.password, this.username)
            fetch(`http://127.0.0.1:8000/core/users/`, {
                method: 'post',
                headers: {
                    'content-type': 'application/json'
                },
                body: JSON.stringify({username: this.username, password: this.password}) 
            })
            .then(() => {
                this.login()
            })
            .catch(error => console.log(error))
        }
    },
    created() {
        if (this.$cookie.get("auth-token")) {
            this.$router.push("/")
        }
    },
})
</script>



<style scoped>
    p {
        cursor: pointer;
    }
</style>
