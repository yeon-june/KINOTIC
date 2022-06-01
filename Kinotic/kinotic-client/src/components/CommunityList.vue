<template>
  <div id="list-box">
      <ArticleComponent 
        v-for="article in articleLst"
        :key="article.pk"
        :article="article"
        class="mx-auto"
      />
  </div>
</template>

<script>
import ArticleComponent from '@/components/ArticleComponent.vue'
import { mapGetters } from 'vuex'

export default {
  name:"CommunityList",
  components: {
    ArticleComponent
  },
  computed: {
    ...mapGetters(['articles']),
    articleLst(){
      return this.articles?.slice(7*(this.page-1),7*this.page)
    }
  },
  props: {
    page:{
      type:Number,
      required:true,
    }
  },

}
</script>

<style scoped>
#list-box{
  border-top: 0.1px solid #cacaca;
  border-bottom: 0.1px solid #cacaca;
  padding-top: 1.5%;
  padding-bottom: 1.5%;
}

</style>