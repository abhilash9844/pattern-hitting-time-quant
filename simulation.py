import random
def simulate(pattern, trails):
    def tosses():
        return 'H' if random.random()<0.5 else 'T'
    total=0
    n=len(pattern)

    for i in range(trails):
        lastnvalues = ""
        count=0
        while True:
             lastnvalues+=tosses()
             count+=1
             lastnvalues=lastnvalues[-n:]

             if lastnvalues==pattern:
                 break
        total+=count
    return total/trails
pattern = input("Enter pattern(H/T only,eg:HT,HTHH,etc): ")
trails=int(input("Enter number of trails: "))

result=simulate(pattern,trails)
print(f"\nExpected steps to get'{pattern}':{result}")
    
        
