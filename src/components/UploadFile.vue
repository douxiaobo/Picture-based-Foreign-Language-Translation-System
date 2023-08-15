<template>
    <div>
      UpLoad File:
      <br>
      <el-button type="primary" @change="handleFileUpload">Choose File</el-button>
      <el-input v-model="input" disabled placeholder="No file Chosen" />
      

      <el-button type="primary" icon="Upload" @click="uploadFile">Upload</el-button>
      <br>
      <el-tag class="m1-2" type="info">Uploaded file:</el-tag>
      <el-tag class="m1-2" type="danger"> {{ uploadedFile }}</el-tag>
      <br>

      <input type="file" ref="fileInput" @change="handleFileUpload" />
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
  </script>