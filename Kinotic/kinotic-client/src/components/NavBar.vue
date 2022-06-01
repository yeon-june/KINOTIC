<template>
  <div>
    <nav v-if="!isLoginPage && !isSignupPage && !is404" class="flex justify-between items-center w-full" id="nav-bar">
      <router-link to="/" class="h-full flex items-center">
      <img src="@/assets/kinoticLogo.png" alt="logo-img"  class="h-4/6">
      </router-link>
      <div>
        <span v-if="isLoggedIn" class="mr-4 leferi-base text-xs">🎫 {{current}} 님!</span>
        <a v-if="isAdmin" href="http://127.0.0.1:8000/admin/" class="leferi-base f-14 mr-3">Admin</a>
        <a v-if="!isLoggedIn" href="/signup" class="leferi-base f-14 mr-3" >Signup</a>
        <a :href="`/${inOrOut}`" class="leferi-base f-14 mr-1" >{{typo}}</a>
      </div>
    </nav>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
export default {
  name:'NavBar',
  data(){
    return{
      imgSrc: require('@/assets/kinoticLogo.png'),
    }
  },
  computed:{
    ...mapGetters(['admins']),
    current () {
      return localStorage.getItem('currentUser')
    },
    isAdmin (){
      return this.admins?.includes(this.current)
    },
    isLoggedIn (){
      return this.$store.getters.isLoggedIn
    },
    inOrOut (){
      return this.isLoggedIn ? 'logout':'login'
    },
    typo() {
      if (this.inOrOut === 'logout') {
        return 'Logout'
      } else{
        return 'Login'
      }
    }
  },
  props:{
    isLoginPage:{
      type: Boolean,
      required: true,
    },
    isSignupPage:{
      type: Boolean,
      required: true,
    },
    is404:{
      type: Boolean,
      required: true,
    },
  }
}
</script>

<style scoped>
@font-face {
    font-family: 'LeferiBaseType-RegularA';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2201-2@1.0/LeferiBaseType-RegularA.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

@font-face {
  font-family: 'EliceDigitalBaeum_Bold';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_220508@1.0/EliceDigitalBaeum_Bold.woff2') format('woff2');
  font-weight: 700;
  font-style: normal;
}
@font-face {
    font-family: 'EliceDigitalBaeum_Regular';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_220508@1.0/EliceDigitalBaeum_Regular.woff2') format('woff2');
    font-weight: 400;
    font-style: normal;
}

@font-face {
    font-family: 'paybooc-ExtraBold';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-07@1.0/paybooc-ExtraBold.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
.leferi-base{
  font-family: 'LeferiBaseType-RegularA';

}

.alice-Bold{
    font-family: 'EliceDigitalBaeum_Bold';

}
.alice-reg {
    font-family: 'EliceDigitalBaeum_Regular';
}

.bc-bold{
  font-family: 'paybooc-ExtraBold';
}


#nav-bar {
  height: 50px !important;
}

.f-12 {
  font-size: 12px !important;
}

.f-14 {
  font-size: 14px !important;
}

.f-16 {
  font-size: 16px !important;
}
</style>