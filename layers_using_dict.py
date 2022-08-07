alphabets={1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",16:"P",
17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z"}
layer=int(input("Layers:"))
times=layer*2-1
for i in range(layer,0,-1):
    for j in range(layer,i,-1):
        print(alphabets[j],end="")
    print(times*alphabets[i],end="")
    times-=2
    for k in range(i+1,layer+1):
        print(alphabets[k],end="")
    print()
times=3
for i in range(2,layer+1):
    for j in range(layer,i,-1):
        print(alphabets[j],end="")
    print(times*alphabets[i],end="")
    times+=2
    for k in range(i+1,layer+1):
        print(alphabets[k],end="")
    print()
