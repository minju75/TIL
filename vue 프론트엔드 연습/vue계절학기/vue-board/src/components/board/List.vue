<template>
  <b-container class="bv-example-row mt-3">
    <b-row>
      <b-col>
        <h3>글목록</h3>
      </b-col>
    </b-row>
    <b-row class="mb-1">
      <b-col style="text-align: right;">
        <b-button variant="outline-primary" @click="writeArticle"
          >글쓰기</b-button
        >
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <b-table
          striped
          hover
          :items="items"
          :fields="fields"
          @row-clicked="viewArticle"
        >
        </b-table>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import Vue from "vue";
import VueRouter from "vue-router";
import { listArticle } from "@/api/board.js"

Vue.use(VueRouter);

export default {
  name: "list",
  data() {
    return {
      fields: [
        { key: "articleno", label: "글번호", tdClass: "tdClass" },
        { key: "subject", label: "제목", tdClass: "tdSubject" },
        { key: "userid", label: "작성자", tdClass: "tdClass" },
        { key: "hit", label: "조회수", tdClass: "tdClass" },
        { key: "regtime", label: "작성일", tdClass: "tdClass" }
      ],
      items: []
      //   {
      //     articleno: 10,
      //     subject: "제목입니다.10",
      //     userid: "kimssafy",
      //     hit: 10,
      //     regtime: "20.11.25"
      //   },
      //   {
      //     articleno: 9,
      //     subject: "제목입니다.9",
      //     userid: "parkssafy",
      //     hit: 20,
      //     regtime: "20.11.24"
      //   },
      //   {
      //     articleno: 8,
      //     subject: "제목입니다.8",
      //     userid: "choissafy",
      //     hit: 20,
      //     regtime: "20.11.24"
      //   },
      //   {
      //     articleno: 7,
      //     subject: "제목입니다.7",
      //     userid: "leessafy",
      //     hit: 70,
      //     regtime: "20.11.23"
      //   },
      //   {
      //     articleno: 6,
      //     subject: "제목입니다.6",
      //     userid: "hongssafy",
      //     hit: 50,
      //     regtime: "20.11.22"
      //   },
      //   {
      //     articleno: 5,
      //     subject: "제목입니다.5",
      //     userid: "kangssafy",
      //     hit: 20,
      //     regtime: "20.11.22"
      //   }
      // ]
    };
  },
  created() {
    let para = {
      pg: 1,
      spp: 20,
      key: '',
      word: '',
    };
    listArticle(
      para,
      (response) => {
        console.log(response)
        this.items = response.data
      },
      (error) => {
        console.log(error)
      }
    )
  },
  methods: {
    writeArticle() {
      this.$router.push({ name: "board-register" });
    },
    viewArticle(item) {
      console.log(item.articleno + "글보자!!");
      this.$router.replace({
        name: "board-view",
        params: { articleno: item.articleno }
      });
      // this.$router.push({ path: `/board/view/${item.articleno}` });
    }
  }
};
</script>

<style scope>
.tdClass {
  width: 50px;
  text-align: center;
}
.tdSubject {
  width: 300px;
  text-align: left;
}
</style>