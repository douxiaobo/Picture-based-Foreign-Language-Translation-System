<template>
    <div>
        <el-button type="primary" round v-if="imageUrl" @click="clearImage">Clear Image</el-button>
        <div class="image-container" :style="{ backgroundImage: `url(${imageUrl})` }">
            <input type="file" @change="onImageSelected" accept="image/*" round />
        </div>        
    </div>
</template>

<script>
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
};
</script>

<style>
.image-container {
  width: 500px;
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