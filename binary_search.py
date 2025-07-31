#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
二分法算法示例 (Binary Search Algorithm Examples)

本文件包含了多种二分法算法的实现和应用示例：
1. 基础二分查找
2. 递归版本二分查找
3. 查找插入位置
4. 查找范围边界
5. 浮点数二分法
"""

def binary_search_iterative(arr, target):
    """
    迭代版本的二分查找算法
    
    Args:
        arr: 已排序的数组
        target: 目标值
    
    Returns:
        目标值的索引，如果不存在返回-1
    
    时间复杂度: O(log n)
    空间复杂度: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # 防止整数溢出
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(arr, target, left=None, right=None):
    """
    递归版本的二分查找算法
    
    Args:
        arr: 已排序的数组
        target: 目标值
        left: 左边界
        right: 右边界
    
    Returns:
        目标值的索引，如果不存在返回-1
    
    时间复杂度: O(log n)
    空间复杂度: O(log n) - 递归调用栈
    """
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def binary_search_insert_position(arr, target):
    """
    查找目标值的插入位置（如果目标值不存在）
    
    Args:
        arr: 已排序的数组
        target: 目标值
    
    Returns:
        目标值应该插入的位置索引
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left


def binary_search_first_occurrence(arr, target):
    """
    查找目标值的第一次出现位置
    
    Args:
        arr: 已排序的数组（可能包含重复元素）
        target: 目标值
    
    Returns:
        目标值第一次出现的索引，如果不存在返回-1
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # 继续在左半部分查找
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def binary_search_last_occurrence(arr, target):
    """
    查找目标值的最后一次出现位置
    
    Args:
        arr: 已排序的数组（可能包含重复元素）
        target: 目标值
    
    Returns:
        目标值最后一次出现的索引，如果不存在返回-1
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # 继续在右半部分查找
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def binary_search_range(arr, target):
    """
    查找目标值的出现范围
    
    Args:
        arr: 已排序的数组（可能包含重复元素）
        target: 目标值
    
    Returns:
        [first_index, last_index] 或 [-1, -1] 如果不存在
    """
    first = binary_search_first_occurrence(arr, target)
    if first == -1:
        return [-1, -1]
    
    last = binary_search_last_occurrence(arr, target)
    return [first, last]


def binary_search_float(func, target, left, right, epsilon=1e-9, max_iterations=100):
    """
    浮点数二分法求解方程
    
    Args:
        func: 单调函数
        target: 目标值
        left: 左边界
        right: 右边界
        epsilon: 精度
        max_iterations: 最大迭代次数
    
    Returns:
        使得 func(x) ≈ target 的 x 值
    """
    for _ in range(max_iterations):
        if right - left < epsilon:
            break
        
        mid = (left + right) / 2
        mid_value = func(mid)
        
        if abs(mid_value - target) < epsilon:
            return mid
        elif mid_value < target:
            left = mid
        else:
            right = mid
    
    return (left + right) / 2


def square_root_binary_search(n, epsilon=1e-9):
    """
    使用二分法计算平方根
    
    Args:
        n: 正数
        epsilon: 精度
    
    Returns:
        n 的平方根
    """
    if n < 0:
        raise ValueError("输入必须是非负数")
    
    if n == 0 or n == 1:
        return n
    
    left, right = 0, max(1, n)
    
    while right - left > epsilon:
        mid = (left + right) / 2
        square = mid * mid
        
        if square < n:
            left = mid
        else:
            right = mid
    
    return (left + right) / 2


def demo_basic_search():
    """演示基础二分查找"""
    print("=== 基础二分查找演示 ===")
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(f"数组: {arr}")
    
    test_cases = [7, 15, 2, 20]
    for target in test_cases:
        # 迭代版本
        result_iter = binary_search_iterative(arr, target)
        # 递归版本
        result_rec = binary_search_recursive(arr, target)
        
        print(f"查找 {target}:")
        print(f"  迭代版本结果: {result_iter}")
        print(f"  递归版本结果: {result_rec}")
        
        if result_iter != -1:
            print(f"  找到！位置: {result_iter}, 值: {arr[result_iter]}")
        else:
            insert_pos = binary_search_insert_position(arr, target)
            print(f"  未找到，应该插入位置: {insert_pos}")
        print()


def demo_range_search():
    """演示范围查找"""
    print("=== 范围查找演示 ===")
    arr = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6]
    print(f"数组: {arr}")
    
    test_cases = [2, 4, 5, 7]
    for target in test_cases:
        range_result = binary_search_range(arr, target)
        print(f"查找 {target} 的范围: {range_result}")
        
        if range_result[0] != -1:
            count = range_result[1] - range_result[0] + 1
            print(f"  出现次数: {count}")
        print()


def demo_float_search():
    """演示浮点数二分法"""
    print("=== 浮点数二分法演示 ===")
    
    # 计算平方根
    numbers = [4, 9, 16, 25, 2, 10]
    for n in numbers:
        sqrt_result = square_root_binary_search(n)
        print(f"{n} 的平方根 ≈ {sqrt_result:.6f}")
        print(f"  验证: {sqrt_result:.6f}² = {sqrt_result**2:.6f}")
    
    print()
    
    # 求解方程 x³ - 2x - 5 = 0
    def cubic_func(x):
        return x**3 - 2*x - 5
    
    solution = binary_search_float(cubic_func, 0, 1, 3)
    print(f"方程 x³ - 2x - 5 = 0 在区间 [1, 3] 的解: x ≈ {solution:.6f}")
    print(f"验证: f({solution:.6f}) = {cubic_func(solution):.6f}")


def run_performance_test():
    """性能测试"""
    import time
    import random
    
    print("=== 性能测试 ===")
    
    # 创建大数组
    size = 1000000
    arr = list(range(0, size * 2, 2))  # 偶数数组
    target = random.choice(arr)
    
    # 测试迭代版本
    start_time = time.time()
    result_iter = binary_search_iterative(arr, target)
    iter_time = time.time() - start_time
    
    # 测试递归版本
    start_time = time.time()
    result_rec = binary_search_recursive(arr, target)
    rec_time = time.time() - start_time
    
    # 测试Python内置方法
    import bisect
    start_time = time.time()
    bisect_pos = bisect.bisect_left(arr, target)
    bisect_result = bisect_pos if bisect_pos < len(arr) and arr[bisect_pos] == target else -1
    bisect_time = time.time() - start_time
    
    print(f"数组大小: {size:,}")
    print(f"目标值: {target}")
    print(f"迭代版本: 结果={result_iter}, 时间={iter_time:.6f}s")
    print(f"递归版本: 结果={result_rec}, 时间={rec_time:.6f}s")
    print(f"bisect模块: 结果={bisect_result}, 时间={bisect_time:.6f}s")


if __name__ == "__main__":
    print("二分法算法示例程序")
    print("=" * 50)
    
    # 运行各种演示
    demo_basic_search()
    demo_range_search()
    demo_float_search()
    run_performance_test()
    
    print("\n程序执行完成！")