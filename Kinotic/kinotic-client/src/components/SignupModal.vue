<template lang="html">
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper" @click="outerClick($event)" id="out">
        <div class="modal-container">
          <div class="modal-header flex justify-between">
            <slot name="header">
            </slot>
            <button @click="$emit('close')" class="text-xl">X</button>
          </div>
          <hr class="mt-1 mb-3">
          <div class="modal-body">
            <slot name="body">
              <!--  -->
            </slot>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>

export default {
  name:"ListDetailModal",
  methods:{
    outerClick(e){
      console.log('click')
      if(e.target.id==='out'){
        this.$emit('close')
      }
    }
  },
}
</script>



<style lang="css">
.closeModalBtn {
  color: #62acde;
}
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  transition: opacity .3s ease;
}
.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}
.modal-container {
  overflow-y: auto;
  width: 750px;
  height: 83vh;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, .33);
  transition: all .3s ease;
  font-family: Helvetica, Arial, sans-serif;
  border-radius: 5px;
  background-color: #fffdff
}

.modal-header{
  height:45px;
}

.modal-body {
  margin: 20px 0;
}
.modal-default-button {
  float: right;
}
/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */
.modal-enter {
  opacity: 0;
}
.modal-leave-active {
  opacity: 0;
}
.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}

.modal-container::-webkit-scrollbar {
    width: 6px;  /* 스크롤바의 너비 */
}

.modal-container::-webkit-scrollbar-thumb {
    height: 20%; /* 스크롤바의 길이 */
    background: #9486CD; /* 스크롤바의 색상 */
    
    border-radius: 10px;
}

.modal-container::-webkit-scrollbar-track {
    background: rgba(141, 40, 235, 0.1);  /*스크롤바 뒷 배경 색상*/
}

</style>