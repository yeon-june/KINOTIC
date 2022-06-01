<template>
  <div class="w-97 mx-auto">
    <img src="@/assets/Search.png" alt="" class="w-2/12 mx-auto">
    <form @submit.prevent="onSubmit" class="w-full h-11 flex items-center px-4 mt-4">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
  <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
</svg> 
      <input type="text" class="h-10 w-full px-4" placeholder="찾고싶은 영화 제목을 입력하세요" v-model="keyword">
    </form>
    <hr class="mt-3 mb-4">
    <SearchList :contents="contents" class="px-1 mb-6"/>

  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import SearchList from '@/components/SearchList.vue'


export default {
  name:'SearchView',
  data(){
    return{
      keyword : this.$route.params.search,

    }
  },
  computed: {
    ...mapGetters(['searches']),
    initKeyword(){
      return this.$route.params.search
    },
    contents(){
      return this.searches
    }
  },

  methods:{
    ...mapActions(['fetchSearch']),
    onSubmit(){
      const search = this.keyword
      this.$router.replace({name:'search', params: { search }})
    },
  },
  components:{
    SearchList,
  },
  created() {
    this.fetchSearch(this.initKeyword)
  },
}
</script>

<style scoped>
form{
  background-color:#f3eef7;
  border-radius:10px;
  box-shadow: rgba(0, 0, 0, 0.05) 0px 1px 2px 0px;
}

input{
  background-color:transparent;
  border-radius:5px;
}
input:focus {
  outline:2px solid #c3b7cf;}

.w-97{
  width:97%;
}
.w-90{
  width:90%
}
</style>