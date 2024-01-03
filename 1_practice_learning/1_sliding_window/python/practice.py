def find_repeated_seq_naive(s, k):
    """_summary_

    Args:
        s (_type_): _description_
        k (_type_): _description_

    Returns:
        _type_: _description_
    """
    n = len(s)
    output_set = []
    include_set = []
    output_set = set()
    for i in range(0, n - k + 1):
        sub_str = s[i : i + k]
        if sub_str not in include_set:
            include_set.append(sub_str)
        else:
            if isinstance(output_set, list):
                if sub_str not in output_set:
                    output_set.append(sub_str)
            else:
                output_set.add(sub_str)
    return output_set


def find_repeated_seq_opt(s, k):
    """_summary_

    Args:
        s (_type_): _description_
        k (_type_): _description_

    Returns:
        _type_: _description_
    """
    window_size = k
    if len(s) <= window_size:
        return set()
    base = 4
    hi_place_value = pow(base, window_size - 1)
    mapping = {"A": 1, "C": 2, "G": 3, "T": 4}
    numbers = []
    for i, _ in enumerate(s):
        numbers.append(mapping.get(s[i]))
    hashing = 0
    substring_hashes, output = set(), set()
    for start in range(len(s) - window_size + 1):
        if start != 0:
            hashing = (hashing - numbers[start - 1] * hi_place_value) * base + numbers[
                start + window_size - 1
            ]
        else:
            for end in range(window_size):
                hashing = hashing * base + numbers[end]
        if hashing in substring_hashes:
            output.add(s[start : start + window_size])
        substring_hashes.add(hashing)
    return output


def find_max_sliding_window_naive(nums, w):
    """_summary_

    Args:
        nums (_type_): _description_
        w (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Replace this placeholder return statement with your code
    n = len(nums)
    output = []
    for i in range(0, n - w + 1):
        output.append(max(nums[i : i + w]))
    return output


def find_max_sliding_window_opt(nums, w):
    from collections import deque

    """_summary_

    Args:
        nums (_type_): _description_
        w (_type_): _description_

    Returns:
        _type_: _description_
    """
    output = []

    def clean_up(i, current_window, numbs, flag_deque):
        """_summary_

        Args:
            i (_type_): _description_
            current_window (_type_): _description_
            numbs (_type_): _description_
        """
        while current_window and numbs[i] >= numbs[current_window[-1]]:
            print(
                f"\t\tAs nums[{i}] = {nums[i]} is greater than or equal to nums[{current_window[-1]}] = {nums[current_window[-1]]},"
            )
            print(f"\t\tremove {current_window[-1]} from current_window")
            if flag_deque:
                current_window.pop()
            else:
                del current_window[-1]

    if len(nums) == 0:
        return []

    # current_window = []
    current_window = deque()

    if isinstance(current_window, list):
        flag_deque = False
    else:
        flag_deque = True

    if w > len(nums):
        w = len(nums)

    print("\n\tFinding the maximum in the first window:")
    for i in range(w):
        clean_up(i, current_window, nums, flag_deque)
        current_window.append(i)
    output.append(nums[current_window[0]])

    print("\n\tFinding the maximum in the remaining windows:")
    for i in range(w, len(nums)):
        clean_up(i, current_window, nums, flag_deque)

        if current_window and current_window[0] <= (i - w):
            if flag_deque:
                current_window.popleft()
            else:
                del current_window[0]

        current_window.append(i)
        output.append(nums[current_window[0]])

    return output


def min_window_naive(str1, str2):
    """_summary_

    Args:
        str1 (_type_): _description_
        str2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Replace this placeholder return statement with your code
    n1 = len(str1)
    n2 = len(str2)
    output = []
    for i in range(n1):
        for j in range(i, n1):
            substr = str1[i:j]
            if str2[0] != substr[0]:
                break
            for k in range(n2):
                if str2[k] not in substr:
                    break

    return ""


def min_window_opt(str1, str2):
    """_summary_

    Args:
        str1 (_type_): _description_
        str2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Replace this placeholder return statement with your code
    size_str1, size_str2 = len(str1), len(str2)
    min_sub_len = float("inf")

    index_s1, index_s2 = 0, 0

    print("\t Length of str1 is: ", size_str1)
    print("\t Length of str2 is: ", size_str2)

    min_subseq = ""
    start, end = 0, 0
    while index_s1 < size_str1:
        if str1[index_s1] == str2[index_s2]:
            if index_s2 == 0:
                start = index_s1
            index_s2 += 1

            # check if a valid substring has been found
            if index_s2 == size_str2:
                end = index_s1

                if end - start + 1 < min_sub_len:
                    min_sub_len = end - start + 1
                    min_subseq = str1[start : end + 1]

                index_s1 = end + 1
                index_s2 = 0
                continue
        index_s1 += 1
    print(f" **** Found item = {min_subseq}, **** start = {start}, **** end = {end}")
    return min_subseq


if __name__ == "__main__":
    """
    # ************************************************************
    # *********************** DNA Sequence ***********************
    STRING = "AAAAACCCCCAAAAACCCCCC"
    k = 8

    STRING = "GGGGGGGGGGGGGGGGGGGGGGGGG"
    k = 9
    output = find_repeated_seq_naive(s=STRING, k=k)
    print(output)

    inputs_string = ["ACGT", "AGACCTAGAC", "AAAAACCCCCAAAAACCCCCC", "GGGGGGGGGGGGGGGGGGGGGGGGG",
                     "TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT", "TTTTTGGGTTTTCCA",
                     "AAAAAACCCCCCCAAAAAAAACCCCCCCTG", "ATATATATATATATAT"]
    inputs_k = [3, 3, 8, 12, 10, 14, 10, 6]

    for j, _ in enumerate(inputs_k):
        print(j+1, ".\tInput Sequence: \'", inputs_string[j], "\'", sep="")
        print("\tk: ", inputs_k[j], sep="")
        print("\tRepeated Subsequence: ",
              find_repeated_seq_opt(inputs_string[j], inputs_k[j]))
        print("-"*100)

    # ************************************************************
    # *********************** Max Sliding Window ***********************
    nums_list = [[1,2,3,4,5,6,7,8,9,10],
                 [3,3,3,3,3,3,3,3,3,3],
                 [10,6,9,-3,23,-1,34,56,67,-1,-4,-8,-2,9,10,34,67],
                 [4,5,6,1,2,3],
                 [9,5,3,1,6,3]]
    windows = [3, 4, 3, 1, 2]
    for i, nums in enumerate(nums_list):
        print(find_max_sliding_window_naive(nums, windows[i]))

    window_sizes = [3, 3, 3, 3, 2, 4, 3, 2, 3, 18]
    nums_list = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [1, 5, 8, 10, 10, 10, 12, 14, 15, 19, 19, 19, 17, 14, 13, 12, 12, 12, 14, 18, 22, 26, 26, 26, 28, 29, 30],
        [10, 6, 9, -3, 23, -1, 34, 56, 67, -1, -4, -8, -2, 9, 10, 34, 67],
        [4, 5, 6, 1, 2, 3],
        [9, 5, 3, 1, 6, 3],
        [2, 4, 6, 8, 10, 12, 14, 16],
        [-1, -1, -2, -4, -6, -7],
        [4, 4, 4, 4, 4, 4]
    ]

    for i, _ in enumerate(nums_list):
        print(f"{i + 1}.\tInput array:\t{nums_list[i]}")
        print(f"\tWindow size:\t{window_sizes[i]}")
        output = find_max_sliding_window_opt(nums_list[i], window_sizes[i])
        print(f"\n\tMaximum in each sliding window:\t{output}")
        print("-"*100)

    # ************************************************************
    # *********************** min window subsequence ***********************
    """
    str1_list = ["abcdebdde", "fgrqsqsnodwmxzkzxwqegkndaa", "zxcvnhss", "alpha", "beta"]
    str2_list = ["bde", "kzed", "css", "la", "ab"]

    for i, (val1, val2) in enumerate(zip(str1_list, str2_list)):
        print(i + 1, ".\t Input strings: (" + val1 + ", " + val2 + ")", sep="")
        min_window_opt(val1, val2)
        print("-" * 100)

    # ************************************************************
