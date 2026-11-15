
class Solution:

    def encode(self, strs: list[str]) -> str:

        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result


    def decode(self, s: str) -> list[str]:

        result = []

        i = 0

        while i < len(s):

            j = s.find("#", i)

            length = int(s[i:j])

            i = j + 1

            word = s[i:i + length]

            result.append(word)

            i = i + length

        return result

