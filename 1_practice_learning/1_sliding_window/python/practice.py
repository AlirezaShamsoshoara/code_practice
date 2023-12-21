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
    mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    numbers = []
    for i, _ in enumerate(s):
        numbers.append(mapping.get(s[i]))
    hashing = 0
    substring_hashes, output = set(), set()
    for start in range(len(s) - window_size + 1):
        if start != 0:
            hashing = (hashing - numbers[start - 1] * hi_place_value) * base \
                + numbers[start + window_size - 1]
        else:
            for end in range(window_size):
                hashing = hashing * base + numbers[end]
        if hashing in substring_hashes:
            output.add(s[start:start + window_size])
        substring_hashes.add(hashing)
    return output


if __name__ == "__main__":
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

    for i, _ in enumerate(inputs_k):
        print(i+1, ".\tInput Sequence: \'", inputs_string[i], "\'", sep="")
        print("\tk: ", inputs_k[i], sep="")
        print("\tRepeated Subsequence: ",
              find_repeated_seq_opt(inputs_string[i], inputs_k[i]))
        print("-"*100)
