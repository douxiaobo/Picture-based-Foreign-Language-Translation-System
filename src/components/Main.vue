<template>
    <div class="container">
        <div class="column left">
            <el-button type="primary" round v-if="imageUrl" @click="clearImage">Clear Image</el-button>
                <div class="image-container" :style="{ backgroundImage: `url(${imageUrl})` }">
                    <input type="file" @change="onImageSelected" accept="image/*" round />
                </div>        
        </div>
        <div class="column right">

            <el-select v-model="originlanguage" class="m-2" placeholder="Select" size="large">
                <el-option v-for="item in originlanguageDict" :key="item" :label="item" :value="item" />
            </el-select>

            <el-button type="primary" @click="demoHandler" round class="buttoncenter">Translate</el-button>

            <el-select v-model="targetlanguage" class="m-2" placeholder="Select" size="large">
                <el-option v-for="item in targetlanguageDict" :key="item" :label="item" :value="item" />
            </el-select>

            <div class="box"></div>
        </div>
    </div>
</template>

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
</style>

<script>

import { ref } from 'vue';
import axios from 'axios';

export default {
  data() {
    return {
      imageUrl: null,
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

    const demoHandler = () => {
      const path = "http://127.0.0.1:8010/api/translateimagetext";

      axios
        .get(path)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    };    

    return {
      originlanguage,
      originlanguageDict,
      targetlanguage,
      targetlanguageDict,
      demoHandler,
      changeoriginlanguage,
      changetargetlanguage,
    };
  },
};
</script>