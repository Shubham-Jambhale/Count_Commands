def commands_count (c):
    #maintains the count of commands
    ls_count = 0
    cp_count = 0
    mv_count = 0
    #iterating on the incoming array and increasing the count of found elemets.
    for i in range(0,len(c)):
        if c[i] == "ls":
            ls_count += 1
        elif c[i] == "cp":
            cp_count +=1   
        elif c[i] == "mv":
            mv_count += 1
        else:
            #checking if not command and checking which command count to increase.
             if c[i].lstrip("!").isdigit():
                    abc = int(c[i].lstrip("!"))
                    y = abc - 1
                    a = c[y]
                    j = 0
                    while  j < i:
                        if a == "ls":
                            ls_count += 1
                            break
                        elif a == "cp":
                            cp_count +=1
                            break;  
                        elif a == "mv":
                            mv_count += 1
                            break; 
                        else :
                            if a.lstrip("!").isdigit():
                                abc = int(a.lstrip("!"))
                                x = abc - 1
                                a = c[x]
                                
                        j = j+1
    outputlist=[]
    outputlist.append(cp_count)
    outputlist.append(ls_count)
    outputlist.append(mv_count)
        
    return outputlist
