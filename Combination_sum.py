class Solution:
    def combinationSum(self, arr, target):
        arr = sorted(set(arr))
        output = []
        def get_sample(val, path, start):
            if val == target:
                output.append(path)
                return
            for i in range(start, len(arr)):
                new_val = val + arr[i]
                if new_val <= target:
                    get_sample(new_val, path + [arr[i]], i) 
                else:
                    break 

        get_sample(0, [], 0)
        return output 