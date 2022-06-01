<template>
<!-- 라우터 링크 만들고 디테일 페이지로 연결 가능한,, + 디테일 페이지에서 fetchmovie -->
  <router-link :to="{name:'movie', params:{moviePk: content.pk} }">
    <div class="content-card px-2 py-3 radius-5 border-light h-270 shadow">
      <div class="h-210 flex items-center radius-5 poster-container">
        <img :src="poster" alt="movie poster" class="radius-5" loading=lazy>
      </div>
      <hr class="my-2">
      <p class="w-95 over-hidden mx-auto f-11 alice-reg h-8 flex items-start">{{content.title}}</p>
    </div>

  </router-link>

</template>

<script>
export default {
  name:'MovieCard',
  props: {
    content:{
      type:Object,
      required:false,
    },
  },
  computed: {
    poster() {
      return 'https://image.tmdb.org/t/p/original/'+this.content.poster_path
    }
  },
}
</script>

<style scoped>
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

.content-card{
  background-color: white;
}

.content-card:hover{
  transform:scale(1.05);
}

.f-11{
  font-size: 13px;
}

.w-95{
  width:98%;
}


.h-210{
  height:210px;
  overflow: hidden;
}

.h-270{
  height:280px;
}

.radius-5{
  border-radius: 5px
}

.border-light{
  border: 1px solid #e7ecf1;
}

.shadow{
  box-shadow: rgba(0, 0, 0, 0.30) 0px 5px 15px;
}

.over-hidden{
  overflow:hidden !important;
}
</style>