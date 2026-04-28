class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            current_max = -1
            for j in range(i + 1, len(arr)):
                if arr[j] > current_max:
                    current_max = arr[j]
            arr[i] = current_max
        return arr