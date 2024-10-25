def time_string(hours, minutes, time_format):
    len_hours = len(str(hours))
    len_minutes = len(str(minutes))
    
   
    if time_format==24:
       new_hours=""
       new_minutes=""
       
       if len_hours == 1:
           new_hours= "0"+ str(hours)

       elif len_hours == 2:
           new_hours = str(hours)

       if len_minutes==1:
           new_minutes= "0"+ str(minutes)
           
       elif len_minutes == 2:
           new_minutes= str(minutes)

       else: print("wrong minutes or hours format")
       
       new_time = new_hours + ":" + new_minutes
    
    elif time_format==12:
        new_hours=""
        new_minutes=""






        

    else: print("wrong time format")

    
    return new_time
     



print(time_string(5, 4 ,24 ))
    
    
   

