<template>  
  <div id="app">
    <nav-header></nav-header>
    <router-view></router-view>
    <nav-footer></nav-footer>
  </div>
  
</template>

<script>
// import HelloWorld from "./components/HelloWorld";
import NavHeader from "./components/Header.vue";
import NavFooter from "./components/Footer.vue";

export default {
  name: "App",

  components: {
    NavHeader,
    NavFooter,
    
  },

  data: () => ({
    //
  })
};
</script>
<style>
  ul,li{list-style:none;}
</style>