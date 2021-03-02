# TwitterSentiment  
/Web:django框架，实现前后端交互,导入百度echarts实现数据动态可视化  
/GetOldTweets3:Python实现爬取Twitter实时数据，注意要将Proxy键值对改为自己的代理，同时及时更新cookie，不然会出错。  
./ 本目录下为Bert实现中文情感分析  
针对不同搜索结果的热度可视化：（如corinavirus）Echart实现动态可视化     
![image](https://user-images.githubusercontent.com/78432083/109454728-d2c57500-7a8f-11eb-83a0-6bb552d70567.png)  
    算法描述：①使用Python对Twitter网站进行相关关键词数据爬取并汇总。  
           ②对爬取得到的数据进行清洗去重去停用词等预处理。  
                                 ③建立embedding层，将单词转换为词向量表示，并进行特征提取。  
                                 ④建立LSTM模型并使用预先标注好的数据集对模型参数进行梯度下降更新。  
                                 ⑤使用Python django Web框架实现前后端交互。  
                                 ⑥得出该时间对于关键词事件的舆情分析以及预测，并使用Echart进行可视化。  
