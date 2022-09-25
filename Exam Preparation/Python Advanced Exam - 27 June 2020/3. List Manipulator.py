def list_manipulator(nums, cmd, *args):
    if cmd == "add" and args[0] == "beginning":
        return list(args[1:]) + nums
    if cmd == "add" and args[0] == "end":
        return nums + list(args[1:])
    if cmd == "remove" and args[0] == "beginning":
        if len(args) == 1:
            return nums[1:]
        else:
            return nums[args[1]:]
    if cmd == "remove" and args[0] == "end":
        if len(args) == 1:
            return nums[:-1]
        else:
            return nums[:-args[1]]



#
print(list_manipulator([1,2,3], "remove", "end"))
# print(list_manipulator([1,2,3], "remove", "beginning"))
# print(list_manipulator([1,2,3], "add", "beginning", 20))
# print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
# print(list_manipulator([1,2,3], "remove", "beginning", 2))
# print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
# print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
