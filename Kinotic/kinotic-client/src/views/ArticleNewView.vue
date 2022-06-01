<template>
  <div>
    <img src="@/assets/NewArticle.png" class="w-3/12 mx-auto mt-5 mb-3" alt="">
    <hr>
    <ArticleForm :article="article" action="create"></ArticleForm>
  </div>
</template>

<script>
import ArticleForm from '@/components/ArticleForm.vue'
export default {
  name: 'AritcleNewView',
  components: { ArticleForm },
  data() {
    return {
      article: {
        pk: null,
        title: '',
        content: '',
      }
    }
  },
}
</script>

<style scoped>
</style>
