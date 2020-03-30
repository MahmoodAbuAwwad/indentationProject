#reading all lines and fill list
with open('file.txt') as f:
    lines = f.readlines()


#loop to edit every Line in file
i=0
for i in range (len(lines)):


    # if statement for #include
    if(lines[i].__contains__('#include')):
        lines[i] = lines[i].strip()
        if(lines[i].count(" ") == 0 or lines[i].count(" ") > 1):
            lines [i] = lines[i].replace(" ","")
            lines[i] = lines[i][:8] + ' ' + lines[i][8:]


    #for spaces before (;)
    j=0
    for j in range (len( lines[i] ) -1):
        if (lines[i][j] ==';'):
            num = 1
            while(lines[i][j-num] == " "):
                lines[i] = lines[i][:j - num] + lines[i][(j - num + 1):]  #replace space by semicolon
                num+=1
            lines[i] = (lines[i][:j+1] + '\n' + lines[i][j+1:].strip())
        j+=1

######################################

    j=0

    while j < len(lines[i]):
        flag = 0
        if(lines[i][j]=='+' or lines[i][j]=='%' or lines[i][j]=='-' or lines[i][j]=='*' or lines[i][j]=='/' or lines[i][j]=='='):
             num=1
             while(lines[i][j-num] == " "):
                 lines[i] = lines[i][:j - num] + lines[i][(j - num +1):]    #replace space by expression
                 num+=1
                 flag = 1
             num = 1
             while(lines[i][j+num] == " "):

                 # 3addel hay  ************
                 lines[i] = lines[i][:j + num] + lines[i][(j + num +1):]    #replace space by expression
                 num+=1
                 flag = 1
             if(flag == 1):
                 j=0
                 continue
             lines[i] = lines[i][:j] +' '+ lines[i][j:]+' '
        j+=1
   ############################################


   #for sucessive  paranthese (( ))
    j=0
    for j in range (len( lines[i] ) -1):
        if ( lines[i][j] =='('  or lines[i][j] ==')'):
            num = 1
            while(lines[i][j-num] == " "):
                lines[i] = lines[i][:j - num] + lines[i][(j - num + 1):]    #replace space by paranthes to remove space
                num+=1
        j+=1



    # 1 blank character after a comma, a full stop, a closing parenthesis.
    j=0
    for j in range (len( lines[i] ) -1):
        if ( lines[i][j] ==','  or (lines[i][j] ==')'and lines[i][j-1]!=')'and lines[i][j+1]!=')') or lines[i][j] =='.'):
                 lines[i] = lines[i][:j+1] + ' ' + lines[i][j+1:]
        j+=1

##############################################################3
    #1blank before (
    j=0
    while j < len(lines[i]):
        #print(lines[i][j])
        if ( lines[i][j] =='(' and lines[i][j-1]!='('):
                 lines[i] = lines[i][:j]+' '+ lines[i][j:]
                 j+=1
        j+=1

#################################################################
  #Remove all blank spaces between operators that contain more than 1 character
    list1=['/','*','-','+','!','&','|','>','<','=']
    j=0
    list2=[]
    index2=0
    for j in range (len( lines[i] ) -1):
        flag=0
        if ( lines[i][j] in list1):
            num=1
            index1=j
            while(lines[i][j+num]==' '):
                if(lines[i][j+num+1] in list1):
                    flag=1
                    index2=j+num+1
                    break
                num+=1
            lines[i]=lines[i][:index1+1]+lines[i][index2:]
            break
        j+=1

    print(lines[i])
    i=i+1
