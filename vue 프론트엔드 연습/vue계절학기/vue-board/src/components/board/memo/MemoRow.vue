<template>
  <b-row class="mb-1">
    <b-col>
      <b-card border-variant="info" class="mb-2" no-body>
        <template>
          <b-row class="m-1">
            <b-col class="text-left ml-3"
              ><strong>{{ comment.userid }}</strong> (20.11.28)
            </b-col>
            <b-col class="text-right mr-3">
              <b-button @click="visual=true" variant="link">수정</b-button>
              <b-button @click="deleteComment" variant="link">삭제</b-button>
            </b-col>
          </b-row>
        </template>
        <b-card-body class="text-left">
          <div v-if="visual">
            <b-input v-model="comment.comment" type="text" />
            <b-button @click="updateComment" >댓글수정</b-button>
          </div>
          <div v-else>
            {{ comment.comment }}
          </div>
        </b-card-body>
      </b-card>
    </b-col>
  </b-row>
</template>

<script>
import { updateComment, deleteComment } from "@/api/memo.js"

export default {
  name: "memorow",
  data: function () {
    return {
      visual: false
    }
  },
  props: {
    comment: [String, Object],
  },
  methods: {
    updateComment: function () {
      this.visual = false
      updateComment(
        this.comment,
        (response) => {
          console.log(response)
          this.$emit('update', response.data)
        },
        (error) => {
          console.log(error)
        }
      )
    },
    deleteComment: function () {
      if (confirm("정말 삭제??")) {
        deleteComment(
          this.comment.articleno,
          this.comment.memono,
          (response) => {
            this.$emit('delete', response.data)
          },
          (error) => {
            console.log(error)
          }
        )
      }
    }
  }
};
</script>

<style></style>
