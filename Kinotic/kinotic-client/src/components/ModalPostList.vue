<template>
  <div class="grid grid-cols-5 gap-4">
    <PostComponent
      v-for="content in contents"
      :key="content.pk"
      :content="content"
    />
  </div>
</template>

<script>
import PostComponent from '@/components/PostComponent.vue'
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
    PostComponent
  },
  created(){
    console.log(this.contents[0])
  }
}
</script>

<style scoped>

</style>