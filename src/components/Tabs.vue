<template>
    <!-- <el-radio-group v-model="tabPosition" style="margin-bottom: 30px">
      <el-radio-button label="top">top</el-radio-button>
      <el-radio-button label="right">right</el-radio-button>
      <el-radio-button label="bottom">bottom</el-radio-button>
      <el-radio-button label="left">left</el-radio-button>
    </el-radio-group> -->
  
    <el-tabs :tab-position="tabPosition" style="height: 200px" class="demo-tabs">
        <el-tab-pane label="UploadFile"><UploadFile /></el-tab-pane>
        <el-tab-pane label="Origin Language"><OriginalLanguage/></el-tab-pane>
        <el-tab-pane label="Target Language"><MotherLanguage/></el-tab-pane>
    </el-tabs>
  </template>
  <script lang="ts" setup>
  import { ref } from 'vue'
import UploadFile from './UploadFile.vue';
import OriginalLanguage from './OriginalLanguage.vue';
import MotherLanguage from './MotherLanguage.vue';
  
  const tabPosition = ref('right')
  </script>
  <style>
  .demo-tabs > .el-tabs__content {
    padding: 32px;
    color: #6b778c;
    font-size: 32px;
    font-weight: 600;
  }
  
  .el-tabs--right .el-tabs__content,
  .el-tabs--left .el-tabs__content {
    height: 100%;
  }
  </style>