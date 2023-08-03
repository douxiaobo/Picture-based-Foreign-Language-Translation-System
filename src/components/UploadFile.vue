<template>
    <div>
      <input type="file" ref="fileInput" @change="handleFileUpload" />
      <button @click="uploadFile">Upload</button>

      <el-button type="primary">
        Upload<el-icon class="el-icon--right"><UpLoad /></el-icon>
      </el-button>
      
      <p>Uploaded file: {{ uploadedFile }}</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        uploadedFile: '',
      };
    },
    methods: {
      handleFileUpload(event) {
        this.uploadedFile = event.target.files[0].name;
      },
      uploadFile() {
        // TODO: Implement file upload logic
        // This example shows how to use the axios library to upload a file
        const formData = new FormData();
        formData.append('file', this.$refs.fileInput.files[0]);
        
        axios.post('/api/upload', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.log(error);
        });
      },
    },
  };
  import {Upload} from '@element-plus/icons-vue'
  </script>