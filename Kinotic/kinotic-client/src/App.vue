<template>
  <div class="my-container mx-auto" id="containter">
    <NavBar :isLoginPage="isLoginPage" :isSignupPage="isSignupPage" :is404="is404" class="my-2"/>
    <router-view :key="$route.fullPath"/>
    <div id="blank"></div>
    <FooterBar :isLoginPage="isLoginPage" :isSignupPage="isSignupPage" :is404="is404" 
    class="footerbar"
    :class="{'footerbar--hidden':!showFooterBar}"
    id="footer-bar" 
    />
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import FooterBar from '@/components/FooterBar.vue'
import {mapActions} from 'vuex'

export default {
  name:'App',
  components: {
    NavBar,
    FooterBar,
  },
  data(){
    return{
      showFooterBar: true,
      lastScrollPostition:0,
      componentKey: 0,
    }
  },
  computed: {
    isLoginPage (){
      return document.location.pathname === '/login'
    },
    isSignupPage (){
      return document.location.pathname === '/signup'
    },
    is404 (){
      return document.location.pathname === '/404'
    },
  },
  methods:{
    ...mapActions(['fetchMovies']),
    onScroll () { 
      // Get the current scroll position 
      const currentScrollPosition = window.pageYOffset || document.documentElement.scrollTop 
      // Because of momentum scrolling on mobiles, we shouldn't continue if it is less than zero 
      if (currentScrollPosition <= 0)

      if (Math.abs(currentScrollPosition - this.lastScrollPosition) < 15)  { return }
      // Here we determine whether we need to show or hide the navbar 
      this.showFooterBar = currentScrollPosition < this.lastScrollPosition 
      // Set the current scroll position as the last scroll position 
      this.lastScrollPosition = currentScrollPosition 

    },
    reRender(){
      this.componentKey += 1
    }
  },
  watch: {
    $route(to, from) {
    if (to.path !== from.path) {
      this.reRender()
      console.log(this.componentKey)
     }
    },
  },

  created(){
    this.fetchMovies()
  },
  mounted () { 
    window.addEventListener('scroll', this.onScroll) 
  }, 
  beforeDestroy () { 
    window.removeEventListener('scroll', this.onScroll) 
  },

}
</script>

<style scoped>
.my-container {
  width: 800px !important;
}

#footer-bar {
  position:fixed;
  width:800px !important;
  bottom:0;
  height:60px !important;
  background: #ffeeac;
  box-shadow: rgba(17, 17, 26, 0.1) 0px 0px 16px;
}

#blank{
  height: 65px;
}

.footerbar{
  transform: translate3d(0, 0, 0); 
  transition: 0.2s all ease-out;

}

.footerbar.footerbar--hidden {
   box-shadow: none; transform: translate3d(0, 100%, 0); 
   }


</style>