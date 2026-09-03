def solution(n):
    return sum(list(map(lambda string: int(string), str(n))))
    
def format_newspaper(paragraphs, aligns, width):
    result = []
    border = "*" * (width + 2)
    result.append(border)
    for j in range(len(aligns)):
        align, paragraph = aligns[j], paragraphs[j]
        words = paragraph.split()
        i = 0
        
        while i < len(words):
            line = words[i]
            i += 1
            
            while i < len(words):
                candidate = line + " " + words[i]
                if len(candidate) <= width:
                    line = candidate
                    i += 1
                else:
                    break
        
            padding = width - len(line)
            if align == "LEFT":
                padded = line + padding * " "
            elif align == "RIGHT":
                padded = padding * " " + line 
            result.append("*" + padded + "*")
    result.append(border)
    
    return result

paragraphs = [
  "one two three four",
  "hello world",
  "a"
]

aligns = [
  "LEFT",
  "RIGHT",
  "LEFT"
]

width = 9

result = format_newspaper(paragraphs, aligns, width)
for row in result:
    print(row)