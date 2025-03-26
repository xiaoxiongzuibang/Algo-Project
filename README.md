# README
section1, 生产流程
1. 读取csv文件，生成名为“french_words"的set
2. 构建 Game 类，负责游戏的逻辑运行
   1. 依照概率生成一个4*4的字母矩阵
   2. 检查用户找到的单词 (word_list)是否在 french_words 中 
   3. 尝试遍历 board 并且找出所有可能的单词：found_word 
   4. 引入 prefix-trie,增加前缀剪枝树，提升计算效率 
4. 构建 UI 类
5. 将French——words转换为一个前缀树结构




