<script setup>
import Header from './components/Header.vue'
import UploadFile from './components/UploadFile.vue'
import Language from './components/Language.Vue'
</script>

<template>
    <div>
        <div>
            <Header />
        </div>
        <hr />
        <main>
            <h2>Upload File:</h2>
            <div>
                <UploadFile />
            </div>
            <hr />
            <div>
                <Language />
            </div>
        </main>
        <hr />
        <footer>
            2023 Engage Trainning Program for University Students With Disability
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


footer{
    background-color: burlywood;
    text-align: right;
}
</style>