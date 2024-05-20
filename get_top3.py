def check_fcis():
    aux=[]
    with open('fci_performances', 'r') as file:
        for line in file:
            aux.append(line.rstrip())
    i=0
    fcis=[]
    for j in range(3):
        if aux[i][:-1] == aux[i+4][:-1]:
            fcis.append(aux[i])
            fcis.extend([aux[i+1],aux[i+2],aux[i+3]])
            i+=8
        else:
            fcis.append(aux[i])
            fcis.extend([aux[i+1],aux[i+2],aux[i+3]])
            i+=4
    return fcis 

fcis=check_fcis()
print(fcis)
