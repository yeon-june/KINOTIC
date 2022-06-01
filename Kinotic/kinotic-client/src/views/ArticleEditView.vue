<template>
  <div>
    <img src="@/assets/ArticleEdit.png" class="w-3/12 mx-auto mt-vh3 mb-3" alt="">
    <hr>
    <article-form v-if="isArticle" :article="article" action="update" class="mt-vh1">

    </article-form>
  </div>

</template>

<script>
import ArticleForm from '@/components/ArticleForm.vue'
import { mapGetters, mapActions } from 'vuex'
  export default {
    name: 'AritcleEditView',
    components: { ArticleForm },
    computed: {
      ...mapGetters(['article', 'isArticle',])
    },
    methods: {
      ...mapActions(['fetchArticle'])
    },
    created() {
      this.fetchArticle(this.$route.params.articlePk)
    },
  }
</script>

<style scoped>
.mt-vh3{
  margin-top:3vh;
}
.mt-vh1{
  margin-top:1vh
}
</style>
