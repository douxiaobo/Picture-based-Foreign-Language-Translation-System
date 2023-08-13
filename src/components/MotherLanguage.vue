<template>
    <h3>Please choose monther language：</h3>
    <el-dropdown size="large" split-button type="primary">
        Mother Language
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
</template>

<style scoped>
.example-showcase .el-dropdown + .el-dropdown {
  margin-left: 15px;
}
</style>