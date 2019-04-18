<template>
  <div>
    <el-row>
      <el-button type="primary" @click="prepare('大数据')">大数据</el-button>
      <el-button type="primary">人工智能</el-button>
      <el-button type="primary">计算机视觉</el-button>
      <el-button type="primary">自然语言处理</el-button>
      <p>{{keyword}}</p>
    </el-row>
  </div>
</template>


<script>

  export default {
    name: "main",
    data() {
      return {
        keyword: 'asdasdasd',
      }
    },
    methods: {
      prepare() {
        let url = '/api/getlist';
        let data = {
          'keyword': this.keyword
        };
        this.$http.post(url, JSON.stringify(data), {emulateJSON:true}).then(function(res){
          this.keyword = 'success';
        },function(res){
          this.keyword = 'fail';
        });
      }
    }
  }

</script>


<style scoped>

</style>
