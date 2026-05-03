

 # utf-8 for tr char
def read_html_file(file_path):
    with open(file_path, 'r', encoding ='utf-8') as file :
        return file.read()
    
# colored HTML file
# copy text with all false, change with true when text matched 
def createMarkedHTML(text,matches,pattern_length,output_path):
    is_marked = [False] * len(text)

    for idx in matches:
        for i in range(idx,idx + pattern_length):
            if i<len(text):
                is_marked[i] = True
    
    result = []
    in_mark = False

    # If it is matched but not marked then we have to marked
    for i in range(len(text)):

        if is_marked[i] and not in_mark:
            result.append("<mark>")
            in_mark = True
        
        # İf not matched (False) but in_mark we have to mark return false,finish mark-mark
        elif not is_marked[i] and in_mark:
            result.append("</mark>")
            in_mark = False

        result.append(text[i])
    
    if in_mark:
        result.append("</mark>")
    
    #write, new file
    with open(output_path, 'w',encoding='utf-8') as f:
        f.write("".join(result))