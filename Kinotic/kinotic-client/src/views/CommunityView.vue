<template>
  <div class="w-97 mx-auto">
    <img src="@/assets/community.png" alt="" class="w-2/12 mx-auto mb-1 mt-5">
    <div v-if="isLoggedIn" class="flex justify-end mb-2 mr-2 write-btn w-97">
      <router-link :to="{ name: 'articleNew' }" class="text-xs write-box px-3 py-1 bc-md thin">글쓰기</router-link>
    </div>
    <CommunityList :page="page" :key="list_reload" class="w-97 mx-auto"/>
    <Paginate
      class="flex mt-5"
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
      v-if="pageCnt > 1">
    </Paginate>
  </div>

</template>

<script>
import CommunityList from '@/components/CommunityList.vue'
import { mapGetters, mapActions} from 'vuex'
import Paginate from 'vuejs-paginate'


export default {
  name:'CommunityView',
  data(){
    return{
      page: 1,
      contents: this.articles,
      list_reload:0,
      rangetype: 0,
      reload: 0,
    }
  },
  components:{
    CommunityList,
    Paginate
  },
  computed: {
    ...mapGetters(['isLoggedIn', 'articles']),
    pageCnt(){
      return this.articles?.length % 7 ? parseInt(this.articles?.length / 7) + 1 : parseInt(this.articles?.length / 7)
    }
  },
  methods: {
    ...mapActions(['fetchArticles']),
  },
  created() {
    this.fetchArticles()
    console.log(this.articles)
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

.alice-Bold{
    font-family: 'EliceDigitalBaeum_Bold';

}
.alice-reg {
    font-family: 'EliceDigitalBaeum_Regular';
}

.bc-bold{
  font-family: 'paybooc-ExtraBold';
}

.write-box{
  background-color: #f1e9fa;
  border-radius: 5px;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 0px 5px 0px, rgba(0, 0, 0, 0.1) 0px 0px 1px 0px;
  color: #535353;
}
.write-box:hover{
  background-color: #e1d3f0;
  font-weight:700;
}

.mt-vh3{
  margin-top:2.5vh;
}
.vh100{
  height:78vh;
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
  width:97%;
}
.thin{
  font-weight: 200 !important;
}
@font-face {
    font-family: 'paybooc-Medium';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-07@1.0/paybooc-Medium.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
.bc-md{
  font-family: 'paybooc-Medium';

}
</style>