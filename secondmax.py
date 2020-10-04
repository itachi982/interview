#!usr/bin/python3
list2 = [79,13,29,7,200] 
list1= [15,23,9]
  
def secondmax(list):

    maximum=max(list[0],list[1])  
    secondmaximum=min(list[0],list[1])
    a=len(list) 
    for i in range(2,a):  
        if list[i]>maximum:  
            secondmaximum=maximum 
            maximum=list[i]  
        elif list[i]>secondmaximum and maximum != list[i]:  
            secondmaximum=list[i] 
        else: 
            if secondmaximum == maximum: 
                secondmaximum = list[i] 
    print("Second highest number is : ",str(secondmaximum)) 

secondmax(list1)
secondmax(list2)
