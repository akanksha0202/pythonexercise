ipAddress = input("Please enter an TP address: ")
if ipAddress[-1] != '.':
    ipAddress += '.'
segment = 1
length = 0

for character in ipAddress:
    if character == '.':
        print("segment {} contains {} characters".format(segment, length))
        segment += 1
        length = 0
    else:
        length +=1

if character != '.':
    print("segment {} contains {} characters".format(segment, length))
