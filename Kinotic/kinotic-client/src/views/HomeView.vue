<template>
  <div :class="{ 'overflow-hidden' : showModal}">
    <ListDetailModal v-if="showModal" @close="showModal = false" id="modal">
      <!-- 1-1) 모달 헤더 -->
      <h3 slot="header" class="bc-card modal-text flex items-center">{{title}}</h3> 
      <!-- 1-2) 모달 푸터 -->
      <span slot="body">
          <ModalList :contents="contents" class="mb-6"/>
          <i class="closeModalBtn fas fa-times" aria-hidden="true"></i>
      </span>
    </ListDetailModal>
    <SearchBar class="w-97 mx-auto mt-6" @onSubmit="onSearch"/>
    <HomeRecList :title="'KINOTIC 추천'" :recs="basicRec" class="w-97 mx-auto" @onClick="onClick('basic')"/>
    <HomeBoxOfficeList :ranks="boxOffice.title" class="w-97 mx-auto"/>
    <HomeRecList :title="'오늘같은 날씨엔 이런 영화 어때요?'" :recs="weatherRec" class="w-97 mx-auto" @onClick="onClick('weather')"/>
    <HomeArticleList :articles="articles" class="w-97 mx-auto"/>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue'
import HomeRecList from '@/components/HomeRecList.vue'
import HomeArticleList from '@/components/HomeArticleList.vue'
import ListDetailModal from '@/components/ListDetailModal.vue'
import ModalList from '@/components/ModalList.vue'
import HomeBoxOfficeList from '@/components/HomeBoxOfficeList.vue'
import { mapGetters, mapActions } from 'vuex' 

export default {
  name:'HomeView',
  components: {
    ModalList,
    SearchBar,
    HomeRecList,
    HomeArticleList,
    ListDetailModal,
    HomeBoxOfficeList,
  },
  data(){
    return{
      title:'',
      showModal: false,
      contents: [],
    }
  },
  computed:{
    ...mapGetters(['isLoggedIn', 'weatherRec', 'basicRec', 'articles','boxOffice'])
  },
  methods: {
    ...mapActions(['fetchBasicRec','fetchWeatherRec','fetchArticles','fetchBoxoffice']),
    onClick(value){
      this.showModal = !this.showModal
      if (value==='basic') {
        this.contents = this.basicRec
        this.title = 'KINOTIC 추천 ✨'
      } else{
        this.contents = this.weatherRec
        this.title = '오늘같은 날씨엔 이런 영화 어때요? ⛅'
      }
    },
    onSearch(search){
      this.$router.push({name:'search', params: { search }})
    },
  },

  created() {
    this.fetchBasicRec()
    this.fetchWeatherRec()
    this.fetchArticles()
    this.fetchBoxoffice()
  }
}
</script>

<style scoped>
@font-face {
    font-family: 'paybooc-Bold';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-07@1.0/paybooc-Bold.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
@font-face {
    font-family: 'yg-jalnan';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_four@1.2/JalnanOTF00.woff') format('woff');
    font-weight: normal;
    font-style: normal;
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
.alice-Bold{
    font-family: 'EliceDigitalBaeum_Bold';
}
.alice-reg {
    font-family: 'EliceDigitalBaeum_Regular';
}
.jalnan {
    font-family: 'yg-jalnan';
}
.bc-card {
    font-family: 'paybooc-Bold';
}

.w-97 {
  width: 97%;
}

.overflow-hidden {
  height: 0vh;
  overflow: hidden;
}

.modal-text{
  color: #374454;
  font-size: 22px;
}


</style>