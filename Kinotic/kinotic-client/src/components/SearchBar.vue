<template>
  <div>
  <form @submit.prevent="onSubmit" class="w-full h-11 flex items-center px-4">
    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
  <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
</svg> 
    <input type="text" class="h-10 w-full px-4" placeholder="찾고싶은 영화 제목을 입력하세요" v-model="keyword">
  </form>
  </div>
</template>

<script>
export default {
  name:"SearchBar",
  data(){
    return{
      keyword: this.searched ? this.searched : '',
    }
  },
  methods:{
    onSubmit(){
      this.$emit('onSubmit', this.keyword) 
      this.keyword = ''    
    },
    onInput(){
      console.log(this.keyword)
    }
  },
  props:{
    searched:{
      type:String,
    }
  },
}
</script>

<style scoped>
form{
  background-color:#f3eef7;
  border-radius:10px;
  box-shadow: rgba(0, 0, 0, 0.05) 0px 1px 2px 0px;
}

input{
  background-color:transparent;
  border-radius:5px;
}
input:focus {
  outline:2px solid #c3b7cf;}
</style>