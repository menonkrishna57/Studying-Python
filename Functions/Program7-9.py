def mixedFraction(num,deno=1):
    remain=num%deno
    if remain!=0:
        whole=num//deno
    print(f"{whole}({remain}/{deno})")
numerator=int(input("Enter numerator:"))
denominator=int(input("Enter denominator"))
mixedFraction(numerator,denominator)