<template>
  <b-row class="mb-3 mt-2">
    <b-col cols="11">
      <b-form-textarea
        id="content"
        placeholder="댓글 입력..."
        rows="2"
        v-model="memoDto.comment"
      ></b-form-textarea>
    </b-col>
    <b-col><b-button @click="writeComment" variant="dark">댓글등록</b-button> </b-col>
  </b-row>
</template>

<script>
import { createComment } from "@/api/memo.js";

export default {
  name: "memowrite",
  data: function () {
    return {
      memoDto: {
        "articleno" : this.articleno,
        "comment" : "",
        "userid": this.$store.state.userInfo.userid
,      }
    }
  },
  props: {
    articleno: [Number]
  },
  methods: {
    writeComment: function () {
      createComment(
        this.memoDto,
        (response) => {
          console.log(response)
          this.memoDto.comment = ""
          this.$emit('write', response.data)
        },
        (error) => {
          console.log(error)
        }
      )
    }
  }
};
</script>

<style></style>
