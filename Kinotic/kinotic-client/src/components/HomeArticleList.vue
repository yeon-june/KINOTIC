<template>
  <div>
    <div class="flex flex-col mx-auto justify-between mt-7 px-3 py-4 info-card" >
      <div class="flex mb-3 ml-2 items-baseline mt-1">
        <p class="text-lg alice-Bold mr-3 font-col">실시간 게시글</p>
      </div>
      <div class="white-box py-2 mx-1">
        <SmallArticleComponent
          v-for="content in contents"
          :key="content.pk"
          :article="content"
          class="w-full mx-auto"/>
      </div>
    </div>
  </div>
</template>

<script>
import SmallArticleComponent from '@/components/SmallArticleComponent'

export default {
  name:'HomeArticleList',
  computed: {
    contents() {
      return this.articles.slice(0,3)
    },
  },
  props: {
    articles: {
      type: Array,
      required: false,
    }
  },
  components:{
    SmallArticleComponent
  },
  created(){
    console
  }

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
.jalnan {
    font-family: 'yg-jalnan';
}

.white-box{
  background-color: white;
  border-radius: 10px;
  box-shadow: rgba(0, 0, 0, 0.05) 0px 1px 2px 0px;
}

.font-col{
  color: #505e70;
}

.info-card{
  background-color: #ebe7f2;
  border-radius: 10px;
  box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
}


</style>