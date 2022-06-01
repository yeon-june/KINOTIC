<template>
  <div class="comment-list-item p-4 my-1">
    <div class="flex items-baseline mb-3">
      <router-link :to="{ name: 'profile', params: { username: review.user.username } }" class="text- alice-Bold ml-1 mr-1">
        {{ review.user.username }} |
      </router-link>
      <p class="text-lg alice-Bold pl-1 pt-1">{{stars}}</p>

    </div>
    <div class="bg-white my-2 pb-2 rad-5">
    <p v-if="!isEditing" class="text-base alice-reg w-full px-3 pt-2">{{ payload.content.content }}</p>
    <p v-if="isEditing" class="w-full px-auto">
      <input type="text" v-model="payload.content.content" autofocus="autofocus" class="alice-reg w-full p-2 h-20 mb-3 bg-gray mx-auto">
    </p>

    <div class="flex flex-col items-end mr-3">
      <div class="flex items-baseline">
        <span v-if="current === review.user.username && !isEditing">
          <button @click="switchIsEditing" class="text-sm alice-reg">Edit</button> ⁝
          <button @click="deleteReview(payload)" class="text-sm alice-reg">Delete</button>
        </span>
        <span v-if="isEditing">
          <button @click="onUpdate">Update</button> |
          <button @click="switchIsEditing">Cancel</button>
        </span>
      </div>
    </div>

    </div>

  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'ReviewListItem',
  props: { 
    review: {
      type:Object
      } },
  data() {
    return {
      isEditing: false,
      payload: {
        moviePk: this.review.movie,
        reviewPk: this.review.pk,
        content:
        {content: this.review.content,
        vote: this.review.vote}
      },
    }
  },
  computed: {
    current() {
      return localStorage.getItem('currentUser')
    },
    moviePk(){
      return this.$route.params.moviePk
    },
    stars(){
      return  '⭐'.repeat(this.payload.content.vote)
    }
  },
  methods: {
    ...mapActions(['updateReview', 'deleteReview']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateReview(this.payload)
      this.isEditing = false
    }
  },
  created(){
    console.log(this.review)
  },
  filters: {
    yyyyMMddhhmm : function(value){ 
      // 들어오는 value 값이 공백이면 그냥 공백으로 돌려줌
      if(value == '') return ''

      // 현재 Date 혹은 DateTime 데이터를 javaScript date 타입화
      const jsDate = new Date(value)

      // 연도, 월, 일 추출
      let year = jsDate.getFullYear()
      let month = jsDate.getMonth() + 1
      let day = jsDate.getDate()
      let hour = jsDate.getHours()
      let min = jsDate.getMinutes()

      // 월, 일의 경우 한자리 수 값이 있기 때문에 공백에 0 처리
      if(month < 10){
      month = '0' + month
      }

      if(day < 10){
      day = '0' + day
      }

      if(hour < 10){
      hour = '0' + hour
      }

      if(min < 10){
      min = '0' + min
      }

      // 최종 포맷 (ex - '2021-10-08')
      return year + '.' + month + '.' + day + ' ' + hour + ':' + min
        }
    },
}
</script>

<style scoped>
input{
  border-radius: 5px;
}

.rad-5{
  border-radius: 5px;
}

.bg-white{
  background: white;
}
.comment-list-item{
  background-color:#F1F6FB;
  border-radius: 5px;
}

.alice-Bold{
  font-family: 'EliceDigitalBaeum_Bold';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_220508@1.0/EliceDigitalBaeum_Bold.woff2') format('woff2');
  font-weight: 700;
  font-style: normal;
}

.alice-reg {
    font-family: 'EliceDigitalBaeum_Regular';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_220508@1.0/EliceDigitalBaeum_Regular.woff2') format('woff2');
    font-weight: 400;
    font-style: normal;
}
.bg-gray{
  background-color: #f7f4f4;
}
</style>