<template>  
    <div class="container">
        <div class="column left"> 
          <div class="image-container" :style="{ backgroundImage: `url(${imageUrl})` }">
            <input type="file" @change="onImageSelected" accept="image/*" round />
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
      responseText:"",
    };
  },
  methods: {
    onImageSelected(event) {
      const file = event.target.files[0];
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = () => {
        this.imageUrl = reader.result;
      };
    },
    clearImage() {
      this.imageUrl = null;
    },
    demoHandler(){
      const path = "http://127.0.0.1:8000/api/translateimagetext";
      const formData=new FormData();
      formData.append('image',this.imageUrl);
      formData.append('target_language',this.targetlanguage);
      formData.append('origin_language',this.originlanguage);

      axios
        .post(path,formData,{
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
  setup() {
    const originlanguage = ref("English");
    const originlanguageDict = [
      "Chinese",
      "English",
      "Spanish",
      "French",
      "Russian",
      "Arabic",
      "German",
      "Japanese",
      "Korean",
    ];

    const changeoriginlanguage = (value) => {
      originlanguage.value = value;
    };

    const targetlanguage=ref("Chinese");
    const targetlanguageDict = [
      "Chinese",
      "English",
      "Spanish",
      "French",
      "Russian",
      "Arabic",
      "German",
      "Japanese",
      "Korean",
    ];

    const changetargetlanguage =(value)=>{
        targetlanguage.value=value;
    }   
    

    return {
      originlanguage,
      originlanguageDict,
      targetlanguage,
      targetlanguageDict,
      changeoriginlanguage,
      changetargetlanguage,
    };
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
    padding: 10px;
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

.image-container button {
  position: absolute;
  bottom: 10px;
  left: 50%;
  transform: translateX(-50%);
}

.el-row {
  margin-bottom: 20px;
}
.el-row:last-child {
  margin-bottom: 0;
}
.el-col {
  border-radius: 4px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
</style>

