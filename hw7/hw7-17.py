# тут переплутали одне завдання з іншим чомусь)

def decode(data):
    if data == []:
        return []
    
    output = []

    for i in range(len(data)):
        
        if str(data[i]).isdigit():
            for k in range(int(data[i])-1):
                output.append(data[i-1])
            output = output + data[i+1:]
            print('output = ', output)
            return decode(output)
        elif not str(data[i]).isdigit():
            output.append(data[i])

    return output



s = ['X', 3, 'Z', 2, 'X', 2, 'Y', 3, 'Z', 2]
decode(s)