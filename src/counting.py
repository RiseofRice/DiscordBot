def counting_loop(n):
    
    
    while True:
        try:
            zahl = int(input("Enter a number: "))
            if zahl == n:
                print("richtig")
                n = n+1 
            else:
                print("Count has been reset. Please start from 1.")
                n=0
                
        except ValueError:
            print("Please enter numbers only. Resetting the game. Please start from 1 again :) ")
            n=0 
        


counting_loop(1)
