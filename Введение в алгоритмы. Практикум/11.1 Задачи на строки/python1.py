"""Strings."""
from typing import Callable


class Solution:
    """Solution."""

    __methods = {"longestPalindrome": "longest_palindrome",
                 "countSubstrings": "count_substrings",
                 "minSteps": "min_steps",
                 "longestCommonPrefix": "longest_common_prefix",
                 "lengthOfLongestSubstring": "length_of_longest_substring",
                 "maxFreq": "max_freq"}

    def __getattr__(self, attr: str) -> Callable:
        """Attribute correction."""
        return getattr(self, self.__methods[attr])

    @staticmethod
    def longest_palindrome(str_s: str) -> str:  # алгоритм Манакера
        """Longest palindrome."""
        str_s = "#".join([""] + list(str_s) + [""])
        length, maximum = len(str_s), [1, 0]
        tab, left, right = [1] * length, 0, -1
        for i in range(length):
            if i <= right:
                tab[i] = min(tab[left + right - i], right - i + 1)
            i_min = min(i + 1, length - i)
            while tab[i] < i_min and str_s[i + tab[i]] == str_s[i - tab[i]]:
                tab[i] += 1
            if i + tab[i] - 1 > right:
                right = i + tab[i] - 1
                left = i - tab[i] + 1
            if maximum[0] < tab[i]:
                maximum = [tab[i], i]
        return str_s[maximum[1] - maximum[0] + 2:maximum[1] + maximum[0]:2]

    @staticmethod
    def count_substrings(str_s: str) -> int:
        """Count substrings-palindromes."""
        str_s = "#".join([""] + list(str_s) + [""])
        length, total = len(str_s), 0
        tab, left, right = [1] * length, 0, -1
        for i in range(length):
            if i <= right:
                tab[i] = min(tab[left + right - i], right - i + 1)
            i_min = min(i + 1, length - i)
            while tab[i] < i_min and str_s[i + tab[i]] == str_s[i - tab[i]]:
                tab[i] += 1
            if i + tab[i] - 1 > right:
                right = i + tab[i] - 1
                left = i - tab[i] + 1
            total += tab[i] >> 1
        return total

    @staticmethod
    def min_steps(str_s: str, str_t: str) -> int:
        """Count of steps from str_t to anagram str_s."""
        my_dict = {}
        for char_s in str_s:
            my_dict[char_s] = my_dict.get(char_s, 0) + 1
        for char_t in str_t:
            my_dict[char_t] = my_dict.get(char_t, 0) - 1
        return sum(val for val in my_dict.values() if val > 0)

    @staticmethod
    def longest_common_prefix(strings: list[str]) -> str:
        """Longest common prefix."""
        if not strings:
            return ""
        end = min(map(len, strings))
        for string in strings:
            for i in range(end):
                if strings[0][i] != string[i]:
                    end = i
                    break
        return strings[0][:end]

    @staticmethod
    def length_of_longest_substring(str_s: str) -> int:
        """Length of the longest substring without repetitions."""
        my_dict = dict.fromkeys(set(str_s), -1)
        result, maximum = 0, 0
        for i, char_s in enumerate(str_s):
            maximum = min(maximum + 1, i - my_dict[char_s])
            result = max(result, maximum)
            my_dict[char_s] = i
        return result

    @staticmethod
    def max_freq(str_s: str, max_letters: int, min_size: int, _: int) -> int:
        """Maximum count of occurrences of substring.

        1) count of unique characters in substring <= max_letters;
        2) min_size <= count of characters.
        """
        count = {}
        for i in range(len(str_s) - min_size + 1):
            sub_str = str_s[i:i + min_size]
            if len(set(sub_str)) <= max_letters:
                count[sub_str] = count.get(sub_str, 0) + 1
        return max(count.values(), default=0)


def problem_1() -> None:
    """Problem 1."""
    strings, results = ["babad", "cbbd"], ["bab", "bb"]
    for string, result in zip(strings, results):
        assert Solution.longest_palindrome(string) == result


def problem_2() -> None:
    """Problem 2."""
    strings, results = ["abc", "aaa"], [3, 6]
    for string, result in zip(strings, results):
        assert Solution.count_substrings(string) == result


def problem_3() -> None:
    """Problem 3."""
    strings = [("bab", "aba"), ("anagram", "mangaar"), ("friend", "family")]
    results = [1, 0, 4]
    for str_s_t, result in zip(strings, results):
        assert Solution.min_steps(*str_s_t) == result


def problem_4() -> None:
    """Problem 4."""
    strings = [["flower", "flow", "flight"], ["dog", "racecar", "car"]]
    results = ["fl", ""]
    for lst, result in zip(strings, results):
        assert Solution.longest_common_prefix(lst) == result


def problem_5() -> None:
    """Problem 5."""
    strings, results = ["abcabcbb", "bbbbb", "pwwkew"], [3, 1, 3]
    for string, result in zip(strings, results):
        assert Solution.length_of_longest_substring(string) == result


def problem_6() -> None:
    """Problem 6."""
    tuples = [("aababcaab", 2, 3, 4), ("aaaa", 1, 3, 3),
              ("aabcabcab", 2, 2, 3)]
    results = [2, 2, 3]
    for my_tuple, result in zip(tuples, results):
        assert Solution.max_freq(*my_tuple) == result


def main():
    """My function."""
    problem_1()
    problem_2()
    problem_3()
    problem_4()
    problem_5()
    problem_6()


if __name__ == "__main__":
    main()
