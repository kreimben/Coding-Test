"""
https://www.algoexpert.io/questions/balanced-brackets
Balanced Brackets
"""


def balancedBrackets(string):
    stack = []
    for ch in string:
        if not stack:
            if not ch.isalnum():
                stack.append(ch)
            continue

        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        elif ch == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif ch == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                return False
        elif ch == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                return False

    if not stack:  # empty state
        return True
    else:
        return False


assert balancedBrackets("(141[])(){waga}((51afaw))()hh()") == True
assert balancedBrackets("(a)") == True
assert balancedBrackets("()([])") == True
assert balancedBrackets("([])(){}(())()()") == True
