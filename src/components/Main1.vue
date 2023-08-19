<template>  
    <div class="container">
        <div class="column left"> 

          
            <div class="image-container">
                <el-upload v-if="!imageUrl" class="upload-demo" drag action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"  multiple   >
                    <el-icon class="el-icon--upload"><upload-filled /></el-icon>
                    <div class="el-upload__text">
                        Drop file here or <em>click to upload</em>
                    </div>    
                </el-upload>
                <input v-if="!imageUrl" type="file" @change="onImageSelected" accept="image/*" round />
                <!-- <el-dialog v-else v-model="dialogVisible"> -->
                    <el-image v-else fit="cover" :src="imageUrl" />
                <!-- </el-dialog> -->
                
            </div> 
            <div>
                <el-row class="row-bg" justify="center" >
                    <el-col :span="6"><div class="grid-content ep-bg-purple" />
                        <el-button type="primary" round v-if="imageUrl" @click="clearImage" size="large">Clear Image</el-button>
                    </el-col>
                </el-row>          
            </div>     
            
            
        </div>
    <div class="column right">  
        <div class="box">{{ responseText }}</div>
        
        <el-row class="row-bg" justify="space-evenly">

            <el-col :span="6"><div class="grid-content ep-bg-purple" />
                <el-select v-model="originlanguage" class="m-2" placeholder="Select" size="large">
                    <el-option v-for="item in originlanguageDict" :key="item" :label="item" :value="item" />
                </el-select>
            </el-col>

          <el-col :span="6"><div class="grid-content ep-bg-purple-light" />
            <el-button type="primary" @click="demoHandler" round class="buttoncenter" size="large">Translate</el-button>
          </el-col>

          <el-col :span="6"><div class="grid-content ep-bg-purple" />
            <el-select v-model="targetlanguage" class="m-2" placeholder="Select" size="large">
              <el-option v-for="item in targetlanguageDict" :key="item" :label="item" :value="item" />
            </el-select>
          </el-col>

        </el-row>
          
      </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';

export default {
  data() {
    return {
      imageUrl: null,
      responseText: "",
      originlanguage: "English",
      targetlanguage: "Chinese",
      originlanguageDict: [
        "Chinese",
        "English",
        "Spanish",
        "French",
        "Russian",
        "Arabic",
        "German",
        "Japanese",
        "Korean",
      ],
      targetlanguageDict: [
        "Chinese",
        "English",
        "Spanish",
        "French",
        "Russian",
        "Arabic",
        "German",
        "Japanese",
        "Korean",
      ],
    };
  },
  methods: {
    async onImageSelected(event) {
      const file = event.target.files[0];
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = () => {
        this.imageUrl = reader.result;
      };

      const formData = new FormData();
      formData.append("image", file);
      formData.append("origin_language", this.originlanguage);
      formData.append("target_language", this.targetlanguage);

      try {
        const response = await axios.post("http://127.0.0.1:8000/api/translateimagetext", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });
        this.responseText = response.data.target_text;
      } catch (error) {
        console.error("Error during translation:", error);
      }
    },
    clearImage() {
      this.imageUrl = null;
      this.responseText="";
    },
    demoHandler() {
      // Translate button handler
      this.responseText="";
      const formData =new FormData;
      formData.append("image",file);
      formData.append("origin_language", this.originlanguage);
      formData.append("target_language", this.targetlanguage);
      axios
        .post("http://127.0.0.1:8000/api/translateimagetext",formData,{
          headers:{
            'Content-Type':'multipart/form-data'
          }
        })
        .then((response) => {
          console.log(response);
          this.responseText=response.data.target_text;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>
.container {
    display: flex;
}

.column {
    width: 50%;
    padding: 10px;
}

.left {
    order: 1;
}

.right {
    order: 2;
}

.box {
    border: 2px solid lightgreen;
    padding: 5px;
    height: 500px;
    background-color: white;
    border-radius: 20px;
}

.buttonright {
    justify-content: right;
    align-items: right;
}

.image-container {
  width: 800px;
  height: 500px;
  border: 2px solid lightgreen;
  background-size: cover;
  background-position: center;
  position: relative;
  background-color: white;
  padding: 5px;
  border-radius: 20px;
}

.image-container input[type="file"] {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  cursor: pointer;
}

.image-fit {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.image-container button {
  position: absolute;
  bottom: 10px;
  left: 50%;
  transform: translateX(-50%);
}
</style>

