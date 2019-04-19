<template>
  <div>
    <el-row style="margin-top: -50px">
      <h1>SOA-HW2 技术趋势分析</h1>
    </el-row>
    <el-row>
      <el-button v-for="keyword in keyword_list" type="primary" @click="prepare(keyword)">{{keyword}}</el-button>
    </el-row>
    <el-row style="margin-top: -20px;">
      <el-col :span="4">
        <h2>关键词热榜</h2>
      </el-col>
    </el-row>
    <el-container style="height:800px">
      <el-aside>
          <p v-for="item in list" style="text-align: left; margin-bottom: -10px">{{item}}</p>
      </el-aside>
      <el-main style="margin-top: -40px">
        <el-row>
          <img :src="fig_src" alt="找不到图片" height="600px" width="1500px" style="margin-top: -50px; margin-left: -250px">
        </el-row>
        <el-row>
          <div id="main" style="width:1300px; height:600px"></div>
        </el-row>
      </el-main>
    </el-container>
  </div>
</template>


<script>

  export default {
    name: "main",
    data() {
      return {
        keyword_list: ['大数据', '人工智能', '计算机视觉', '自然语言处理', '数据挖掘', '区块链', '机器人'],
        list: '',
        cnt: 0,
        fig_src: null,
        data: null
      }
    },
    methods: {
      get_echart() {
        let url = '/api/getxy';
        this.$http.get(url).then(function (res) {
          this.data = res.body;
          console.log(this.data);
          let xian = [];
          for (let i = 0; i < this.data[0].length; i++) {
            xian.push([this.data[0][i], this.data[1][i]])
          }
          let echarts = require('echarts');
          let myChart = echarts.init(document.getElementById('main'));
          let myoption = {
            backgroundColor: new echarts.graphic.RadialGradient(0.3, 0.3, 0.8, [{
              offset: 0,
              color: '#f7f8fa'
            }, {
              offset: 1,
              color: '#cdd0d5'
            }]),
            title: {
              text: 'Hype Cycle'
            },
            xAxis: {
              type: 'value'
            },
            yAxis: {
              type: 'value'
            },
            series: [
            {
              name: '1990',
              data: this.data[2],
              type: 'scatter',
              symbolSize: 5,
              label: {
                emphasis: {
                  show: true,
                  formatter: function (param) {
                    return param.data[2];
                  },
                  position: 'top'
                }
              },
              itemStyle: {
                normal: {
                  shadowBlur: 10,
                  shadowColor: 'rgba(120, 36, 50, 0.5)',
                  shadowOffsetY: 5,
                  color: new echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
                    offset: 0,
                    color: 'rgb(251, 118, 123)'
                  }, {
                    offset: 1,
                    color: 'rgb(204, 46, 72)'
                  }])
                }
              }
            },
              {
              data: xian,
              type: 'line',
              smooth: true,
              showSymbol: false,
                color: 'rgb(50, 50, 200)'
            }]
          };
          myChart.setOption(myoption);
        }, function (res) {
          console.log("Failed to get pos.");
        });
      },
      prepare(keyword) {
        let url = '/api/getlist';
        let data = {
          'keyword': keyword,
        };
        this.$http.post(url, data, {emulateJSON: true}).then(function (res) {
          this.list = res.body;
          console.log('get list');
          this.cnt += 1;
          this.fig_src = '/api/getfig/' + this.cnt;
          console.log(this.fig_src);
          this.get_echart();
        }, function (res) {
          this.list = 'fail';
          this.get_echart();
        });
      },
    },
    created() {
    }
  }

</script>


<style scoped>

</style>
