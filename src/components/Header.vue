

<template>
    
    <div class="title">
        <h1 class="title">
            Picture-based Foreign Language Translation System
        </h1>
        <!-- <p class="author">
            Author: Xiaobo Dou & Yitu Ma<br>
            Xiaobo Dou's Mentor: Xing Fan<br>
            Yitu Ma's Mentor: Rachel Wang
        </p> -->       
        <!-- <el-descriptions class="el-descriptions-large">
            <el-descriptions-item label="Author:" class="el-descriptions-small">Xiaobo Dou & Yitu Ma</el-descriptions-item>    
        </el-descriptions>
        <el-descriptions>
            <el-descriptions-item label="Xiaobo Dou's Mentor:" class="el-descriptions-small">Xing Fan</el-descriptions-item>
        </el-descriptions> 
        <el-descriptions>
            <el-descriptions-item label="Yitu Ma's Mentor:" class="el-descriptions-small">Rachel Wang</el-descriptions-item>
        </el-descriptions> -->

        

        <!-- <div class="small-text">
            <el-row :gutter="20">
                <el-col :span="14"></el-col>
                <el-col :span="10" laber-align="right">Author:</el-col>
                <el-col :span="10" laber-align="left">Xiaobo Dou & Yitu Ma</el-col>
            </el-row>
            <el-row :gutter="20">
                <el-col :span="14"></el-col>
                <el-col :span="10">Xiaobo Dou's Mentor:</el-col>
                <el-col :span="10">Xing Fan</el-col>
            </el-row>
            <el-row :gutter="20">
                <el-col :span="14"></el-col>
                <el-col :span="10">Yitu Ma's Mentor:</el-col>
                <el-col :span="10">Rachel Wang</el-col>
            </el-row>
        </div> -->


        
        
    </div>
    <!-- <div class="small-font">
            <el-descriptions class="el-descriptions-large">
                <el-descriptions-item label="Author:" class="el-descriptions-small">Xiaobo Dou & Yitu Ma</el-descriptions-item>
            </el-descriptions>
            <el-descriptions>
                <el-descriptions-item label="Xiaobo Dou's Mentor:" class="el-descriptions-small">Xing Fan</el-descriptions-item>
            </el-descriptions>
            <el-descriptions>
                <el-descriptions-item label="Yitu Ma's Mentor:" class="el-descriptions-small">Rachel Wang</el-descriptions-item>
            </el-descriptions>
        </div> -->

        
    <!-- <div class="small-text">
            <el-row :gutter="5">
                <el-col :span="2" laber-align="right" >Author</el-col>
                <el-col :span="1">:</el-col>
                <el-col :span="2" laber-align="left">Xiaobo Dou & Yitu Ma</el-col>
            </el-row>
            <el-row :gutter="5">
                <el-col :span="2" text-align="right">Xiaobo Dou's Mentor</el-col>
                <el-col :span="1">:</el-col>
                <el-col :span="2" text-align="left">Xing Fan</el-col>
            </el-row>
            <el-row :gutter="5">
                <el-col :span="2" laber-align="right">Yitu Ma's Mentor</el-col>
                <el-col :span="1">:</el-col>
                <el-col :span="2" vertical-align="left">Rachel Wang</el-col>
            </el-row>
        </div> -->
        <div class="author">
  <el-row :gutter="6" class="small-text" justify="end">
    <el-col :xs="8" :sm="6" :md="4" :lg="3" :xl="2" class="align-right">Author:</el-col>
    <el-col :xs="8" :sm="6" :md="4" :lg="3" :xl="2">Xiaobo Dou & Yitu Ma</el-col>
  </el-row>
  <el-row :gutter="6" class="small-text" justify="end">
    <el-col :xs="8" :sm="6" :md="4" :lg="3" :xl="2" class="align-right">Xiaobo Dou's Mentor:</el-col>
    <el-col :xs="8" :sm="6" :md="4" :lg="3" :xl="2">Xing Fan</el-col>
  </el-row>
  <el-row :gutter="6" class="small-text" justify="end">
    <el-col :xs="8" :sm="6" :md="4" :lg="3" :xl="2" class="align-right">Yitu Ma's Mentor:</el-col>
    <el-col :xs="8" :sm="6" :md="4" :lg="3" :xl="2">Rachel Wang</el-col>
  </el-row>
</div>

</template>

<style>


  .example-showcase .el-dropdown + .el-dropdown {
  margin-left: 15px;
  }

.title {
    font-size: 40px;
    /* background-color: aqua; */
    height: 60%;
    line-height: 1;
    text-align: center;
    color: blue;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}

.author{
  /* background-color: aqua; */
    color: black;
    font-size: 13px;
    /* text-align: right; */
    font-weight: bolder;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
.eldescriptions-large{
    vertical-align: auto;
    font-size: 12px;
}

.el-descriptions-small{
    float:right;
}

.el-col {
  border-radius: 4px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.small-font {
    font-size: 0.8em;
    text-align: right;
    width:100%；
  }
  .small-text {
    font-size: 1.0em;
    width: "120";
  }
  .align-right:before {
    content: "";
    display: inline-block;
    width: 1em;
  }
  .align-right {
    text-align: right;
  }
  .align-left {
    text-align: left;
  }
</style>

