import  os

directory  =  os . path . dirname ( __file__ )

def  control_open ( file ):
    try:
        filename  =  os . path . join ( directory , file )
        f  =  open ( filename , 'r' )
    except FileNotFoundError as err:
        return  "FileNotFoundError: {}" . format ( filename )
    except IOError as err:
        return '=======',"IO error: {}".format(err),'======='
    f.close()
    return ""
