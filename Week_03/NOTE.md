# 学习笔记

## 递归
- 一般一段复杂的程序都能找到重复的地方
- 使用递归很多时候能够让代码很简洁
- 递归是计算机擅长的，人不擅长于递归，所以熟悉后不要手动递归
- 递归按照模板来，不迷路

**python**
```python
def recursion(level, param1, param2, ...): 
    # 终止条件
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # 处理本层
    process(level, data...) 
    # 递归 
    self.recursion(level + 1, p1, ...) 
    # 如果有需要，清理本层状态
```


### 树的遍历
- 深度优先：前、中、后序遍历，其实就是根节点处理跟子节点的前后关系
- 广度优先

代码模板：
```python
def traverse(TreeNode root):
    print('前序遍历的' + root.val)
    traverse(root.left)
    print('中序遍历的' + root.val)
    traverse(root.right)
    print('后序遍历的' + root.val)
```

## 分治
- 分治是一种思想，通常是把一个大问题分解成为很多个小问题去解决，然后合并结果
- 它本身是运用到了递归的，所以它的代码模板跟递归有点像

```python
def divide_conquer(problem, param1, param2, ...): 
  # 终止条件 
  if problem is None: 
	print_result 
	return 

  # 准备数据，分片
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 

  # 处理子问题，得到结果
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …

  # 合并结果 
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # 清理本层状态
```



### 全排列问题

给三个数 [1,2,3]，你肯定不会无规律地乱穷举，一般是这样：

- 先固定第一位为 1，然后第二位可以是 2，那么第三位只能是 3；
- 然后可以把第二位变成 3，第三位就只能是 2 了；
- 然后就只能变化第一位，变成 2，然后再穷举后两位……

其实这就是回溯算法，下面这棵树就是**决策树**：

<img src="https://pic.leetcode-cn.com/717e30489d3d78f79c9b2d75ed5da913d853cd344fe3335e39fcfc319a231cf2-file_1575263105327" width="400px">

上面说的「**路径**」和「**选择列表**」作为决策树上每个节点的属性，比如下图列出了几个节点的属性：

<img src="https://pic.leetcode-cn.com/c7d8716a279071f9eaa806dc4ede58f280b17fd643e968a921056d0de3dc65c0-file_1575263105332" width="400px">

我们定义的 `backtrack` 函数其实就像一个指针，在这棵树上游走，同时要正确维护每个节点的属性，每当走到树的底层，其「**路径**」就是一个全排列。

<img src="https://pic.leetcode-cn.com/be9396dfb1e87d8f0db66d582d12f9f5ed569b630338bfe0377de938ffa0dc2c-file_1575263105330" width="400px">

现在理解回溯的核心算法就比较简单了：
``` python
for 选择 in 选择列表:
    # 做选择
    路径.add(选择)
    backtrack(路径, 选择列表)
    # 撤销选择
    路径.remove(选择)
```

路径的添加，往往伴随着剪枝

<img src="https://pic.leetcode-cn.com/d3feae35b7d1d6c9e5a48230d200c2b27106b53abb57fbd244a1fd549416b400-file_1575263105333" width="400px">



## 心得

刻意练习到成为专业人员
