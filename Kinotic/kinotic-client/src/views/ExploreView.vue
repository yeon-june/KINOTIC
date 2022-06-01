<template>
  <div class="w-97 mx-auto">
    <div class="flex justify-start items-center my-6">
      <label for="order" class="px-2 text-center text-lg py-0.5">정렬</label>
      <select name="order" @change="onChange($event)" v-model="rangetype" aria-label="Default select example" class="form-select appearance-none
        block
        w-1/4
        px-3
        py-1
        text-base
        font-normal
        text-gray-700
        bg-white bg-clip-padding bg-no-repeat
        border border-solid border-gray-300
        rounded
        transition
        ease-in-out
        focus:text-gray-700 focus:bg-white focus:border-purple-600 focus:outline-none">
          <option value="9">가나다순</option>
          <option value="1">개봉예정</option>
          <option value="2">평점내림차순</option>
          <option value="3">평점오름차순</option>
          <option value="4">평가많은순</option>
          <option value="5">개봉일내림차순</option>
          <option value="6">개봉일오름차순</option>
          <option value="7">상영시간긴순</option>
          <option value="8">상영시간짧은순</option>
        </select>

    </div>
    <ExploreList :page="page" :key="list_reload" class="px-1 mb-10"/>
    <Paginate
      class="flex mt-10"
      v-model="page"
      :page-count=pageCnt
      :page-range="3"
      :margin-pages="2"
      :prev-text="'Prev'"
      :next-text="'Next'"
      :container-class="'pagination'"
      :page-class="'page-item'"
      :prev-class="'prev'"
      :next-class="'next'"
      v-if="pageCnt > 1"
      >
    </Paginate>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import ExploreList from '@/components/ExploreList.vue'
import Paginate from 'vuejs-paginate'


export default {
  name:'ExploreView',
  data(){
    return{
      page: 1,
      contents: this.movies,
      list_reload:0,
      rangetype: 0,
      reload: 0,
    }
  },
  computed: {
    ...mapGetters(['movies']),
    pageCnt(){
      return parseInt(this.movies.length / 20)
    }

    
  },
  methods:{
    ...mapActions(['fetchMovies', 'rangeMovie']),
    onChange(){
      this.page = 1
      this.rangeMovie(this.rangetype)
    }
  },
  components:{
    Paginate,
    ExploreList,
  },
  created() {
    this.fetchMovies()
  },

}

</script>

<style>
@font-face {
    font-family: 'paybooc-Bold';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-07@1.0/paybooc-Bold.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
.bc-bold{
    font-family: 'paybooc-Bold';

}

.pagination {
  height: 30px !important;
  display:flex;
  justify-content:space-around;
  align-content: center;
  width:60%;
  margin-left: auto !important;
  margin-right: auto !important;
  background-color: #fdfcf9;
  border-radius: 2px;
  box-shadow: rgba(0, 0, 0, 0.12) 0px 1px 3px, rgba(0, 0, 0, 0.2) 0px 1px 2px;
}
.page-item {
  display: flex;
  justify-content: center;
  align-items: center;
  padding-right: 7px !important;
  padding-left: 7px !important;
  width: 57px !important;
  background-color: #fdfcf9;
}
.active{
  background-color: #fce389;
  box-shadow: rgba(0, 0, 0, 0.06) 0px 2px 4px 0px inset;

}
.pagination > li {
  margin-right:1px;
  margin-left:1px;
}
.next{
  display:flex;
  align-items:center;
  padding-left: 15px !important;
  padding-right:10px !important;
  border-left:solid 0.1px #eee;

}
.prev{
  display:flex;
  align-items:center;
  padding-right: 15px !important;
  padding-left:10px !important;
  border-right:solid 0.1px #eee;
}
.w-97{
  width:97% !important;
}



</style>