class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:


        def backtrack(pattern_idx: int, string_idx: int) -> bool:

            if pattern_idx == pattern_length and string_idx == string_length:
                return True

            if (pattern_idx == pattern_length or
                string_idx == string_length or
                string_length - string_idx < pattern_length - pattern_idx):
                return False

            current_pattern_char = pattern[pattern_idx]

            for end_idx in range(string_idx, string_length):
                substring = s[string_idx:end_idx + 1]

                if pattern_to_string.get(current_pattern_char) == substring:
                    if backtrack(pattern_idx + 1, end_idx + 1):
                        return True

                elif current_pattern_char not in pattern_to_string and substring not in used_substrings:
                    pattern_to_string[current_pattern_char] = substring
                    used_substrings.add(substring)

                    if backtrack(pattern_idx + 1, end_idx + 1):
                        return True

                    del pattern_to_string[current_pattern_char]
                    used_substrings.remove(substring)

            return False

        pattern_length = len(pattern)
        string_length = len(s)
        pattern_to_string = {}  
        used_substrings = set() 

        return backtrack(0, 0)
