<template>
  <b-container class="bv-example-row mt-3">
    <b-row>
      <b-col>
        <h3>글보기</h3>
      </b-col>
    </b-row>
    <b-row class="mb-1">
      <b-col class="text-left">
        <b-button variant="outline-primary" @click="listArticle">목록</b-button>
      </b-col>
      <b-col class="text-right">
        <b-button
          variant="outline-info"
          size="sm"
          @click="moveModifyArticle"
          class="mr-2"
          >글수정</b-button
        >
        <b-button variant="outline-danger" size="sm" @click="deleteArticle"
          >글삭제</b-button
        >
      </b-col>
    </b-row>
    <b-row class="mb-1">
      <b-col>
        <b-card
          :header-html="
            `<h3>${article.articleno}.
          ${article.subject}</h3><h6>${article.userid} ${article.regtime}</h6>`
          "
          class="mb-2"
          border-variant="dark"
          no-body
        >
          <b-card-body class="text-left">
            <div>
              <template v-for="(msg, index) in message">
                {{ msg }}<br :key="index" />
              </template>
            </div>
          </b-card-body>
        </b-card>
      </b-col>
    </b-row>
    <!-- 댓글 -->
    <memo-write 
      :articleno="articleno" 
      @write = "writeMemo"/>
    <memo-row 
      v-for="(memo, index) in memos" 
      :key="index" :comment ="memo" 
      @delete = "deleteMemo" 
      @update = "updateMemo" />
  </b-container>
</template>

<script>
import MemoWrite from "./memo/MemoWrite"
import MemoRow from "./memo/MemoRow"
import { getArticle, deleteArticle } from "@/api/board.js"
import { createComment } from "@/api/memo.js"

export default {
  name: "detail",
  components: {
    MemoWrite,
    MemoRow
  },
  data() {
    const articleno = Number(this.$route.params.articleno)
    console.log(articleno + "번글입니다.")
    return {
      articleno: Number(this.$route.params.articleno),
      article: {
        articleno: articleno,
        subject: "",
        content:"",
        userid: "",
        hit: 0,
        regtime: ""
      },
      memos: []
    };
  },
  created: function () {
    getArticle(
      this.$route.params.articleno,
      (response) => {
        this.article = response.data;
      },
      (error) => {
        console.log(error);
      }
    );
    createComment (
      this.$route.params.articleno,
      (response) => {
        console.log(response.data)
        this.comment = response.data
      },
      (error) => {
        console.log(error)
      }
    )
  },
  computed: {
    message: function() {
      return this.article.content.split("\n")
    }
  },
  methods: {
    writeMemo (data) {
      this.comments = data
    },
    deleteComment (data) {
      this.comments = data
    },
    updateComment (data) {
      this.comments = data
    },
    listArticle() {
      this.$router.push({ name: "board-list" })
    },
    moveModifyArticle() {
      this.$router.replace({
        name: "board-modify",
        params: { articleno: this.article.articleno }
      });
      //   this.$router.push({ path: `/board/modify/${this.articleno}` });
    },
    deleteArticle() {
      console.log(this.article.articleno + "글삭제!!")
      if (confirm("정말로 삭제하시겠습니까?")){
        deleteArticle(
          this.$route.params.articleno,
          (response) => {
            this.article = response.data
            this.$router.push({ name: "board-list" })
          },
          (error) => {
            console.log(error)
          }
        );
      }
    }
  }
};
</script>

<style></style>
