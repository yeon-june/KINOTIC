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
  },
  props: {
    contents:{
      type:Array,
    }
  },

  components:{
    MovieCard,
  },
  created(){
    console.log(this.contents[0])
  }
}
</script>

<style scoped>

</style>