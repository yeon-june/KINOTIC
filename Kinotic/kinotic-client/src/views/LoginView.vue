<template>
  <div class="flex flex-col justify-center items-center w-full" id="wrap">
    <div class="center flex flex-col items-center justify-center">
    <img src="@/assets/Login.png" alt="signup img" id="signup-img" class="mb-8">

    <account-error-list v-if="authError"></account-error-list>


    <form @submit.prevent="login(loginCredentials)" id="signup-form" class="flex flex-col justify-center items-center">
      <div id="input-div" >
        <label for="username">Username</label> <br>
        <input  v-model="loginCredentials.username" type="text" id="username" class="px-2" required/>
      </div>
      <div id="input-div" class="mt-6 mb-7">
        <label for="password1">Password</label> <br>
        <input v-model="loginCredentials.password" type="password" id="password1" class="px-2" required />
      </div>

      <button>Submit</button>
    </form>
    <!-- <div @click="openNew">여기</div> -->
    <div class="flex items-end justify-end mt-2">
      <a href="/" class="mr-3">HOME</a>
      <a href="/signup">SIGNUP</a>
    </div>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        loginCredentials: {
          username: '',
          password: '',
        }
      }
    },
  computed: {
      ...mapGetters(['authError', 'isLoggedIn'])
    },
  methods: {
    ...mapActions(['login']),
    // openNew() {
    //   window.open('http://localhost:8000/api/v1/accounts/password_reset/')
    // }
  },
  created(){
    console.log(document.referrer)
    if (this.isLoggedIn) {
      document.location.href = "/"
    }
  }
  }
</script>

<style scoped>
#full-screen{
  height:100vh;
}

#signup-img{
  width:25%;
}

#signup-form{
  width:70%;
  height:40vh;
  min-height: 250px;
  max-height: 400px;
  background-color: #FFF2BF;
  border-radius: 20px;
}

#input-div{
  width:80%;
}
#wrap {
  display: grid;
  place-items: center;
  min-height: 90vh;
}

input{
  width: 100% !important;
  height: 7vh;
  min-height: 35px;
  max-height: 45px;
  border-radius: 10px;
  background-color:white;
}

button{
  height:45px;
  background-color: #BCA7D2 !important;
  width:25%;
  border-radius:10px;
  color:white !important;
}
</style>
