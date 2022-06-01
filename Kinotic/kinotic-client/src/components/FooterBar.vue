<template>
    <nav v-if="!isLoginPage && !isSignupPage && !is404" class="flex justify-between items-strech w-full" :class="active" @click.prevent>
      <router-link to="/" class="w-1/5 flex justify-center items-center home">
        <div class="flex flex-col items-center justify-center w-full h-full" @click="makeActive('home')">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 f-4d4d" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.7">
    <path stroke-linecap="round" stroke-linejoin="round" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
  </svg>
          <span class="text-xs alice-reg f-4d4d">홈</span>
        </div>
      </router-link>  
      <router-link to="/explore" class="w-1/5 flex justify-center items-center explore">
        <div class="flex flex-col items-center justify-center w-full h-full"  @click="makeActive('explore')">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 f-4d4d" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.7">
  <path stroke-linecap="round" stroke-linejoin="round" d="M5 8h14M5 8a2 2 0 110-4h14a2 2 0 110 4M5 8v10a2 2 0 002 2h10a2 2 0 002-2V8m-9 4h4" />
</svg>
          <span class="text-xs alice-reg f-4d4d">탐색</span>
        </div>
      </router-link>
      <router-link to="/recommend" class="w-1/5 flex justify-center items-center recommend">
        <div class="flex flex-col items-center justify-center w-full h-full"  @click="makeActive('recommend')">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 f-4d4d" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.7">
  <path stroke-linecap="round" stroke-linejoin="round" d="M7 4v16M17 4v16M3 8h4m10 0h4M3 12h18M3 16h4m10 0h4M4 20h16a1 1 0 001-1V5a1 1 0 00-1-1H4a1 1 0 00-1 1v14a1 1 0 001 1z" />
</svg>
          <span class="text-xs alice-reg f-4d4d" >추천</span>
        </div>
      </router-link>
      <router-link to="/community" class="w-1/5 flex justify-center items-center community">
        <div class="flex flex-col items-center justify-center w-full h-full" @click="makeActive('community')">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 f-4d4d" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.7">
  <path stroke-linecap="round" stroke-linejoin="round" d="M17 8h2a2 2 0 012 2v6a2 2 0 01-2 2h-2v4l-4-4H9a1.994 1.994 0 01-1.414-.586m0 0L11 14h4a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2v4l.586-.586z" />
</svg>
          <span class="text-xs alice-reg f-4d4d">커뮤니티</span>
        </div>
      </router-link>
      <router-link :to="{ name: 'mypage', params: { username } }" class="w-1/5 flex justify-center items-center mypage">
        <div class="flex flex-col items-center justify-center w-full h-full" @click="makeActive('mypage')">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 f-4d4d" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.7">
  <path stroke-linecap="round" stroke-linejoin="round" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
</svg>
          <span class="text-xs alice-reg f-4d4d">마이페이지</span>
        </div>
      </router-link>
    </nav>
</template>

<script>
export default {
  name:'FooterBar',
  data(){
    return{
      active: '',
    }
  },
  computed:{
    isLoggedIn (){
      return this.$store.getters.isLoggedIn
    },
    inOrOut (){
      return this.isLoggedIn ? 'logout':'login'
    },
    username (){
      return localStorage.getItem('currentUser')
    },
  },
  methods:{
    makeActive(item){
      this.active = item
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
  },
  created(){
    if(document.location.pathname === '/') {
      this.active='home'
    } else if(document.location.pathname === '/recommend'){
      this.active='recommend'
    } else if(document.location.pathname === '/explore'){
      this.active='explore'
    } else if(document.location.pathname === '/community'){
      this.active='community'
    } else if(document.location.pathname === '/mypage/'+localStorage.getItem('currentUser')){
      this.active='mypage'
    } else{
      this.active=''
    }
  }

}
</script>

<style scoped>
@font-face {
    font-family: 'yg-jalnan';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_four@1.2/JalnanOTF00.woff') format('woff');
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
.alice-Bold{
    font-family: 'EliceDigitalBaeum_Bold';

}
.alice-reg {
    font-family: 'EliceDigitalBaeum_Regular';
}
.jalnan {
    font-family: 'yg-jalnan';
}

.f-4d4d{
  color: #4d4d4d;;
}

.onPage{
  background-color: #ffdd81;
  box-shadow: rgba(0, 0, 0, 0.06) 0px 2px 4px 0px inset;
}

.onPageFont{
  font-weight:800;
}

nav.home .home,
nav.explore .explore,
nav.recommend .recommend,
nav.community .community,
nav.mypage .mypage{
  background-color:#fce389;
  box-shadow: rgba(0, 0, 0, 0.06) 0px 2px 4px 0px inset;
}

</style>