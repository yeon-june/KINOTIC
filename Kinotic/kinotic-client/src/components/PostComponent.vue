<template>
  <router-link :to="{ name: 'article', params: { articlePk } }" class="content-card">
    <div class=" flex flex-col justify-between">
      <div class="flex flex-col justify-between">
        <p class="bc-bold text-sm">{{content.title}}</p>
      </div>
      <hr class="my-1">
      <div>
        <p class="bc-md text-sm mb-2">{{shortContent}}</p>
        <p class="bc-md f-11">{{content.created_at | yyyyMMdd}}</p>
      </div>
    </div>
  </router-link>
</template>

<script>
export default {
  name:'PostComponentCard',
  props: {
    content:{
      type:Object,
      required:false,
    }
  },
  computed:{
    shortContent(){
      return this.content.content.slice(0,10) + '...'
    },
    articlePk(){
      return this.content.pk
    },
  },
  created(){
    console.log(this.content)
  },
  filters: {
    yyyyMMdd : function(value){ 
      // 들어오는 value 값이 공백이면 그냥 공백으로 돌려줌
      if(value == '') return ''

      // 현재 Date 혹은 DateTime 데이터를 javaScript date 타입화
      const jsDate = new Date(value)

      // 연도, 월, 일 추출
      let year = jsDate.getFullYear()
      let month = jsDate.getMonth() + 1
      let day = jsDate.getDate()

      // 월, 일의 경우 한자리 수 값이 있기 때문에 공백에 0 처리
      if(month < 10){
      month = '0' + month;
      }

      if(day < 10){
      day = '0' + day
      }

      // 최종 포맷 (ex - '2021-10-08')
      return year + '.' + month + '.' + day
        }
        }
} 
</script>

<style scoped>
.content-card{
  background-color: white;
  border-radius: 5px;
  box-shadow: rgba(0, 0, 0, 0.04) 0px 3px 5px;
}
.content-card:hover{
  background-color: rgb(245, 245, 245);
}
.f-11{
  font-size:11px !important;
}
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
.h70{
  min-height:70px;
}
</style>