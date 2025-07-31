#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的二分法算法示例
"""

def binary_search_with_steps(arr, target):
    """
    带详细步骤的二分查找算法
    """
    left, right = 0, len(arr) - 1
    step = 1
    
    print(f"在数组 {arr} 中查找 {target}")
    print(f"初始范围: left={left}, right={right}")
    print("-" * 40)
    
    while left <= right:
        mid = left + (right - left) // 2
        print(f"第 {step} 步:")
        print(f"  left={left}, right={right}, mid={mid}")
        print(f"  arr[{mid}] = {arr[mid]}")
        
        if arr[mid] == target:
            print(f"  找到目标值！位置: {mid}")
            return mid
        elif arr[mid] < target:
            print(f"  {arr[mid]} < {target}, 在右半部分查找")
            left = mid + 1
        else:
            print(f"  {arr[mid]} > {target}, 在左半部分查找")
            right = mid - 1
        
        print(f"  新范围: left={left}, right={right}")
        print()
        step += 1
    
    print("未找到目标值")
    return -1


def simple_binary_search(arr, target):
    """
    简单的二分查找实现
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


if __name__ == "__main__":
    # 测试数组
    test_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    print("二分法算法演示")
    print("=" * 50)
    
    # 演示查找存在的元素
    print("查找存在的元素:")
    binary_search_with_steps(test_array, 13)
    
    print("\n" + "=" * 50)
    
    # 演示查找不存在的元素
    print("查找不存在的元素:")
    binary_search_with_steps(test_array, 6)
    
    print("\n" + "=" * 50)
    
    # 简单测试
    print("简单测试:")
    targets = [1, 7, 15, 20, 0]
    for target in targets:
        result = simple_binary_search(test_array, target)
        if result != -1:
            print(f"找到 {target} 在位置 {result}")
        else:
            print(f"未找到 {target}")