
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
    for i in range(0, n-k+1):
        sub_str = s[i:i+k]
        if sub_str not in include_set:
            include_set.append(sub_str)
        else:
            if isinstance(output_set, list):
                if sub_str not in output_set:
                    output_set.append(sub_str)
            else:
                output_set.add(sub_str)
    return output_set


if __name__ == "__main__":
    STRING = "AAAAACCCCCAAAAACCCCCC"
    k = 8

    STRING = "GGGGGGGGGGGGGGGGGGGGGGGGG"
    k = 9
    output = find_repeated_seq_naive(s=STRING, k=k)
    print(output)
