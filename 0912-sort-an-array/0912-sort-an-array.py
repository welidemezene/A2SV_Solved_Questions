class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        This function takes a list of numbers (nums) and returns a sorted version of it
        using the merge_sort algorithm.
        """
        # Calling to start sorting
        return self.merge_sort(nums)

    def merge(self, left_half, right_half):
        """
        Merges two sorted lists (left_half and right_half) into one sorted list.
        """
        result = []
        i = j = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                result.append(left_half[i])
                i += 1
            else:
                result.append(right_half[j])
                j += 1
                
        result.extend(left_half[i:])
        result.extend(right_half[j:])
        return result

    def merge_sort(self, arr):
        """
        Sorts a list of numbers (arr) using the merge sort algorithm.
        """
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_part = arr[:mid]
        right_part = arr[mid:]

        sorted_left = self.merge_sort(left_part)
        sorted_right = self.merge_sort(right_part)

        return self.merge(sorted_left, sorted_right)