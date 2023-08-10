<script setup>
import Header from './components/Header.vue'
import UploadFile from './components/UploadFile.vue'
import Language from './components/Language.Vue'
import ChooseLanguage from './components/ChooseLanguage.vue'
</script>

<template>
    <div class="common-layout">
        <div>
            <Header />
        </div>
        <hr />
        <main>
            <!-- <h2>Upload File:</h2>
            <div>
                <UploadFile />
            </div> -->
            
            <div class="container">
                
                <div class="left-column">
                    <h2>UpLoad File:</h2>
                    <UploadFile />
                </div>
                
                <div class="right-column">
                    <h2>Choose your monther language：</h2>
                    <ChooseLanguage />
                </div>
            </div>
            <hr />
            <div>
                <Language />
            </div>
        </main>
        <hr />
        <footer>
            @2023 Engage Trainning Program for University Students With Disability
        </footer>
    </div>
</template>

<style scoped>

/*
header {
    background-color:aqua;
    height:60px;
    padding:20px;
    text-align: center;
    font-size: 20px;
}*/


.container {
    display: flex;
    background-color: yellowgreen;  
    /* justify-content: space-between;  */ 
    flex-direction: row;
  }
  .left-column{
    flex:1;
  }

  .right-column{
    flex:1;
    border-left:1px solid #ccc;
    padding-left:20px;
  }

  /* .left {
    order: 1;
    width: 50%;
  }
  
  .right {
    order: 2;
    width: 50%;
  } */

footer{
    background-color: burlywood;
    text-align: right;
}
</style>