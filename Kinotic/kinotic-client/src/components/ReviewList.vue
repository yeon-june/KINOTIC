<template>
  <div class="comment-list">
    
    <ReviewForm/>
    <hr class="my-3">
    <div>
      <ReviewListItem
        v-for="review in reviews" 
        :review="review" 
        :key="review.pk"/>     
    </div>

  </div>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem.vue'
import ReviewForm from '@/components/ReviewForm.vue'
// import { mapGetters } from 'vuex'


export default {
  name: 'ReviewList',
  components: { 
    ReviewListItem,
    ReviewForm,
   },
  props: { reviews: Array },
  created(){
    console.log(this.reviews)
  },

}
</script>

<style>

</style>