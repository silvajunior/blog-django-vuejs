<template>
    <div class="container">
      <h1 class="title">Blog Posts</h1>
  
      <!-- Formulário para criar um novo post -->
      <div class="new-post-form">
        <input v-model="newPost.title" placeholder="Title" class="input" />
        <textarea v-model="newPost.content" placeholder="Content" class="textarea"></textarea>
        <button @click="createPost" class="btn">Create Post</button>
      </div>
  
      <!-- Lista de posts -->
      <div v-if="posts.length">
        <ul class="posts-list">
          <li v-for="post in posts" :key="post.id" class="post-item">
            <h2>{{ post.title }}</h2>
            <p>{{ post.content }}</p>
            <div class="post-actions">
              <button @click="editPost(post)" class="btn btn-edit">Edit</button>
              <button @click="deletePost(post.id)" class="btn btn-delete">Delete</button>
            </div>
          </li>
        </ul>
      </div>
      <p v-else>Loading...</p>
  
      <!-- Formulário para editar um post -->
      <div v-if="editingPost" class="edit-post-form">
        <input v-model="editingPost.title" placeholder="Title" class="input" />
        <textarea v-model="editingPost.content" placeholder="Content" class="textarea"></textarea>
        <button @click="updatePost" class="btn btn-update">Update Post</button>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        posts: [],
        newPost: { title: '', content: '' },
        editingPost: null,
      };
    },
    created() {
      this.fetchPosts();
    },
    methods: {
      async fetchPosts() {
        try {
          const response = await axios.get('http://localhost:8000/api/posts/');
          this.posts = response.data;
        } catch (error) {
          console.error(error);
        }
      },
  
      async createPost() {
        try {
          const response = await axios.post('http://localhost:8000/api/posts/create/', this.newPost);
          this.posts.push(response.data);
          this.newPost = { title: '', content: '' }; // Limpa o formulário
        } catch (error) {
          console.error(error);
        }
      },
  
      async deletePost(id) {
        try {
          await axios.delete(`http://localhost:8000/api/posts/${id}/`);
          this.posts = this.posts.filter(post => post.id !== id);
        } catch (error) {
          console.error(error);
        }
      },
  
      editPost(post) {
        this.editingPost = { ...post }; // Copia o post para editar
      },
  
      async updatePost() {
        try {
          const response = await axios.put(`http://localhost:8000/api/posts/${this.editingPost.id}/`, this.editingPost);
          const index = this.posts.findIndex(post => post.id === this.editingPost.id);
          this.$set(this.posts, index, response.data);
          this.editingPost = null; // Limpa o formulário de edição
        } catch (error) {
          console.error(error);
        }
      }
    }
  }
  </script>
  
  <style scoped>
  /* Estilos para o layout */
  .container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .title {
    text-align: center;
    font-size: 36px;
    margin-bottom: 20px;
  }
  
  .new-post-form, .edit-post-form {
    margin-bottom: 20px;
  }
  
  .input, .textarea {
    width: 100%;
    padding: 10px;
    margin: 10px 0;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .btn {
    padding: 10px 20px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .btn:hover {
    background-color: #45a049;
  }
  
  .btn-edit {
    background-color: #f0ad4e;
  }
  
  .btn-edit:hover {
    background-color: #ec971f;
  }
  
  .btn-delete {
    background-color: #d9534f;
  }
  
  .btn-delete:hover {
    background-color: #c9302c;
  }
  
  .posts-list {
    list-style-type: none;
    padding: 0;
  }
  
  .post-item {
    border-bottom: 1px solid #ccc;
    padding: 10px;
    margin-bottom: 10px;
  }
  
  .post-actions {
    margin-top: 10px;
  }
  
  .post-actions button {
    margin-right: 10px;
  }
  </style>
  