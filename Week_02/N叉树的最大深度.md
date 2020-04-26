 N叉树的最大深度

给定一个 N 叉树，找到其最大深度。

最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

例如，给定一个 3叉树 :我们应返回其最大深度，3。

说明:

树的深度不会超过 1000。

树的节点总不会超过 5000。

```python
"""
复杂度分析
时间复杂度：每个节点遍历一次，所以时间复杂度是 O(N)O(N)，其中 NN 为节点数。
空间复杂度：最坏情况下, 树完全非平衡，
例如 每个节点有且仅有一个孩子节点，递归调用会发生 NN 次（等于树的深度），所以存储调用栈需要 O(N)O(N)。
但是在最好情况下（树完全平衡），树的高度为 \log(N)log(N)。
所以在此情况下空间复杂度为 O(\log(N))O(log(N))。
"""
class Solution(object):
    def maxDepth(self, root):
        if root is None: 
            return 0 
        elif root.children == []:
            return 1
        else: 
            height = [self.maxDepth(c) for c in root.children]
            return max(height) + 1
```

