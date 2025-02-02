# https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/description/


class Solution:
    def minimizeResult(self, expression: str) -> str:
        num1, num2 = expression.split("+")

        def if_not_to_one(s: str) -> str:
            if not s:
                return "1"
            return s

        min_val = float("inf")
        min_val_exp = ""

        for i in range(len(num1)):
            for j in range(1, len(num2) + 1):
                val = (
                    int(if_not_to_one(ll := num1[:i]))
                    * (int(l := num1[i:]) + int(r := num2[:j]))
                    * int(if_not_to_one(rr := num2[j:]))
                )
                if val < min_val:
                    min_val = val
                    min_val_exp = f"{ll}({l}+{r}){rr}"

        return min_val_exp
