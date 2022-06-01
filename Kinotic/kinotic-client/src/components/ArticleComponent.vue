<template>
  <router-link :to="{ name: 'article', params: { articlePk } }">
    <div class="flex px-5 py-2 justify-between w-full article-box my-2 mx-auto">
      <div class="flex w-8/12 items-center">
      <div class="w-1/4 flex justify-around items-center mr-10">
        <p class="text-center bc-bold text-xs">🧾 {{article.pk}}</p>
        <p class="text-lg thin pb-2">||</p>
      </div>

      
      <!-- <div class="flex items-center"> -->
        <p class="bc-md text-sm ml-7">{{article.title}}</p>
      </div>
      <div class="flex flex-col justify-center items-end mr-3">
        <div class="flex">
        <p class="mr-2 bc-md text-xs">author: {{article.user.username}}</p>
        <p class=" text-xs"><svg id="heart" xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
    <path stroke-linecap="round" stroke-linejoin="round" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
  </svg> : {{article.like_count}}</p>

        </div>
        <p class="bc-md text-xs">{{article.created_at|yyyyMMddhhmm}}</p>
      </div>
    </div>
  </router-link>
</template>

<script>
export default {
  name:"ArticleComponent",
  props: {
    article: {
      type:Object,
      required: false,
    },
    index: {
      type:Number
    }
  },
  computed: {
    articlePk() {
      return this.article.pk
    }
  },
  created(){
    console.log(this.article)
  },
  filters: {
    yyyyMMddhhmm : function(value){ 
      // 들어오는 value 값이 공백이면 그냥 공백으로 돌려줌
      if(value == '') return ''

      // 현재 Date 혹은 DateTime 데이터를 javaScript date 타입화
      const jsDate = new Date(value)

      // 연도, 월, 일 추출
      let year = jsDate.getFullYear()
      let month = jsDate.getMonth() + 1
      let day = jsDate.getDate()
      let hour = jsDate.getHours()
      let min = jsDate.getMinutes()

      // 월, 일의 경우 한자리 수 값이 있기 때문에 공백에 0 처리
      if(month < 10){
      month = '0' + month
      }

      if(day < 10){
      day = '0' + day
      }

      if(hour < 10){
      hour = '0' + hour
      }

      if(min < 10){
      min = '0' + min
      }

      // 최종 포맷 (ex - '2021-10-08')
      return year + '.' + month + '.' + day + ' ' + hour + ':' + min
        }
    },
}
</script>

<style scoped>
@font-face {
    font-family: 'paybooc-Medium';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-07@1.0/paybooc-Medium.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
@font-face {
    font-family: 'paybooc-Bold';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-07@1.0/paybooc-Bold.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
.bc-bold{
    font-family: 'paybooc-Bold';

}
.bc-md{
    font-family: 'paybooc-Medium';
}

#heart {
  color:#9486CD;
  display:inline;
}
.article-box{
  background-color: #f5f6f8;
  border-radius: 10px;
  box-shadow: rgba(27, 31, 35, 0.04) 0px 1px 0px, rgba(255, 255, 255, 0.25) 0px 1px 0px inset;
}

.article-box:hover{
  transform:scale(1.005);
  background-color: #dce0e4;

}

p{
  vertical-align: middle;
}

.thin{
  font-weight: 100 !important;
}
</style>