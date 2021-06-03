<template>
    <div>
        <label for="username">Title</label><br/>
        <input type="text" placeholder="username" id="username" v-model="username"><br/>
        <label for="password">Description</label><br/>
        <input type="password" placeholder="password" id="password" v-model="password"><br/>
        <button @click="login()">Login</button>
    </div>
</template>

<script>
export default {
  name: 'Auth',
  data() {
      return {
          username: '',
          password: ''
      }
  },
  created() {
      if (this.$cookie.get("auth-token")) {
          this.$router.push("/")
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
                let token = res.token;
                this.$cookie.set('auth-token', token, { expires: '1M' });
                this.$router.push("/")
            })
            .catch(error => console.log(error))
      }
  }
}
</script>
