<h1 align="center">DynFirework</h1>

<p align="center">
  <b>更真实自然的烟花！</b>
</p>
<p align="center">
    <img src="https://img.shields.io/badge/Minecraft-1.12.2 1.16.5-green?style=for-the-badge" />
    <a href="LICENSE">
        <img src="https://img.shields.io/badge/License-GPL--3.0-important?style=for-the-badge" />
    </a>
    <a href="https://qm.qq.com/q/m6XfOuCtVe">
    <img src="https://img.shields.io/badge/QQ-技术交流/反馈群-blue?style=for-the-badge" />
    </a>
    <a href="https://space.bilibili.com/288309681">
    <img src="https://img.shields.io/badge/bilibili-TianKong_y-pink?style=for-the-badge" />
    </a>
</p>

## > 简介
*DynFirework*是使用Python编写的*Minecraft*粒子烟花生成器**代码模板**，提供了若干模板函数以便生成一定样式的烟花数据包文件(.mcfunction)。
**[介绍视频](https://www.bilibili.com/video/BV1xYxxeqEMf/)**
## > 前置Mod及版本兼容性
*DynFirework*的输出指令基于[Colorblock](https://www.bilibili.com/read/cv32079719/)的rgbatickparameter和normal子指令，以实现渐变颜色粒子。
由于*Colorblock*仅支持1.12.2和1.16.5版本，当前版本的*DynFirework v1.0*生成的指令也只在上述2个版本有效。
理论上可以通过修改输出指令部分的代码并移除渐变色功能，使用原版particle指令以兼容全部版本，这是之后的更新内容之一。
## > 使用方法
*DynFirework v1.0*目前不具有图形化界面，只是提供了4种烟花函数模板和5种烟花发射轨迹函数模板。
使用方法为，下载源代码后，复制main.py副本或直接编写main函数，调用上述模板以生成烟花粒子。
生成器会在代码目录下创建一个functions子文件夹，一个tick对应该文件夹下的一个.mcfuntion文件。
如果你不了解.mcfuntion，可以参考[BV1aP41167ef](https://www.bilibili.com/video/BV1aP41167ef)
## > 函数模板介绍
**一、烟花模板**
1. basic_single_layer_firework
**单层烟花**
参数包括：

|参数名|含义|数据类型|
|---|---|---|
|tick|烟花爆炸时的游戏刻|int|
|x、y、z|烟花爆炸的坐标|float|
|start_color、end_color|烟花粒子渐变色的rgb|(int, int, int)|
|speed|烟花爆炸初速度|float|
|horizontal_angle_step、vertical_angle_step|烟花轨迹方向水平、竖直方向枚举角度间隔（单位为°）|int|
|duration|烟花轨迹前进时间（单位为秒）|float|
|lifetime|烟花粒子存在时间（单位为秒）|float|
2. basic_double_layer_firework
**双层烟花**
参数包括：

|参数名|含义|数据类型|
|---|---|---|
|tick|烟花爆炸时的游戏刻|int|
|x、y、z|烟花爆炸的坐标|float|
|inner_start_color、inner_end_color|内层烟花粒子渐变色的rgb|(int, int, int)|
|outer_start_color、outer_end_color|外层烟花粒子渐变色的rgb|(int, int, int)|
|inner_speed、outer_speed|内、外层烟花爆炸初速度|float|
|outer_horizontal_angle_step, outer_vertical_angle_step|外层烟花轨迹方向水平、竖直方向枚举角度间隔（单位为°）（没有内层参数，会根据速度比例关系自动计算）|int|
|duration|烟花轨迹前进时间（单位为秒）|float|
|lifetime|烟花粒子存在时间（单位为秒）|float|
3. directional_firework
**聚向烟花**
参数包括：

|参数名|含义|数据类型|
|---|---|---|
|tick|烟花爆炸时的游戏刻|int|
|x、y、z|烟花爆炸的坐标|float|
|start_color、end_color|烟花粒子渐变色的rgb|(int, int, int)|
|speed|烟花爆炸初速度|float|
|direction_horizontal_angle, direction_vertical_angle|烟花爆炸方向水平、垂直角（类似经纬度）（单位为°）|int|
|spread_angle|轨迹方向偏移范围（单位为°）|int|
|track_count|轨迹数量|int|
|duration|烟花轨迹前进时间（单位为秒）|float|
|lifetime|烟花粒子存在时间（单位为秒）|float|
4. clustered_firework
**集束烟花**
参数包括：

|参数名|含义|数据类型|
|---|---|---|
|tick|烟花爆炸时的游戏刻|int|
|x、y、z|烟花爆炸的坐标|float|
|start_color、end_color|烟花粒子渐变色的rgb|(int, int, int)|
|speed|烟花爆炸初速度|float|
|horizontal_angle_step、vertical_angle_step|烟花轨迹方向水平、竖直方向枚举角度间隔（单位为°）|int|
|spread_angle|轨迹方向偏移范围（单位为°）|int|
|track_count|轨迹数量|int|
|duration|烟花轨迹前进时间（单位为秒）|float|
|lifetime|烟花粒子存在时间（单位为秒）|float|

**二、发射轨迹模板**
1. launch_trajectory
**基础曲线发射轨迹**
参数包括：

|参数名|含义|数据类型|
|---|---|---|
|end_tick|轨迹结束时的游戏刻|int|
|x0、y0、z0|轨迹起始坐标|float|
|x1、y1、z1|轨迹终止坐标|float|
|start_color、end_color|轨迹粒子渐变色的rgb|(int, int, int)|
|duration|烟花轨迹前进时间（单位为秒）|float|
|k、m0|模拟抛体的空气阻力系数、质量（k与m0的比例决定轨迹形状）|float|
|rho|粒子密度，即单位tick生成的粒子数|int|
|lifetime|轨迹粒子存在时间（单位为秒）|float|

2. launch_spark_trajectory
**火花发射轨迹**
参数包括：

|参数名|含义|数据类型|
|---|---|---|
|end_tick|轨迹结束时的游戏刻|int|
|x0、y0、z0|轨迹起始坐标|float|
|x1、y1、z1|轨迹终止坐标|float|
|duration|烟花轨迹前进时间（单位为秒）|float|
|k、m0|模拟抛体的空气阻力系数、质量（k与m0的比例决定轨迹形状）|float|
|lifetime|轨迹粒子存在时间（单位为秒）|float|
|particle_count|每个tick生成的火花数量|int|

3. trajectory_with_random_offset
**随机扰动发射轨迹**
参数包括：

|参数名|含义|数据类型|
|---|---|---|
|end_tick|轨迹结束时的游戏刻|int|
|x0、y0、z0|轨迹起始坐标|float|
|x1、y1、z1|轨迹终止坐标|float|
|duration|烟花轨迹前进时间（单位为秒）|float|
|k、m0|模拟抛体的空气阻力系数、质量（k与m0的比例决定轨迹形状）|float|
|lifetime|轨迹粒子存在时间（单位为秒）|float|
|interval_ticks|扰动频率，即每多少tick生成一个随机偏移点|int|
|points_per_tick|每个tick生成的粒子数量|int|

4. thick_trajectory_with_random_offset
**随机扰动发射轨迹（粗）**
在随机扰动发射轨迹的基础上，原先一个粒子的位置在一定范围内生成多个粒子
参数包括：

|参数名|含义|数据类型|
|---|---|---|
|end_tick|轨迹结束时的游戏刻|int|
|x0、y0、z0|轨迹起始坐标|float|
|x1、y1、z1|轨迹终止坐标|float|
|duration|烟花轨迹前进时间（单位为秒）|float|
|k、m0|模拟抛体的空气阻力系数、质量（k与m0的比例决定轨迹形状）|float|
|lifetime|轨迹粒子存在时间（单位为秒）|float|
|interval_ticks|扰动频率，即每多少tick生成一个随机偏移点|int|
|points_per_tick|每个tick生成的粒子数量|int|
|range_x、range_y、range_z|每组粒子生成的范围|float|
|particle_count|每组粒子的数量|int|

5. expanding_trajectory_with_random_offset
**扩散随机扰动发射轨迹**
在随机扰动发射轨迹（粗）的基础上，轨迹粒子向外扩散
参数包括：

|参数名|含义|数据类型|
|---|---|---|
|end_tick|轨迹结束时的游戏刻|int|
|x0、y0、z0|轨迹起始坐标|float|
|x1、y1、z1|轨迹终止坐标|float|
|duration|烟花轨迹前进时间（单位为秒）|float|
|k、m0|模拟抛体的空气阻力系数、质量（k与m0的比例决定轨迹形状）|float|
|lifetime|轨迹粒子存在时间（单位为秒）|float|
|interval_ticks|扰动频率，即每多少tick生成一个随机偏移点|int|
|points_per_tick|每个tick生成的粒子数量|int|
|range_x、range_y、range_z|每组粒子生成的范围|float|
|particle_count|每组粒子的数量|int|
|speed_factor|扩散速率|float|

## > 效果展示
<div align=center>  <img src="https://s2.loli.net/2024/09/30/15STOnguXb2vINA.png" height="300" width="300">  </div>
<p align="center"><b>双层烟花</b></p>
<div align=center>  <img src="https://s2.loli.net/2024/09/30/jOSAcTvmf4d7PCg.png" height="300" width="300">  </div>
<p align="center"><b>双层渐变烟花</b></p>
<div align=center>  <img src="https://s2.loli.net/2024/09/30/JuYBx7DfncHASQj.png" height="300" width="300">  </div>  
<p align="center"><b>单层渐变烟花</b></p>

## > 作者&技术交流/反馈群
- bilibili：[TianKong_y](https://space.bilibili.com/288309681)
- QQ：[技术交流/反馈群](https://qm.qq.com/q/m6XfOuCtVe)
