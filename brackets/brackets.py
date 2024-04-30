def check_brackets(sequence_brackets: str):
    brackets = {
        "{":"}",
        "(":")",
        "[":"]",
    }
    left = 0
    right = len(sequence_brackets) - 1
    while left < right:
        left_bracket = sequence_brackets[left]
        right_bracket = sequence_brackets[right]

        is_right_bracket_opening = right_bracket in brackets.keys()
        is_left_bracket_closing = left_bracket in brackets.values()

        if is_left_bracket_closing or is_right_bracket_opening:
            return False

        if brackets[left_bracket] != right_bracket:
            return False

        left += 1
        right -= 1
    return True
