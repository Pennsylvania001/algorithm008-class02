#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def maxArea(self, height):
        maxNum = 0
        for i in range(0, len(height) - 1):
            for j in range(i + 1, len(height)):
                area = (j - i) * min(height[i], height[j])
                maxNum = max(maxNum, area)
        return maxNum
