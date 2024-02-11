def counting_loop(n):
    #returns n number to inputparsing
    
    while True:
        try:
            zahl = int(input())
            if zahl == n:
                print("richtig")
                n = n+1 
            else:
                print("Restart")
                n=0
                #bot posts a sad gif
        except ValueError:
            print("Nur nummern ")
        


counting_loop(1)
