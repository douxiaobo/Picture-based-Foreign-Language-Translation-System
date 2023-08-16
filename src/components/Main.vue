<template>
    <div class="container">
        <div class="column left">
            <UploadPicture />
            <!-- <el-button type="primary" round>
                Upload<el-icon justify="el-icon--right"><Upload /></el-icon>

            </el-button>
            <el-button type="primary" round>
                Delete<el-icon justify="el-icon--right"><Delete /></el-icon>
            </el-button>
            <div class="box">
                           
                     

                
            </div> -->
        </div>
        <div class="column right">
            <!-- <el-dropdown class="buttonleft">
                <el-button type="primary" round>
                    Original Language<el-icon class="el-icon--right"><arrow-down /></el-icon>
                </el-button>
                <template #dropdown>
                    <el-dropdown-menu>
                        <el-dropdown-item v-for="language in languages">{{ language }}</el-dropdown-item> -->
                        <!-- <el-dropdown-item>Chinese</el-dropdown-item>
                        <el-dropdown-item>English</el-dropdown-item>
                        <el-dropdown-item>Spanish</el-dropdown-item>
                        <el-dropdown-item>French</el-dropdown-item>
                        <el-dropdown-item>Russian</el-dropdown-item>
                        <el-dropdown-item>Arabic</el-dropdown-item>
                        <el-dropdown-item>German</el-dropdown-item>
                        <el-dropdown-item>Japanese</el-dropdown-item>
                        <el-dropdown-item>Korean</el-dropdown-item> -->
                    <!-- </el-dropdown-menu>
                </template>
            </el-dropdown> -->

            <el-select v-model="originLanguage" class="m-2" placeholder="Select" size="large">
                <el-option v-for="item in originLanguageDict" :key="item" :label="item" :value="item" />
            </el-select>

            <el-button type="primary" @click="demoHandler" round class="buttoncenter">Translate</el-button>

            <el-dropdown class="buttonright">
                <el-button type="primary" round>
                    Mother Language<el-icon class="el-icon--right"><arrow-down /></el-icon>
                </el-button>
                <template #dropdown>
                    <el-dropdown-menu>
                        <el-dropdown-item v-for="language in languages">{{ language }}</el-dropdown-item>
                        <!-- <el-dropdown-item>Chinese</el-dropdown-item>
                        <el-dropdown-item>English</el-dropdown-item>
                        <el-dropdown-item>Spanish</el-dropdown-item>
                        <el-dropdown-item>French</el-dropdown-item>
                        <el-dropdown-item>Russian</el-dropdown-item>
                        <el-dropdown-item>Arabic</el-dropdown-item>
                        <el-dropdown-item>German</el-dropdown-item>
                        <el-dropdown-item>Japanese</el-dropdown-item>
                        <el-dropdown-item>Korean</el-dropdown-item> -->
                    </el-dropdown-menu>
                </template>
            </el-dropdown>
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

.buttonleft {}

.buttoncenter {}

.buttonright {
    justify-content: right;
    align-items: right;
}
</style>

<script lang="ts" setup>
import { VueElement, ref } from 'vue'
import { Delete, Download, Plus, ZoomIn } from '@element-plus/icons-vue'

import type { UploadFile } from 'element-plus'

import UploadPicture from './UploadPicture.vue'
import axios from 'axios'
import OriginalLanguage from './OriginalLanguage.vue'

const originLanguage = ref('English')
const originLanguageDict = ['Chinese', 'English', 'Spanish', 'French', 'Russian', 'Arabic', 'German', 'Japanese', 'Korean']
const demoHandler = () => {
    const path = 'http://127.0.0.1:8010/api/translateimagetext'
      axios.get(path)
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.log(error)
        })
}

const dialogImageUrl = ref('')
const dialogVisible = ref(false)
const disabled = ref(false)

const handleRemove = (file: UploadFile) => {
    console.log(file)
}

const handlePictureCardPreview = (file: UploadFile) => {
    dialogImageUrl.value = file.url!
    dialogVisible.value = true
}

const handleDownload = (file: UploadFile) => {
    console.log(file)
}



const languages = ref(['Chinese', 'English', 'Spanish', 'French', 'Russian', 'Arabic', 'German', 'Japanese', 'Korean'])


</script>


<script>

</script>