<template>
  <router-link :to="{ name: 'article', params: { articlePk } }">
    <div class="flex py-1 px-4 justify-between w-97 article-box my-1 mx-auto ">
      <div class="flex justify-center flex-col">
        <p class="alice-reg f-10 c-5353">title</p>
        <h1 class="alice-reg text-base">{{article.title}}</h1>
      </div>
      <div class="flex flex-col items-end">
        <p class="alice-reg text-sm mb-1">author: {{article.user.username}}</p>
        <p class="alice-reg text-xs"><svg id="heart" xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
    <path stroke-linecap="round" stroke-linejoin="round" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
  </svg> : {{article.like_count}}</p>
      </div>
    </div>
  </router-link>
</template>

<script>
export default {
  name:"SmallArticleComponent",
  props: {
    article: {
      type:Object,
      required: false,
    }
  },
  computed: {
    articlePk() {
      return this.article.pk
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

#heart {
  color:#9486CD;
  display:inline;
}
.article-box{
  background-color: #ECEEF0;
  border-radius: 10px;
  box-shadow: rgba(0, 0, 0, 0.04) 0px 3px 5px;
}
.c-5353{
  color:#535353;
}
.f-10{
  font-size: 10px;
}

.w-97{
  width:96%;
}

.article-box:hover{
  background-color: #d4dae0;

}
</style>