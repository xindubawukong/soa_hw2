<template>
  <div>
    <el-row>
      <el-button type="primary" @click="prepare('大数据')">大数据</el-button>
      <el-button type="primary">人工智能</el-button>
      <el-button type="primary">计算机视觉</el-button>
      <el-button type="primary">自然语言处理</el-button>
    </el-row>
    <el-row>
      <el-col :span="4">
        <h2>关键词热榜</h2>
      </el-col>
    </el-row>
    <el-container style="height:600px">
      <el-aside>
          <p v-for="item in list" style="text-align: left; margin-bottom: -10px">{{item}}</p>
      </el-aside>
      <el-main>
        <img src="/api/getfig1" alt="找不到图片">
      </el-main>
    </el-container>
    <p>{{list}}</p>
  </div>
</template>


<script>

  export default {
    name: "main",
    data() {
      return {
        keyword: '大数据',
        list: ''
      }
    },
    methods: {
      prepare() {
        let url = '/api/getlist';
        let data = {
          'keyword': this.keyword,
        };
        this.$http.post(url, data, {emulateJSON: true}).then(function (res) {
          this.list = res.body;
          console.log('post done');
        }, function (res) {
          this.list = 'fail';
        });
      },
    },
    created() {
      this.prepare();
    }
  }

</script>


<style scoped>

</style>
