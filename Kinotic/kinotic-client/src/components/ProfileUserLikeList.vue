<template>
  <div>
    <div class="flex flex-col mx-auto justify-between mt-7 px-4 py-5 info-card" >
      <div class="flex justify-between my-1">  
        <div class="flex mb-3 ml-2 items-baseline">
          <p class="pl-1 text-lg bc-Bold mr-4 f-5353">{{user}} 찜목록</p>
          <p class="text-xs bc-Bold mr-3 f-5353">찜 개수: {{contentsCnt}}</p>
        </div>
          <button @click="$emit('onClick','Like')" class="col-darkp flex items-start mr-2" v-if="contentsCnt > 5">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
    <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z" />
  </svg>
          </button>
      </div>
      <div class="flex">      
        <ProfileMovieCard 
          v-for="content in contents"
          :key="content.pk"
          :content="content"
          class="w-1/5 p-1"/>
        <DefaultMovieCard         
          v-if="!contentsCnt"
          class="w-1/5 p-1"/>
      </div>
    </div>
  </div>
</template>

<script>
import ProfileMovieCard from "@/components/ProfileMovieCard.vue";
import DefaultMovieCard from "@/components/DefaultMovieCard.vue"

export default {
  name:'ProfileUserLikeList',
  computed: {
    current(){
      return localStorage.getItem('currentUser')
    },
    contents() {
      return this.profile.like_movie?.slice(0,5)
    },
    contentsCnt() {
      return this.profile.like_movie?.length
    },
    user(){
      if (this.profile.username === this.current){
        return '나의'
      } else{
        return this.profile.username + ' 님의'
      }
    }
  },
  props: {
    profile: {
      type: Object,
      required: true,
    }
  },
  components:{
    ProfileMovieCard,
    DefaultMovieCard,
  }
}
</script>

<style scoped>
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
.bc-ExtraBold{
  font-family: 'paybooc-ExtraBold';
}
.bc-Bold{
  font-family: 'paybooc-Bold';

}
.f-5353{
  color:#535353;
}


.info-card{
  background-color: #f8f4fe;
  border-radius: 10px;
  box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;

}

</style>