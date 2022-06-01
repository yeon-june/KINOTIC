<template>
  <div>
    <div class="flex mx-auto justify-between mt-7 px-6 py-5 info-card" >
      <div class="flex items-center">
        <img src="@/assets/default.jpg" alt="" class="rounded-full mr-7 w-20 h-20 border" >
        <div class="flex flex-col justify-center">
          <div class="flex mb-1 items-end pb-2">
            <p class="text-xl mr-3 bc-Bold f-5353">{{profile.username}}</p>
            <button v-if="current !== profile.username" @click="followThis" class="px-3 py-1 text-xs follow">{{followBtn}}</button>
          </div>
          <div class="flex">
            <button @click="$emit('onClick','followings')">
              <p class="text-xs mr-3 bc-Bold f-5353">followings: {{followingCnt}}</p>
            </button>
            <button @click="$emit('onClick','followers')">
              <p class="text-xs mr-3 bc-Bold f-5353">followers: {{followersCnt}}</p>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'

export default {
  name:'ProfileUserinfoCard',

  methods:{
    ...mapActions(['followUser']),
    followThis(){
      if (this.isLoggedIn) {
          this.followUser(this.profilePk)
        } else{
          window.location.href = '/login'
        }
    }
  },
  computed: {
    ...mapGetters(['isLoggedIn']),
    profilePk(){
      return this.profile.pk
    },
    current(){
      return localStorage.getItem('currentUser')
    },
    following_usernames() {
        return this.profile?.followers?.map ((user)=> {
          return user?.username
        })
      },
    isFollowing(){
      return this?.following_usernames?.includes(this.current)
    },
    followBtn() {
      if (this.isFollowing){
        return 'UnFollow'
      } else {
        return 'Follow'
      }
    },
    profileImg () {
      if (this.profile.profile_image === 'static/default.jpg') {
        return '@/assets/default.jpg'
      } else {
        return this.profile.profile_image
      }
    },
    followingCnt() {
      return this.profile.followings?.length
    },
    followersCnt() {
      return this.profile.followers?.length
    },
    isMe() {
      return this.profile.username === localStorage.getItem('currentUser')
    }
  },
  props: {
    profile: {
      type: Object,
      required: true,
    }
  },
  created(){
    console.log(this.profile)
  }
}
</script>

<style scoped>
.info-card{
  background-color: #f8f4fe;
  border-radius: 10px;
  box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;

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
.bc-ExtraBold{
  font-family: 'paybooc-ExtraBold';
}
.bc-Bold{
  font-family: 'paybooc-Bold';

}
.f-5353{
  color:#535353;
}

.border{
  border: 1px solid #e2e2e2;
}
button.follow{
  background-color: #fdeeb7;
  border-radius: 4px;
  box-shadow: rgba(60, 64, 67, 0.1) 0px 1px 2px 0px, rgba(60, 64, 67, 0.1) 0px 1px 3px 1px;
}
</style>