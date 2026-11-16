"""
Given a string of up to 100,000 characters containing only
'(', ')', '[', ']', '{', and '}', return True if it is valid.

Every opening bracket must have a matching closing bracket.
Brackets must close in the correct order.
An empty string is valid.

Example: "([])" → True
Example: "([)]" → False

Pattern: Stack — Last In, First Out (LIFO)

"""


def valid_parentheses(text: str) -> bool:
  stack: list[str] = [] # track opening brackets waiting to close

  pairs = {")": "(", "]": "[", "}": "{"}  # match closings to openings

  for bracket in text:  # read each bracket left to right
    if bracket in "([{":   # is it opening bracket
      stack.append(bracket)   # add to top of stack
    else:
      if not stack:    # if no opening bracket
        return False
  
      if stack.pop() != pairs[bracket]:  # check latest opening
        return False
  
  return not stack #valid only if every opening bracket was matched



if __name__ == "__main__":
    assert valid_parentheses("([])") is True
    assert valid_parentheses("([)]") is False
    print("Both checks passed!")


# Time: O(n)
# Extra Space: O(n) in the worst case





