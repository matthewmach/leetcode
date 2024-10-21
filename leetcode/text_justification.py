# Idea: keep counter of extra_spaces needed to pad between
#       modulo number of spaces left tells you if you need to add additional
#       if space = 0 or last line, append all extra spaces to the end
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        out = []
        i = 0
        words = words[::-1]
        while len(words) > 0:
            line = []
            count = maxWidth
            space = 0
            while count-space > 0 and len(words) > 0 and len(words[-1]) <= count-space:
                word = words.pop()
                line.append(word)
                count -= len(word) # count space
                space += 1            

            space -= 1 # no space on last word
            extra_space = count - space

            line_str = ""
            for w in line:
                line_str = line_str + w
                add_spaces = 1
                
                print (w, space, extra_space)
                if len(words) > 0:
                    if space > 0 and extra_space > 0:
                        if extra_space % space > 0:
                            add_spaces += 1
                            extra_space -= 1
                        add_spaces += extra_space//space
                        extra_space -= extra_space//space
                    elif space == 0:
                        add_spaces = extra_space
                        extra_space = 0
                else:
                    if w == line[-1]:
                        add_spaces += extra_space -1

                for i in range(add_spaces):
                    line_str = line_str + " "
                space -= 1

            out.append(line_str)

        return out