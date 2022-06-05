<template>
  <div>
    <form @submit.prevent="onSubmit()" class="review-form px-3 pb-3 pt-1">
      
      <div class="star-rating mb-2">
        <input type="radio" id="10-stars" name="rating" value="10" v-model="content.vote" :disabled="!isLoggedIn"/>
        <label for="10-stars" class="star">&#9733;</label>
        <input type="radio" id="9-stars" name="rating" value="9" v-model="content.vote" :disabled="!isLoggedIn"/>
        <label for="9-stars" class="star">&#9733;</label>
        <input type="radio" id="8-stars" name="rating" value="8" v-model="content.vote" :disabled="!isLoggedIn"/>
        <label for="8-stars" class="star">&#9733;</label>
        <input type="radio" id="7-stars" name="rating" value="7" v-model="content.vote" :disabled="!isLoggedIn"/>
        <label for="7-stars" class="star">&#9733;</label>
        <input type="radio" id="6-star" name="rating" value="6" v-model="content.vote" :disabled="!isLoggedIn"/>
        <label for="6-star" class="star">&#9733;</label>
        <input type="radio" id="5-stars" name="rating" value="5" v-model="content.vote" :disabled="!isLoggedIn"/>
        <label for="5-stars" class="star">&#9733;</label>
        <input type="radio" id="4-stars" name="rating" value="4" v-model="content.vote" :disabled="!isLoggedIn"/>
        <label for="4-stars" class="star">&#9733;</label>
        <input type="radio" id="3-stars" name="rating" value="3" v-model="content.vote" :disabled="!isLoggedIn"/>
        <label for="3-stars" class="star">&#9733;</label>
        <input type="radio" id="2-stars" name="rating" value="2" v-model="content.vote" :disabled="!isLoggedIn"/>
        <label for="2-stars" class="star">&#9733;</label>
        <input type="radio" id="1-star" name="rating" value="1" v-model="content.vote" :disabled="!isLoggedIn"/>
        <label for="1-star" class="star">&#9733;</label>
        <div class="flex items-end text-box mr-1">
          <p class="alice-reg form-text">평점: </p>
        </div>
      </div>
      <div class="flex flex-col px-1 ">
        <input type="text" v-model="content.content" class="alice-reg w-full px-3 py-2 h-20 mb-3" :disabled="!isLoggedIn" :placeholder="placeHolder" required>
        <div class="flex justify-end px-1">
          <button class="p-1 alice-reg">작성</button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name:'ReviewForm',
  data() {
    return{
      content: {
        content:'',
        vote: 0,
      },
    }
  },
  computed: {
    ...mapGetters(['isLoggedIn']),
    moviePk(){
      return this.$route.params.moviePk
    },
    placeHolder(){
      return this.isLoggedIn ? '리뷰를 작성해 주세요' : '리뷰를 작성하려면 로그인 해주세요'
    }
  },
  methods: {
    ...mapActions(['createReview']),
    onSubmit() {
      console.log(this.content )
      this.createReview({ moviePk: this.moviePk, content: this.content })
      this.content.content = ''
      this.content.vote = 0
    }
  },
}
</script>

<style scoped>
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


input{
  border-radius: 5px;
}

button{
  background-color: #ffefb5;
  width: 12%;
  font-size:15px;
  border-radius: 3px;
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

input[type="text"]:disabled {
  background: rgb(235, 235, 235);
  border: 0.1px solid white;
}
</style>