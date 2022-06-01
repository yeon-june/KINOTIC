<template>
<!-- 라우터 링크 만들고 디테일 페이지로 연결 가능한,, + 디테일 페이지에서 fetchmovie -->
  <router-link :to="{name:'movie', params:{moviePk: content.pk} }">
    <div class="content-card px-2 py-3 radius-5">
      <div class="h-150 flex items-center radius-5 poster-container">
        <img :src="poster" alt="movie poster" class="radius-5" loading=lazy>
      </div>
      <hr class="my-1">
      <p class="w-95 mx-auto f-12 alice-reg h-8 flex items-center over-hidden">{{content.title}}</p>
    </div>

  </router-link>

</template>

<script>
export default {
  name:'ProfileMovieCard',
  props: {
    content:{
      type:Object,
      required:false,
    },
    recs:{
      type:Array,
      required:false,
    }
  },
  computed: {
    poster() {
      return 'https://image.tmdb.org/t/p/original/'+this.content.poster_path
    }
  },
  created(){
    console.log(this.content)
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

.alice-Bold{
    font-family: 'EliceDigitalBaeum_Bold';

}
.alice-reg {
    font-family: 'EliceDigitalBaeum_Regular';
}

.poster-container{
  box-shadow: rgba(0, 0, 0, 0.05) 0px 1px 2px 0px;

}

.leferi-base{
  font-family: 'LeferiBaseType-RegularA';

}
.content-card{
  background-color: white;
  height:210px !important;
  box-shadow: rgba(0, 0, 0, 0.17) 0px 3px 6px;

}
.content-card:hover{
  transform:scale(1.01);
}

.h-150{
  height:150px;
  overflow: hidden;
}

.radius-5{
  border-radius: 5px
}
.f-12{
  font-size: 12px;
}
</style>