def IncrVal(num):
    print(f"Parameter num has value {num} \nid=",id(num))
    num+=5
    print(f"Id after number incremented by 5 is {id(num)}")
IncrVal(5)