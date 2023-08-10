<template>
    <div class="container">
      <div class="column left">
        <h2 class="originallanguage">Original Language</h2>
        <div class="box">
          <!-- 在这里添加原始语言的文本 -->
        </div>
      </div>
      <div class="column right">
        <h2 class="originallanguage">Mother Language</h2>
        <!-- <div><ChooseLanguage /></div> -->
        <div class="box">
          <!-- 在这里添加母语的文本 -->
        </div>
      </div>
    </div>
  </template>

  <script setup>import ChooseLanguage from './ChooseLanguage.vue'</script>
  
  <style>
  .container {
    display: flex;
    background-color: yellowgreen;    
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
  
  h2 {
    text-align: center;
  }
  
  .box {
    border: 1px solid black;
    padding: 10px;
    height:350px;
  }

  .originallanguage{
    color: blue;
  }
  </style>