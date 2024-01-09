def is_palindrome(s):
    """_summary_

    Args:
        s (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Replace this placeholder return statement with your code
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    # ************************************************************
    # *********************** DNA Sequence ***********************
    test_cases = ["RACEACAR", "A", "ABCDEFGFEDCBA",
                  "ABC", "ABCBA", "ABBA", "RACEACAR"]
    i = 1
    for s in test_cases:
        print("Test Case #", i)
        print(is_palindrome(s))
        print("-" * 100, end="\n\n")
        i = i + 1
    # ************************************************************
