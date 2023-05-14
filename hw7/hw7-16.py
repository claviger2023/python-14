def encode(data):
    if data == []:
        return []
    
    output = []
    
    counter = 1

    for i in range(len(data)):
        if i == 0:
            output.append(data[0])
        
        else:
            if data[i] == data[0]:
                counter +=1
            else:
                output.append(counter)
                
                for k in range(len(data)):
                    if k >= i:
                        output.append(data[k])
                
                return print(output)            
        


s = 'XXXZZXXYYYZZ'

encode(s)

