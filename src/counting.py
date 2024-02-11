def counting(n):
    #returns n number to inputparsing
    
    while True:
        n+=1
        inputparsing(n)
   
   
   
def inputparsing(n):
    # Compares input with returnvalue
    if n <= 1:
        zahl=int(input("fang an zu zählen:"))
    else:
        zahl=int(input("zähl weiter: "))
    if zahl == n:
        right(zahl)
    else:
        Wrong()

def Wrong():
    print("Restart")
    # Bot postet ein sad gif 
    counting(0)

def right(zahl):
    counting(zahl)

counting(0)