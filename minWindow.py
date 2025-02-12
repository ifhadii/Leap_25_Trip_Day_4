from collections import defaultdict
from typing import List
def minWindow(s, t):
    if not s or not t or len(s) < len(t):
        return ""

    target_counts = defaultdict(int)
    for char in t:
        target_counts[char] += 1

    left = 0
    min_length = float('inf')
    min_window = ""
    required = len(target_counts)
    formed = 0
    window_counts = defaultdict(int)

    for right in range(len(s)):
        char = s[right]
        window_counts[char] += 1

        if char in target_counts and window_counts[char] == target_counts[char]:
            formed += 1

        while left <= right and formed == required:
            current_window_length = right - left + 1

            if current_window_length < min_length:
                min_length = current_window_length
                min_window = s[left:right + 1]

            left_char = s[left]
            window_counts[left_char] -= 1

            if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                formed -= 1

            left += 1

    return min_window

