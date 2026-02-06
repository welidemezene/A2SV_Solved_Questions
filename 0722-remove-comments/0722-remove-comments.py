class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        in_block = False
        
        new_line_buffer = []
        for line in source:
            i = 0
            while i < len(line):
                char = line[i]

                if in_block:
                    if i+1 < len(line) and char == "*" and line[i+1] == "/":
                        
                        in_block = False
                        i+=1
                else:
                    if i+1 < len(line) and char == "/" and line[i+1] == "*":
                        
                        in_block = True
                        i+=1
                    elif i+1 < len(line) and char == "/" and line[i+1] == "/": 
                        break
                    else:
                        new_line_buffer.append(char)  
                i+=1
            if not in_block and new_line_buffer:
                res.append("".join(new_line_buffer)) 
                new_line_buffer = []  
        return res                          
        
        