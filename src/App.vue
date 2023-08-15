<script setup>
import Header from './components/Header.vue'
import UploadFile from './components/UploadFile.vue'
import Language from './components/Language.Vue'
import MotherLanguage from './components/MotherLanguage.vue'
import Tabs from './components/Tabs.vue'
import Main from './components/Main.vue'
</script>

<template>
    <div>
        <div class="header">
            <Header />
        </div>
        <hr />
        <main class="common-layout">
            <Main />
            <!-- <h2>Upload File:</h2>
            <div>
                <UploadFile />
            </div> -->
            <!-- <div>
                <Tabs />
            </div> -->
            <!-- <div class="container">
                
                <div class="left-column">
                    
                    <UploadFile />
                </div>
                
                <div class="right-column">
                    
                    <MotherLanguage />
                </div>
            </div> -->
            <!-- <hr />
            <div>
                <Language />
            </div> -->
        </main>
        <hr />
        <footer>
            @2023 Engage Trainning Program for University Students With Disability
        </footer>
    </div>
</template>

<style scoped>

.common-layout{
    background-color: #f4f4f5;;
    /* background-image: url(./assets/2.jpg); */
    background-size: cover;
    background-position: center;
}


header {
    background-color: white;
}


.container {
    display: flex;
    /* background-color: yellowgreen;  */ 
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
    /* background-color: burlywood; */
    text-align: right;
}
</style>