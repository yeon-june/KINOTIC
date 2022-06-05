<template>
  <div class="comment-list-item p-4 my-1">
    <div class="flex items-baseline mb-3">
      <router-link :to="{ name: 'profile', params: { username: review.user.username } }" class="text- alice-Bold ml-1 mr-1">
        {{ review.user.username }} |
      </router-link>
      <p v-if="!isEditing" class="text-lg alice-Bold pl-1 pt-1">{{stars}}</p>
      <form v-if="isEditing">
        <div class="star-rating mb-2">
          <input type="radio" id="10-stars-edit" name="rating" value="10" v-model="payload.content.vote"/>
          <label for="10-stars-edit" class="star">&#9733;</label>
          <input type="radio" id="9-stars-edit" name="rating" value="9" v-model="payload.content.vote"/>
          <label for="9-stars-edit" class="star">&#9733;</label>
          <input type="radio" id="8-stars-edit" name="rating" value="8" v-model="payload.content.vote"/>
          <label for="8-stars-edit" class="star">&#9733;</label>
          <input type="radio" id="7-stars-edit" name="rating" value="7" v-model="payload.content.vote"/>
          <label for="7-stars-edit" class="star">&#9733;</label>
          <input type="radio" id="6-star-edit" name="rating" value="6" v-model="payload.content.vote"/>
          <label for="6-star-edit" class="star">&#9733;</label>
          <input type="radio" id="5-stars-edit" name="rating" value="5" v-model="payload.content.vote"/>
          <label for="5-stars-edit" class="star">&#9733;</label>
          <input type="radio" id="4-stars-edit" name="rating" value="4" v-model="payload.content.vote"/>
          <label for="4-stars-edit" class="star">&#9733;</label>
          <input type="radio" id="3-stars-edit" name="rating" value="3" v-model="payload.content.vote"/>
          <label for="3-stars-edit" class="star">&#9733;</label>
          <input type="radio" id="2-stars-edit" name="rating" value="2" v-model="payload.content.vote"/>
          <label for="2-stars-edit" class="star">&#9733;</label>
          <input type="radio" id="1-star-edit" name="rating" value="1" v-model="payload.content.vote"/>
          <label for="1-star-edit" class="star">&#9733;</label>
          <div class="flex items-end text-box mr-1">
            <p class="alice-reg form-text">평점: </p>
          </div>
        </div>
      </form>


    </div>
    <div class="bg-white my-2 pb-2 rad-5">
    <p v-if="!isEditing" class="text-base alice-reg w-full px-3 pt-2">{{ payload.content.content }}</p>
    <p v-if="isEditing" class="w-full px-auto">
      <input type="text" v-model="payload.content.content" autofocus class="alice-reg w-full p-2 h-20 mb-3 bg-gray border-gray mx-auto">
    </p>

    <div class="flex flex-col items-end mr-3">
      <div class="flex items-baseline">
        <span v-if="current === review.user.username && !isEditing">
          <button @click="switchIsEditing" class="text-sm alice-reg">Edit</button> ⁝
          <button @click="deleteReview(payload)" class="text-sm alice-reg">Delete</button>
        </span>
        <span v-if="isEditing">
          <button @click="onUpdate" class="text-sm alice-reg">Update</button> |
          <button @click="switchIsEditing" class="text-sm alice-reg">Cancel</button>
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
      editedVote: 0,
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
  background-color: #fafafa;
}
.border-gray{
  border: solid 0.5px #8c8c8c;
}

.star {
  display: flex;
  align-items:center;
}

.form-text{
  font-size:15px;
}

.text-box{
  padding-bottom:0.5px;
}

.star-rating {  
  display:flex;
  flex-direction: row-reverse;
  font-size:20px;
  justify-content:space-around;
  padding:0.2em;
  text-align:center;
  width:17rem;
}

.star-rating input {
  display:none;
}

.star-rating label {
  color:#ccc;
  cursor:pointer;
}

.star-rating :checked ~ label {
  color:#f90;
}

.star-rating label:hover,
.star-rating label:hover ~ label {
  color:#fc0;
}

.review-form{
  border: solid 1px #e6e5e5 !important;
  background-color: #F2EEF6;
  border-radius:5px;
}
</style>