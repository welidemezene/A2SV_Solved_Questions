class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_arr = [0] * (n + 1)

        # Step 1: Apply shifts efficiently
        for start, end, direction in shifts:
            if direction == 1:
                shift_arr[start] += 1
                shift_arr[end + 1] -= 1
            else:
                shift_arr[start] -= 1
                shift_arr[end + 1] += 1

        # Step 2: Compute prefix sum
        for i in range(1, n):
            shift_arr[i] += shift_arr[i - 1]

        # Step 3: Apply shifts to characters
        result = []
        for i in range(n):
            new_char = chr((ord(s[i]) - ord('a') + shift_arr[i]) % 26 + ord('a'))
            result.append(new_char)

        return "".join(result)