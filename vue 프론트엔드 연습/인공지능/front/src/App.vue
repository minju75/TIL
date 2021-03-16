<template>

    <v-main style="background-color: #192537;">
      <HelloWorld/>
    </v-main>

</template>

<script>
import HelloWorld from './components/HelloWorld';

export default {
  name: 'App',

  components: {
    HelloWorld,
  },

  data: () => ({
    //
  }),
};
</script>

<style>
    * {
    font-family: "MapoFlowerIsland";
    color: white;
  }
  @font-face {
    font-family: "MapoFlowerIsland";
    src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/MapoFlowerIslandA.woff")
      format("woff");
    font-weight: normal;
    font-style: normal;
  }
</style>
