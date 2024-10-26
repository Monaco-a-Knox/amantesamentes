import os, re, textwrap

def walk(adr):
    mylist = []
    for root, dirs, files in os.walk(adr):
        for name in files:
            adrlist = os.path.join(root, name)
            mylist.append(adrlist)
    return mylist


def create_file(dstname):
    if not os.path.exists(os.path.dirname(dstname)):
        os.makedirs(os.path.dirname(dstname))

fl = walk('script')
sumlen = 0

for fn in fl:
    src = open(fn, 'r', encoding='utf8')
    script_lines = src.readlines()

    dstname = 'script_done' + fn[6:-3] + 'txt'
    create_file(dstname)
    dst = open(dstname, 'w', encoding='utf8')
    
    #get the number of lines
    line_count = 0
    for line in script_lines: line_count += 1
    
    for i in range(line_count):
      line = script_lines[i]

      #split up lines that are too long to fit on-screen
      line_len = len(line)
      new_line = ""
      done_newline = False
      if not ord(line[0]) == 9670: continue #first character must be ◆
      message_len = 0
      is_message = 0
      
      for j in range(line_len):
        character = line[j]
        if ord(character) == 9670: #find the second ◆, where message starts
          is_message += 1

        if is_message >= 2:
          if character == " " and message_len > 25: #add a [n] after a space, when character count is over 30
            new_line = new_line + "[n]"
            message_len = 0
            continue
            
        if is_message >= 2: message_len += 1
        new_line = new_line + character
        
      script_lines[i] = new_line
 
    dst.writelines(script_lines)
    dst.close()