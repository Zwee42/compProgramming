 
 
line = input()
# times = len(line.split(" \"Revert \""))-1

is_revert = False

while (True):
    val = line[:8] 
    if val == "Revert \"":
        is_revert = not is_revert
    else:
        break
    # print(line)
    line = line[8:]
    if(len(line) < 9):
        break
    
print("revert" if is_revert else "unrevert")

# if line[:8] == "Revert \"":
#     times += 1
#     print("unrevert" if times % 2 == 0 else "revert")
# else: print("unrevert")



# def is_revert(s):
#     splits = s.split("\"", 1)
#     if len(splits) > 1 and len(splits[0]) > 0 and splits[0][-1] != "\\":
#         a = is_revert(splits[1])
#         if a and splits[0].strip() == "Revert": return False
#         elif not a and splits[0].strip() == "Revert": return True
#     elif len(splits) > 0:
#         return splits[0][:6] == "Revert"
#     else: return False

# inp = input()
# print("revert" if is_revert(inp) else "unrevert")