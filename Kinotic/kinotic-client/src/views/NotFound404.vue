<template>
  <div id="wrap">
    <div id="center">
    <img class="not-found mx-auto flex justify-center" src="@/assets/page404.png" alt="not-found">
    <p class="text-center mt-1 text-lg">
      Click 
    <a href="http://localhost:8080/" class="text-2xl col-p">HERE</a>
      to go home.
    </p>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'NotFound404',
  }
</script>

<style scoped>
#wrap {
  display: grid;
  place-items: center;
  min-height: 90vh;
}

  img.not-found {
    width: 90%;
    margin: 0;
  }

.col-p{
  color:rgb(104, 62, 144);
  font-weight: 900;
}
</style>
