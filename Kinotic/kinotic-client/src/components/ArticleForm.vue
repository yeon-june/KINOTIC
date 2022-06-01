<template>
  <form @submit.prevent="onSubmit" class="py-6 px-8">
    <div class="flex flex-col mb-5">
      <label for="title" class="alice-Bold f-5353">TITLE </label>
      <input v-model="newArticle.title" type="text" id="title" class="border w-full mt-2 h-8 px-2" required/>
    </div>
    <div class="flex flex-col mb-6">
      <label for="content" class="alice-Bold f-5353">CONTENT </label>
      <textarea v-model="newArticle.content" type="text" id="content" class="border w-full vh-45 mt-2 px-2" required></textarea>
    </div>
    <div>
      <button class="w-full py-2 flex justify-center items-center alice-Bold f-6161 text-base">{{ action }}</button>
    </div>
  </form>
</template>

<script>
import { mapActions } from 'vuex'

  export default {
    name: 'ArticleForm',
    props: {
      article: Object,
      action: String,
    },
    data() {
      return {
        newArticle: {
          title: this.article.title,
          content: this.article.content,
        }
      }
    },

    methods: {
      ...mapActions(['createArticle', 'updateArticle']),
      onSubmit() {
        if (this.action === 'create') {
          this.createArticle(this.newArticle)
        } else if (this.action === 'update') {
          const payload = {
            pk: this.article.pk,
            ...this.newArticle,
          }
          this.updateArticle(payload)
        }
      },
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
.border{
  border: solid 0.1px #e0e0e0;
  border-radius: 5px;
  box-shadow: rgba(0, 0, 0, 0.06) 0px 2px 4px 0px inset;
}

.f-5353{
  color:#444444;
}


.f-6161{
  color:#616161;
}

.vh-45{
  height: 40vh;
}

button{
  background-color: #dcd3e6;
  border-radius: 5px;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 12px;
}

input:focus {outline:2px solid #c3b7cf;}
textarea:focus {outline:2px solid #c3b7cf;}

</style>
