def  even_Odd():
    x = int (input("Enter X value: "))
    list_num =[]
    for i in range(x):
        list_num.append(int(input()))

    for i in list_num:
        if i% 2==0 :
            print(i , "is even")
        else :
            print(i,'is odd')        
even_Odd()
  
