print "I will find all prime numbers within a range! "
div = 3 #divider should be odd
primelist = []
range1 = input("Beginning of range: ")
range2 = input("End of range: ")
prospect = range1

while prospect <= range2:   #repeat until all numbers in range exauhsted
    if prospect == 2:          #because main code wont find 2
        primelist.append(prospect)
        prospect += 1
    elif prospect == 3:        #because main code wont find 3
        primelist.append(prospect)
        prospect += 2
    elif prospect % 2 == 0:    #check for/ make prospect odd
        prospect += 1
    else:
        while prospect % div != 0:  #prove div doesnt divide evenly
            if div >= (prospect / 2) + 1:   #once half the numbers are checked
                primelist.append(prospect)  #and div still doesnt divide evenly
                div = 3
                prospect += 2               # +2 to skip to next odd number
                continue
            else:
                div += 2                    # +2 to div to keep div odd
        prospect += 2                       # +2 to skip to next odd number
        div = 3
print primelist
