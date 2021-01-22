import { createInstance } from "./index.js";

const instance = createInstance();
// const config = {
//   headers: { "access-token": localStorage.getItem("access-token") }
// };

function readComment(articleno, success, fail) {
  instance
    .get(`memo/${articleno}`)
    .then(success)
    .catch(fail)
};

function createComment(comment, success, fail) {
  instance
    .post(`memo`, JSON.stringify(comment))
    .then(success)
    .catch(fail)
};

function updateComment(comment, success, fail) {
  instance
    .put(`memo`, JSON.stringify(comment))
    .then(success)
    .catch(fail)
};

function deleteComment(articleno, menono, success, fail) {
  instance
    .delete(`memo/${articleno}/${menono}`)
    .then(success)
    .catch(fail)
};


export { createComment, readComment, updateComment, deleteComment };