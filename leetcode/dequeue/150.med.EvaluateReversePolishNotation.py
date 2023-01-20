from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set("+-*/")
        for t in tokens:
            if t in ops:
                sec = stack.pop()
                first = stack.pop()
                seq = first + t + sec
                res = int(eval(seq))
                stack.append(str(res))
            else:
                stack.append(t)
        return int(stack.pop())


class OfficialSolution:
    def evalRPN(self, tokens: List[str]) -> int:

        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b,
        }

        stack = []
        for token in tokens:
            if token in operations:
                number_2 = stack.pop()
                number_1 = stack.pop()
                operation = operations[token]
                stack.append(operation(number_1, number_2))
            else:
                stack.append(int(token))
        return stack.pop()
