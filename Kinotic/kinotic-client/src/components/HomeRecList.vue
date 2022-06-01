<template>
  <div class="flex flex-col mx-auto mt-7 px-2 py-4 info-card">
    <div class="flex ml-3 justify-between mr-3 my-1">
      <p class="text-lg bc-bold mr-3 col-darkp">{{title}}</p>
      <button @click="$emit('onClick')" class="col-darkp">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.8">
  <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z" />
</svg>
      </button>
    </div>
    <hr class="mt-1">
    <div class="flex">
      <MainMovieCard 
        v-for="content in recshort"
        :key="content.pk"
        :recs="recs"
        :content="content"
        class="w-1/4 p-2"/>
    </div>
  </div>
</template>

<script>
import MainMovieCard from "@/components/MainMovieCard.vue"

export default {
  name:'HomeRecList',
  computed:{
    recshort() {
      return this.recs.slice(0,4)
    }
  },
  props: {
    title:{
      type: String,
      required: true,
    },
    recs: {
      type: Array,
      required: true,
    }
  },
  components:{
    MainMovieCard,
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
@font-face {
    font-family: 'paybooc-ExtraBold';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-07@1.0/paybooc-ExtraBold.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
@font-face {
    font-family: 'paybooc-Bold';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-07@1.0/paybooc-Bold.woff') format('woff');
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
.font-22{
  font-size:21px;
}

.font-col{
  color: #505e70;
}

.col-darkp{
  color:#614c88;
}

.text-stroke {
  -webkit-text-stroke: 1.5px #614c88;
}

.info-card{
  background-color: #f8f4fe;
  border-radius: 10px;
  box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
}


.font-w{
  font-weight: bolder;
}

</style>