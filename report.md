# SOA-HW2 技术趋势分析



计65 丁相允 2016011361



## 实验概述

构建一个简单的网站，让用户能获取一些指定领域的关键词和它们每年的热度数据，将关键词按照总体的热度(每年的数值之和)从高到低排序，可视化展示总体热度前 10 个关键词的年份-热度图，并标出前 20 个关键词映射到技术成熟度曲线的位置。



## 实验内容

人工智能和大数据的截图位于`example`目录下。

### 后端

后端采用django框架编写，代码位于`server`目录下。后端直接使用了提供的`api_query.py`和 `hype_cycle.py`， 并进行了一定的修改。

`views.py`中定义了的响应函数如下：`getlist`返回热点关键词列表（直接调用`api_query`）；`getfig`返回折线图，使用matplotlib库作图后返回前端；`getxy`返回技术成熟度曲线及前20个关键词的位置。

因为提供的图片锯齿比较严重，故我在`pre-process.py`中使用了`opencv`库中的中值滤波器进行了平滑处理，处理后的图片相对比较平滑，得到的坐标更为准确。

![image-20190419205217750](/Users/xdbwk/Library/Application Support/typora-user-images/image-20190419205217750.png)

### 前端

前端采用vue框架编写，在`frontend`目录下，主要编写的部分位于`/frontend/src/components/main.vue`。为了方便我使用了webpack快速搭建vue框架。前端页面概览如下：

![image-20190419205610865](/Users/xdbwk/Library/Application Support/typora-user-images/image-20190419205610865.png)

顶部的按钮栏可以选择想要查看的技术类别，包括'大数据', '人工智能', '计算机视觉', '自然语言处理', '数据挖掘', '区块链', '机器人'等。左侧给出了搜索到的关键词热榜，右侧上部是前十个词的热点折线图，右侧下部是前二十个词在技术成熟度曲线上的位置。

前端使用了element-ui库辅助编写界面。使用vue-resource的ajax功能与后端进行数据传输。

我的热点折线图是后端生成将图片传递给前端的，但技术成熟度曲线则是后端给前端数据，前端作图。后端传输的数据包括：曲线上的1000个点的坐标（基于`api_query.py`）、前二十个热点词及其在成熟度曲线上的位置（基于

`hype_cycle.py`）。然后使用echarts库进行前端绘图。此处没有后端作图的原因是，有些点在曲线上的位置太密集，故我想采用鼠标移到点上再显示其对应的热点词的方式。效果如下：

![image-20190419211422653](/Users/xdbwk/Library/Application Support/typora-user-images/image-20190419211422653.png)

每个点都对应一个热点词，鼠标移到上面即可显示位置。

### 前后端交互

实验中用到的api如下（django中的`urls.py`）：

```python
    url(r'^api/getlist', views.getlist),
    url(r'^api/getfig*', views.getfig),
    url(r'^api/getxy', views.getxy),
```

其中getlist是post方法，另外两个都是get方法。



## 实验小结

本次试验让我体会到了“全栈工程师”是多么难的一件事情。还需要多多学习。