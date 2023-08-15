<template>
    <div class="container">
        <div class="column left">
            <el-button type="primary" round>
                Upload<el-icon justify="el-icon--right"><Upload /></el-icon>

            </el-button>
            <el-button type="primary" round>
                Delete<el-icon justify="el-icon--right"><Delete /></el-icon>
            </el-button>
            <div class="box"></div>
        </div>
        <div class="column right">
            <el-dropdown class="buttonleft">
                <el-button type="primary" round>
                    Original Language<el-icon class="el-icon--right"><arrow-down /></el-icon>
                </el-button>
                <template #dropdown>
                    <el-dropdown-menu>
                        <el-dropdown-item>Chinese</el-dropdown-item>
                        <el-dropdown-item>English</el-dropdown-item>
                        <el-dropdown-item>Spanish</el-dropdown-item>
                        <el-dropdown-item>French</el-dropdown-item>
                        <el-dropdown-item>Russian</el-dropdown-item>
                        <el-dropdown-item>Arabic</el-dropdown-item>
                        <el-dropdown-item>German</el-dropdown-item>
                        <el-dropdown-item>Japanese</el-dropdown-item>
                        <el-dropdown-item>Korean</el-dropdown-item>
                    </el-dropdown-menu>
                </template>
            </el-dropdown>

            <el-button type="primary" round class="buttoncenter">Translate</el-button>

            <el-dropdown class="buttonright">
                <el-button type="primary" round>
                    Mother Language<el-icon class="el-icon--right"><arrow-down /></el-icon>
                </el-button>
                <template #dropdown>
                    <el-dropdown-menu>
                        <el-dropdown-item>Chinese</el-dropdown-item>
                        <el-dropdown-item>English</el-dropdown-item>
                        <el-dropdown-item>Spanish</el-dropdown-item>
                        <el-dropdown-item>French</el-dropdown-item>
                        <el-dropdown-item>Russian</el-dropdown-item>
                        <el-dropdown-item>Arabic</el-dropdown-item>
                        <el-dropdown-item>German</el-dropdown-item>
                        <el-dropdown-item>Japanese</el-dropdown-item>
                        <el-dropdown-item>Korean</el-dropdown-item>
                    </el-dropdown-menu>
                </template>
            </el-dropdown>
            <div class="box"></div>
        </div>
    </div>
</template>

<style>
.container{
    display:flex;
}
.column{
    width:50%;
    padding:10px;
}
.left{
    order:1;
}
.right{
    order:2;
}
.box {
    border: 2px solid lightgreen;
    padding: 10px;
    height:350px;
    background-color: white;
    border-radius: 20px;
}
.buttonleft{

}
.buttoncenter{

}
.buttonright{
    justify-content: right;
    align-items: right;
}
</style>