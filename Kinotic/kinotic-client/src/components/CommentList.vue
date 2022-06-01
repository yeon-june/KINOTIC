<template>
  <div class="comment-list">

    <ul>
      <comment-list-item 
        v-for="comment in comments" 
        :comment="comment" 
        :key="comment.pk">
      </comment-list-item>        
    </ul>

  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem.vue'
// import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'CommentList',
  components: {CommentListItem },
  props: { comments: Array },
}
</script>

<style scoped>

</style>