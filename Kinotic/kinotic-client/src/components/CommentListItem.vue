<template>
  <div class="my-1">
    <router-link :to="{ name: 'profile', params: { username: comment.user.username } }" class="alice-Bold ml-1 mr-2">
      {{ comment.user.username }}
    </router-link> 
    <span v-if="current === comment.user.username && !isEditing">
      <button @click="switchIsEditing" class="alice-reg text-xs">Edit</button> ⁝
      <button @click="deleteComment(payload)" class="alice-reg text-xs">Delete</button>
    </span>
    <span v-if="isEditing">
      <button @click="onUpdate" class="alice-reg text-xs">Update</button> |
      <button @click="switchIsEditing" class="alice-reg text-xs">Cancel</button>
    </span>
    <div class="comment-list-item p-2 mt-1">
    <p v-if="!isEditing" class="alic-reg">{{ payload.content }}</p>
    <input v-if="isEditing" type="text" v-model="payload.content" class="w-full px-1">
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        articlePk: this.comment.article,
        commentPk: this.comment.pk,
        content: this.comment.content
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
    current() {
      return localStorage.getItem('currentUser')
    }
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style scoped>
.alice-Bold{
  font-family: 'EliceDigitalBaeum_Bold';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_220508@1.0/EliceDigitalBaeum_Bold.woff2') format('woff2');
  font-weight: 700;
  font-style: normal;
}

.alice-reg {
    font-family: 'EliceDigitalBaeum_Regular';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_220508@1.0/EliceDigitalBaeum_Regular.woff2') format('woff2');
    font-weight: 400;
    font-style: normal;
}

.comment-list-item{
  background-color:#f1f5f8;
  border-radius: 5px;
}

</style>