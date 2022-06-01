<template>
  <div class="content-card p-3">
    <div class="w-full blank-poster mx-auto mb-2">
    </div>
    <p class="w-full blank-title"></p>
  </div>
</template>

<script>
export default {
  name:"DefaultMovieCard"
}
</script>

<style scoped>
.content-card{
  background-color: white;
  border-radius: 10px;
}

.blank-poster{
  background-color: #E4E9EF;
  height: 150px;
}

.blank-title{
  height:15px;
  background-color: #dfe0e2;
}
</style>