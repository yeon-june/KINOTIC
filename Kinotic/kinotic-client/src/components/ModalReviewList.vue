<template>
  <div class="grid grid-cols-5 gap-4">
    <ReviewComponent
      v-for="content in contents"
      :key="content.pk"
      :content="content"
    />
  </div>
</template>

<script>
import ReviewComponent from '@/components/ReviewComponent.vue'
import {mapGetters} from 'vuex'

export default {
  name:'ModalList',
  computed: {
    ...mapGetters(['movies']),
  },
  props: {
    contents:{
      type:Array,
    }
  },

  components:{
    ReviewComponent
  },
  created(){
    console.log(this.contents[0])
  }
}
</script>

<style scoped>

</style>