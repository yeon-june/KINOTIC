<template>
  <div class="w-97 mx-auto">
    <p class="title alice-Bold mt-4">{{ article.title }}</p>
    <div class="flex items-baseline mb-2">
      <p class="text-sm mr-1">작성자:</p>
      <router-link :to="{name: 'profile', params: {'username': article.user.username} }" class="text-sm">{{article.user.username}}</router-link>
      <p class="text-sm mx-2">⁝</p>
      <p class="text-sm mr-1">작성일:</p>
      <p class="text-sm">{{ article.created_at | yyyyMMddhhmm}}</p>
      <p class="text-sm mx-2">⁝</p>
      <div>
        Likeit:
        <button
          @click="ifLogLike" class="text-sm"
        >{{ like_icon }}</button>
      </div>
    </div>
    <div class="content-box p-3 flex flex-col justify-between">
    <p class=" text-lg alice-reg">
      {{ article.content }}
    </p>
    <div v-if="isAuthor" class="flex justify-end items-baseline mr-1">
      <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
        <button class="text-sm alice-reg">Edit</button>
      </router-link>
      <p class="mx-1 text-sm alice-reg">⁝</p>
      <button @click="deleteArticle(articlePk)" class="text-sm alice-reg">Delete</button>
    </div>
    </div>
    <!-- Article Edit/Delete UI -->

    <div class="h-8"></div>

    <!-- Comment UI -->
    <CommentForm/>
    <hr class="my-4">
    <comment-list :comments="article.comments"></comment-list>

  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/CommentList.vue'
  import CommentForm from '@/components/CommentForm.vue'



  export default {
    name: 'ArticleDetailView',
    components: { 
      CommentList,
      CommentForm
       },
    data() {
      return {
        articlePk: this.$route.params.articlePk,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'article', 'isLoggedIn']),

      likeCount() {
        return this.article?.like_users?.length
      },
      current() {
        return localStorage.getItem('currentUser')
      },
      like_usernames() {
        return this.article?.like_users.map ((user)=> {
          return user?.username
        })
      },
      liking() {
        return this?.like_usernames.includes(this.current)
      },
      like_icon() {
        if (this.liking){
          return '💜'
        } else { 
          return '🖤'
        }
      },

    },
    methods: {
      ...mapActions([
        'fetchArticle',
        'likeArticle',
        'deleteArticle',
      ]),
      ifLogLike(){
        if (this.isLoggedIn) {
          this.likeArticle(this.articlePk)
        } else{
          window.location.href = '/login'
        }
      },
    },
    created() {
      this.fetchArticle(this.articlePk)
      console.log(this.article)
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

.w-97{
  width:97%;
}

.title{
  font-size: 30px;
}
.alice-Bold{
  font-family: 'EliceDigitalBaeum_Bold';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_220508@1.0/EliceDigitalBaeum_Bold.woff2') format('woff2');
  font-weight: 700;
  font-style: normal;
}

.content-box{
  min-height:300px;
  border: solid 0.1px #dddddd;
  border-radius: 5px;
  box-shadow: rgba(0, 0, 0, 0.04) 0px 2px 4px 0px inset;
}
</style>
