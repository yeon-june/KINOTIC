<template>
  <div :class="{ 'overflow-hidden' : showModal}">
    <ListDetailModal v-if="showModal" @close="showModal = false">
      <!-- 1-1) 모달 헤더 -->
      <h3 slot="header" class="bc-card modal-text flex items-center">{{title}}</h3> 
      <!-- 1-2) 모달 푸터 -->
      <span slot="body">
          <ModalList :contents="contents" class="px-1 mb-6"/>
          <i class="closeModalBtn fas fa-times" aria-hidden="true"></i>
      </span>
    </ListDetailModal>
    <HomeRecList :title="'KINOTIC 추천'" :recs="basicRec" class="w-97 mx-auto" @onClick="onClick('basic')"/>
    <HomeRecList :title="'내 친구는 뭘 보고 있을까?'" :recs="userFollowRec" class="w-97 mx-auto" @onClick="onClick('follow')"/>
    <HomeRecList :title="`${current}님은 이런 것도 좋아할 것 같아요!`" :recs="userLikeRec" class="w-97 mx-auto" @onClick="onClick('like')"/>
    <HomeRecList :title="'오늘같은 날씨엔 이런 영화 어때요?'" :recs="weatherRec" class="w-97 mx-auto" @onClick="onClick('weather')"/>
    
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex' 
import HomeRecList from '@/components/HomeRecList.vue'
import ListDetailModal from '@/components/ListDetailModal.vue'
import ModalList from '@/components/ModalList.vue'


export default {
  name:'RecommendView',
  data(){
    return{
      title:'',
      showModal: false,
      contents: [],
    }
  },
  components: {
    HomeRecList, ListDetailModal, ModalList
  },
  computed:{
    ...mapGetters(['isLoggedIn', 'weatherRec', 'basicRec', 'userFollowRec', 'userLikeRec']),
    current(){
      return localStorage.getItem('currentUser')
    }
  },
  methods: {
    ...mapActions(['fetchBasicRec','fetchWeatherRec', 'fetchUserFollowRec', 'fetchUserLikeRec']),
    onClick(value){
      this.showModal = !this.showModal
      if (value==='basic') {
        this.contents = this.basicRec
        this.title = 'KINOTIC 추천'
      } else if(value==='weather') {
        this.contents = this.weatherRec
        this.title = '오늘같은 날씨엔 이런 영화 어때요?'
      } else if(value==='follow') {
        this.contents = this.userFollowRec
        this.title = '내 친구는 뭘 보고 있을까?'
      } else if(value==='like') {
        this.contents = this.userLikeRec
        this.title = `${this.current}님은 이런 것도 좋아할 것 같아요!`
      }
    }
  },
  created() {
    if (this.isLoggedIn) {
      this.fetchBasicRec()
      this.fetchWeatherRec()
      this.fetchUserFollowRec()
      this.fetchUserLikeRec()
    } else {
      document.location.href ="/login"
    }
  },
}
</script>

<style scoped>
@font-face {
    font-family: 'paybooc-Bold';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-07@1.0/paybooc-Bold.woff') format('woff');
    font-weight: normal;
    font-style: normal;
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