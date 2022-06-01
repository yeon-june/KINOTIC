<template>
  <div class="w-97 mx-auto">
    <div class="bg-5353 vh-50 outer">
      <div class="item-wrapper">
      <img :src="this.poster" alt="alter" class="item-box vh-50 full-img">
      <img :src="this.poster" alt="poster image" class="crop-img vh-50 px-5 item-box">
      </div>

    </div>
    <div class="px-1">
    <p class="title alice-Bold mt-4 ">{{ movie.title }}</p>
    <div class="flex mb-3 items-baseline">
      <p class="mr-3 alice-reg text-sm">개봉일: {{movie.release_date}}</p> 
      <p class="text-sm">⁝</p>
      <p class="mx-3 alice-reg text-sm">관람객 수: {{movie.popularity}}</p>
      <p class="text-sm">⁝</p>
      <p class="mx-3 alice-reg text-sm">상영시간: {{movie.runtime}}분</p>
      <p class="text-sm">⁝</p>
      <p class="ml-3 mr-1 alice-reg text-sm">⭐ {{movie.vote_average}}</p>
      <p class="alice-reg text-xs">({{movie.vote_count}}명 참여)</p>
    </div>
    <!-- Article Like UI -->
    <div class="flex mb-3">
      <div class="mr-2">
        Likeit:
        <button class="px-2"
          @click="ifLogLike"
        >{{ like_icon }}</button>
      </div>

      <div>
        Watchedit!:
        <button class="px-2"
          @click="ifLogWatch"
        >{{ look_icon }}</button>
      </div>
    </div>
    <hr class="mb-2 col-hr">
    <div class="flex mb-6">
      <div 
      v-for="(genre,index) in movie.genres"
      :key="index"
      class="genre-box mr-2 px-2">
      {{genre.name}}
      </div>
    </div>
    <p class="alice-reg" align="justify">
      {{ movie.overview }}
    </p>

    <p class="mt-9 alice-Bold text-lg f-5353">예고편</p>
    <hr class="mt-1 mb-2">
    <div class="w-full trailer-container">
      <iframe v-if="movie.src" :src="movie.src" class="w-3/4 mx-auto h-350"></iframe>
    </div>
    </div>

    <br>
    <hr class="mb-1">

    <!-- Comment UI -->
    <ReviewList :reviews="reviews" class="p-1"/>

  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import ReviewList from '@/components/ReviewList.vue'


  export default {
    name: 'MovieDetailView',
    components: { ReviewList },
    computed: {
      ...mapGetters(['movie', 'movieTrailer', 'isLoggedIn']),
      reviews(){
        return this?.movie?.reviews
      },

      moviePk() {
        return this.$route.params.moviePk
        },
      likeCount() {
        return this.movie?.like_users?.length
      },
      current() {
        return localStorage.getItem('currentUser')
      },
      like_usernames() {
        return this.movie?.like_users?.map ((user)=> {
          return user?.username
        })
      },
      liking() {
        return this?.like_usernames.includes(this.current)
      },
      looked_usernames() {
        return this.movie?.looked_users?.map ((user)=> {
          return user?.username
        })
      },
      looked() {
        return this?.looked_usernames.includes(this.current)
      },
      like_icon() {
        if (this.liking){
          return '❤'
        } else { 
          return '🖤'
        }
      },
      look_icon() {
        if (this.looked){
          return 'WATCHED!🔁'
        } else { 
          return 'NOT YET! ▶'
        }
      },
      poster() {
      return 'https://image.tmdb.org/t/p/original/'+this.movie.poster_path
      },

    },
    methods: {
      ...mapActions([
        'fetchMovie',
        'likeMovie',
        'lookMovie',
        'fetchMovieTrailer',
      ]),
      ifLogLike(){
        if (this.isLoggedIn) {
          this.likeMovie(this.moviePk)
        } else{
          window.location.href = '/login'
        }
      },
      ifLogWatch(){
        if (this.isLoggedIn) {
          this.lookMovie(this.moviePk)
        } else{
          window.location.href = '/login'
        }
      },
    },
    created() {
      this.fetchMovie(this.moviePk)
    },
  }
</script>

<style scoped>
.trailer-container{
  background-color: #16191d;
}

.h-350{
  height:350px;
}

.item-wrapper{
  position:relative;
}

.item-box{
  position:absolute;
  left:50%;
  transform:translate(-50%,0);
}

.col-hr{
  border-color: #cecece;
}

.crop-img{
  width:100%;
  max-height: 350px;
  transition: all ease 0.5s;
  object-fit: cover;
  object-position: 0 50%;
  filter: opacity(100%);
}

.crop-img:hover{
  filter:opacity(0%)  
}

.full-img{
    max-height: 350px;
}

.bg-5353{
  background-color: #161616;
}
.title{
  font-size: 26px;
}
.alice-Bold{
  font-family: 'EliceDigitalBaeum_Bold';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_220508@1.0/EliceDigitalBaeum_Bold.woff2') format('woff2');
  font-weight: 700;
  font-style: normal;
}

.alice-reg {
    font-family: 'EliceDigitalBaeum_Regular';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_220508@1.0/EliceDigitalBaeum_Regular.woff2') format('woff2');
    font-weight: 400;
    font-style: normal;
}

.w-97{
  width:97%;
}
.vh-50{
  height:50vh;
}
.genre-box{
  background-color:#4A2C80;
  color:white;
  border-radius:3px;
}
.outer{
    max-height: 350px;
}
.f-5353{
  color:#535353;
}
</style>
