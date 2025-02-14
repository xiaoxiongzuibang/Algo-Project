# README
<img width="996" alt="截屏2025-02-14 14 59 46" src="https://github.com/user-attachments/assets/e5ec02ab-e5c5-4335-9879-15dea71b6b9f" />

Important update: 更新数据库


### GUI.py需要：
1. 为了可视化初始board，需要一个函数允许我获得初始随机生成的字母，例如`letter_matrix = function(...)`, letter_matrix可以是一个数字矩阵或字符串矩阵，格式为ndarray。

### Game.py需要：
1. 
### 第一阶段

1. 生成16个符合频率的字母 (done）
2. 生产面板 （done）————>调整尺寸
4. 接受用户信息并且返回单词 
5. 判断单词是否在字典中 （ {'cat','dog'} ; french_words 是set 格式）
6. 生成正确错误的反馈 （逻辑+UI）
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
