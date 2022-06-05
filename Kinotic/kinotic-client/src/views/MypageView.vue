<template>

  <div class="w-97 mx-auto" :class="{ 'overflow-hidden' : showModal || showPostModal || showReviewModal || showFollowModal}">
    <FollowListModal v-if="showFollowModal" @close="showFollowModal = false" id="modal">
      <!-- 1-1) 모달 헤더 -->
      <h3 slot="header" class="bc-card flex items-center">{{title}}</h3> 
      <!-- 1-2) 모달 푸터 -->
      <span slot="body">
          <ul>
            <li v-for="content in contents" :key="content.pk">
              <router-link :to="{name: 'profile', params: {username: content.username} }">{{content.username}}</router-link>
            </li>
          </ul>
          <i class="closeModalBtn fas fa-times" aria-hidden="true"></i>
      </span>
    </FollowListModal>


    <ListDetailModal v-if="showModal" @close="showModal = false" id="modal">
      <!-- 1-1) 모달 헤더 -->
      <h3 slot="header" class="bc-card modal-text flex items-center">{{title}}</h3> 
      <!-- 1-2) 모달 푸터 -->
      <span slot="body">
          <ModalList :contents="contents" class="mb-6"/>
          <i class="closeModalBtn fas fa-times" aria-hidden="true"></i>
      </span>
    </ListDetailModal>

    <ListDetailModal v-if="showPostModal" @close="showPostModal = false" id="modal">
      <!-- 1-1) 모달 헤더 -->
      <h3 slot="header" class="bc-card modal-text flex items-center">{{title}}</h3> 
      <!-- 1-2) 모달 푸터 -->
      <span slot="body">
          <ModalPostList :contents="contents" class="mb-6"/>
          <i class="closeModalBtn fas fa-times" aria-hidden="true"></i>
      </span>
    </ListDetailModal>

    <ListDetailModal v-if="showReviewModal" @close="showReviewModal = false" id="modal">
      <!-- 1-1) 모달 헤더 -->
      <h3 slot="header" class="bc-card modal-text flex items-center">{{title}}</h3> 
      <!-- 1-2) 모달 푸터 -->
      <span slot="body">
          <ModalReviewList :contents="contents" class="mb-6"/>
          <i class="closeModalBtn fas fa-times" aria-hidden="true"></i>
      </span>
    </ListDetailModal>

    <ProfileUserinfoCard :profile="profile" @onClick="onCheckFollow"/>
    <ProfileUserLikeList :profile="profile" @onClick="onClick('like')"/>
    <ProfileUserLookedList :profile="profile"  @onClick="onClick('look')"/>
    <UserReviewList :profile="profile" @onClick="onReviewClick"/>
    <UserArticleList :profile="profile" @onClick="onPostClick"/>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import ProfileUserinfoCard from '@/components/ProfileUserinfoCard.vue'
import ProfileUserLikeList from '@/components/ProfileUserLikeList.vue'
import ProfileUserLookedList from '@/components/ProfileUserLookedList.vue'
import UserArticleList from '@/components/UserArticleList.vue'
import UserReviewList from '@/components/UserReviewList.vue'
import ListDetailModal from '@/components/ListDetailModal.vue'
import ModalList from '@/components/ModalList.vue'
import ModalPostList from '@/components/ModalPostList.vue'
import ModalReviewList from '@/components/ModalReviewList.vue'
import FollowListModal from '@/components/FollowListModal.vue'


export default {
  name:'MypageView',
  data(){
    return{
      title:'',
      showModal: false,
      showPostModal: false,
      showReviewModal: false,
      showFollowModal: false,
      contents: [],
    }
  },
  computed: {
    ...mapGetters(['profile', 'isLoggedIn'])

  },
  methods: {
    ...mapActions(['fetchProfile', 'fetchCurrentUser']),
    onClick(value){
      this.showModal = !this.showModal
      if (value==='like') {
        this.contents = this.profile.like_movie
        this.title = '나의 찜목록'
      } else{
        this.contents = this.profile.looked
        this.title = '내가 본 영화'
      }
    },
    onPostClick(){
      this.showPostModal = !this.showPostModal
        this.contents = this.profile.articles
        this.title = '나의 최근 게시글'
    },
    onReviewClick(){
      this.showReviewModal = !this.showReviewModal
        this.contents = this.profile.reviews_list
        this.title = '나의 최근 리뷰'
    },
    onCheckFollow(value){
      this.showFollowModal = !this.showFollowModal
      if (value ==='followings') {
        this.contents = this.profile.followings
        this.title = 'My Following List'
      } else{
        this.contents = this.profile.followers
        this.titlel = 'My Follower List'
      }
    }
  },
  created() {
    if  (!this.isLoggedIn) {
      document.location.href="/login"
    } else{
      const payload = { username: this.$route.params.username }
      this.fetchProfile(payload)
    }
  },
  components: {
    ListDetailModal,
    ProfileUserinfoCard,
    ProfileUserLikeList,
    ProfileUserLookedList,
    UserArticleList,
    UserReviewList,
    ModalList,
    ModalPostList,
    ModalReviewList,
    FollowListModal
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
.w-97{
  width:97%
}
.overflow-hidden {
  height: 80vh;
  overflow: hidden;
}

.modal-text{
  color: #374454;
  font-size: 22px;
}
</style>