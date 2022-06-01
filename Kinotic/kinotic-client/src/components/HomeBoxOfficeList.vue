<template>
  <div>
    <div class="flex flex-col mx-auto justify-between mt-7 px-3 py-4 info-card" >
      <div class="flex mb-3 ml-3 items-baseline mt-1">
        <p class="text-lg bc-bold mr-3 font5353">실시간 박스오피스</p>
      </div>
      <div class="white-box py-3 mx-2 grid grid-cols-2 grid-rows-5">
        <div 
          v-for="(rank, index) in ranks"
          :key="index"
          :rank="rank"
          class="w-11/12 mx-auto article-box px-4 flex">
          <p class="w-1/12  alice-Bold">{{index+1}}</p>
          <p class="w-1/12">⁝</p>
          <p class="w-5/6 alice-reg f-15 flex items-center">{{rank}}</p>
          </div>

      </div>
    </div>
  </div>
</template>

<script>

export default {
  name:'HomeArticleList',
  props: {
    ranks: {
      type: Array,
      required: false,
    }
  },
  components:{
  },

}
</script>

<style scoped>
.f-15{
  font-size:14px;
}

.white-box{
  background-color: white;
  border-radius: 10px;
  box-shadow: rgba(0, 0, 0, 0.05) 0px 1px 2px 0px;
}
.font5353{
  color: #505e70;

}

.info-card{
  background-color: #fff5d3;
  border-radius: 10px;
  box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
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


.alice-Bold{
    font-family: 'EliceDigitalBaeum_Bold';

}
.alice-reg {
    font-family: 'EliceDigitalBaeum_Regular';
}

.bc-bold{
  font-family: 'paybooc-ExtraBold';
}

.article-box{
  background-color: #e7edf3;
  border-radius: 5px;
  padding-top:2px;
  padding-bottom:2px;
  margin-top:2px;
  margin-bottom:2px;
}

.font-22{
  font-size:21px;
}
</style>