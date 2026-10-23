def to_min(time):
    split = time.split(":")
    h = int(split[0])*60
    m = int(split[1])
    return h+m

def format_time(time):
    days = time//24//60
    hours = time // 60 % 24
    minut = time % 60
    out = ""
    if days >= 1 :
        out += f"{days} day"
    if days > 1:
        out += f"s"

    if hours > 0 and days > 0:
        out += ", "

    if hours >= 1:
        out += f"{hours} hour"
    if hours > 1:
        out += f"s"
        
    if hours > 0 and minut > 0:
        out += ", "
    if minut >= 1:
        out += f"{minut} minute"
    if minut > 1:
        out += f"s"
    if len(out.split(",")) == 2:
        out = out.replace(", "," and ")
        
    return out

    
 

inp = input().split(" ")
date1 = inp[0]
time1 = to_min(inp[1])

inp = input().split(" ")
date2 = inp[0]
time2 = to_min(inp[1])


wd = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]



index1 = wd.index(date1)
index2 = wd.index(date2)

if index1 > index2:
    index2 += 7

if date1 == date2:
    if time1 > time2:
        index2 += 7
    elif time1 == time2:
        print("7 days")
        exit()

        
time1 = time1 + index1*24*60
time2 = time2 + index2*24*60


print(format_time(time2-time1))



