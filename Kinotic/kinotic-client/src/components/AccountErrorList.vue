<template>
  <div class="account-error-list mb-4">
    <p v-for="(errors, field) in authError" :key="field" class="bc-bold flex flex-col items-center">
      {{ field }} ERROR
      
      <ul>
        <li v-for="(error, idx) in errors" :key="idx" class="text-xs bc-bold">
          {{ error }}
        </li>
      </ul>
    </p>

  </div>
</template>

<script>
  import { mapGetters } from 'vuex'
  
  export default {
    name: 'AccountErrorList',
    computed: {
      ...mapGetters(['authError'])
    },
  }
</script>

<style scoped>
@font-face {
    font-family: 'paybooc-Bold';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-07@1.0/paybooc-Bold.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
.bc-bold{
    font-family: 'paybooc-Bold';

}
  .account-error-list {
    color: rgb(122, 44, 248);
  }
</style>
