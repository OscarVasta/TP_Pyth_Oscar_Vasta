from control_open import control_open
processed_file  =  False
while  not  processed_file :
    filename  =  input ( "Enter file:" )
    file_control  =  control_open ( file_name )
    if  len ( file_control ) ==  0 :
        # do something
        processed_file  =  True
    else:
        print ( file_control )

print ( "End of program." )
