# README
2025.2.18更新
> 1. 新增“选词闪烁”功能
> 2. 新增结果显示与准确率显示功能
> 3. 更新了Game.py获取判断结果的API
> 4. 更新了新词源
> 5. 修复了DataFrame无法索引问题
> 6. 修复了按钮不灵敏问题
>    
> 待解决：
> 1. 概率分布不合理，依照规则难以找到答案
> 2. 待新增Restart功能
> 3. 待新增规则约束

![output](https://github.com/user-attachments/assets/efb35051-56bb-4be1-807b-1c77ebe8e63a)
------

Important update: 数据库已更新
  moodle 上发了新的词典，我已经调整完 CreatSet 了，GUI 部分如有相关部分记得调整
  新版的词典：“b" 识别为 False ； 没有音符号

Important update: 数据库已更新

Important update: 数据库已更新




### GUI.py需要：
1. 为了可视化初始board，需要一个函数允许我获得初始随机生成的字母，例如`letter_matrix = function(...)`, letter_matrix可以是一个数字矩阵或字符串矩阵，格式为ndarray。

### Game.py需要：
1. 
### 第一阶段

1. 生成16个符合频率的字母 (done）
2. 生产面板 （done）————>调整尺寸（done）
4. 接受用户信息并且返回单词 （done）
5. 判断单词是否在字典中 （ {'cat','dog'} ; french_words 是set 格式）
6. 生成正确错误的反馈 （逻辑+UI）（done）
7. 添加UI细节（ 字母按钮，提交按钮，刷新按钮）

（2，3 UI 类；1，4逻辑类）

### 第二阶段

1. 对于french——words构建剪枝树（game）
2. 遍历棋盘，生成正确的单词（game）
3. 生成最大可能单词数（game）
4.  对比输入，找出遗漏 （UI）

### 第三阶段（附加功能）

1. 计时模式 （增加计时模块）
2. 评分系统（根据找到的单词的个数，时间，复杂程度来评分）————> 设计评分方式 （正确率）
3. 竞赛模式 （1. 正确率/2.时间
