def func(nums, n):
    if n < 0:
        return 0
    
    if n == 0:
        return nums[0]
    
    left = nums[n] + func(nums, n-2)
    right = func(nums, n - 1)

    return max(left, right)

def main():
    nums = [1,2, 3, 4, 1]
    n = len(nums)
    print(func(nums, n-1))

if __name__ == "__main__":
    main()