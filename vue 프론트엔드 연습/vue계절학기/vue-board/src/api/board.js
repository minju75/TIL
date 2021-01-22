import { createInstance } from "./index.js";

const instance = createInstance();
// const config = {
//   headers: { "access-token": localStorage.getItem("access-token") }
// };

function listArticle(para, success, fail) {
  instance
    .get(`article`, { params : para })
    .then(success)
    .catch(fail)
};

function registerArticle(article, success, fail) {
  instance
    .post(`article`, JSON.stringify(article))
    .then(success)
    .catch(fail)
};

function getArticle(articleno, success, fail) {
  instance
    .get(`article/${articleno}`)
    .then(success)
    .catch(fail)
};

function modifyArticle(article, success, fail) {
  instance
    .put(`article`, JSON.stringify(article))
    .then(success)
    .catch(fail)
};

function deleteArticle(articleno, success, fail) {
  instance
    .delete(`article/${articleno}`)
    .then(success)
    .catch(fail)
};

function createComment(comment, success, fail) {
  instance
    .psost(`Comment`, JSON.stringify(comment))
    .then(success)
    .catch(fail)
};

export { listArticle, registerArticle, getArticle, deleteArticle, modifyArticle };