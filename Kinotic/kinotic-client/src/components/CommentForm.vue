<template>
  <div>
    <form @submit.prevent="onSubmit()" class="comment-form px-3 py-3">
      <p class="alice-reg mb-2 text-base">댓글 작성</p>
      <input type="text" v-model="content" class="alice-reg w-full p-2 h-50 mb-2 radius-5 input-box" :disabled="!isLoggedIn" :placeholder="placeHolder" required>
      <div class="flex justify-end">
        <button class="submit-btn text-sm py-1">작성</button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name:'CommentForm',
  data() {
    return{
      content: '',
    }
  },
  computed: {
    ...mapGetters(['article', 'isLoggedIn']),
    articlePk(){
      return this.article.pk
    },
    placeHolder(){
      return this.isLoggedIn ? '댓글을 작성해 주세요' : '댓글을 작성하려면 로그인 해주세요'
    }
  
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      this.createComment({ articlePk: this.articlePk, content: this.content, })
      this.content = ''
    }
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
.alice-Bold{
    font-family: 'EliceDigitalBaeum_Bold';

}
.alice-reg {
    font-family: 'EliceDigitalBaeum_Regular';
}
.comment-form{
  border: solid 1px #e6e5e5 !important;
  background-color: #F2EEF6;
  border-radius:5px;
}

.submit-btn{
  background-color: #ffefb5;
  width: 12%;
  font-size:14px;
  border-radius: 3px;
}

.h-50{
  height:50px;
}

.radius-5{
  border-radius:5px;
}

.input-box{
  background-color: white;
  box-shadow: rgba(0, 0, 0, 0.03) 0px 2px 4px 0px inset;
}

input[type="text"]:disabled {
  background: rgb(235, 235, 235);
  border: 0.1px solid white;
}
</style>