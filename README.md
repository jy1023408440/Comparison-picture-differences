# Comparison-picture-differences

比较两个图片的差异：


环境：
Pycharm
python3.5.1
opencv3.4.1+contrib


步骤：
1.读取图片
2.Sobel算子处理图片
3.图片相减
4.中值滤波
5.形态学腐蚀
6.低通滤波
7.形态学膨胀
8.寻找轮廓
9.根据面积筛选轮廓
10.画轮廓并展示
