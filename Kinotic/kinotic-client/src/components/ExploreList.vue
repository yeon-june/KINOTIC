<template>
  <div class="grid grid-cols-4 gap-4">
    <MovieCard
      v-for="content in contents"
      :key="content.pk"
      :content="content"
    />
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'
import {mapGetters} from 'vuex'

export default {
  name:'ExploreList',
  computed: {
    ...mapGetters(['movies']),
    contents(){
      return this.movies?.slice(20*(this.page-1),20*this.page)
    }
  },
  props: {
    page:{
      type:Number,
      required:true,
    }
  },

  components:{
    MovieCard,
  },
}
</script>

<style scoped>

</style>