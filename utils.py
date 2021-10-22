def get_max(nums):
    my_max = nums[0]
    for num in nums:
        if num > my_max:
            my_max = num
    return my_max
