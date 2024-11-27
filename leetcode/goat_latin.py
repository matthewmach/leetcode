class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {"a", "e", "i", "o", "u"}
        word = ""
        out = []
        index = 1
        for i in range(len(sentence)):
            c = sentence[i]
            if c != " ":
                word = word + c
            if c == " " or i == len(sentence) - 1:
                print (word)
                if word[0].lower() not in vowels:
                    word = word[1:] + word[0]
                word = word + "ma"
                for i in range(index):
                    word = word + "a"
                out.append(word)
                word = ""
                index += 1
        return " ".join(out)
        