n = int( input ("Wich number will be end of Fibonnachi: "))
fibonacci = [0,1] 
for item in fibonacci:
    if fibonacci[-1] + fibonacci[-2]  < n :
        fibonacci.append(fibonacci[-1] + fibonacci[-2] )
print (fibonacci)