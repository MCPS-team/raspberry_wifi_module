from wifi import Cell, Scheme

def wifiscan():

    allSSID = Cell.all('wlan0')
    print (allSSID) # prints all available WIFI SSIDs
    myssid= 'Cell(ssid=davide-ThinkPad)' # vivekHome is my wifi name
    
    print(allSSID[myssid])

    for i in range(len(allSSID)):
        if str(allSSID [i]) == myssid:
            a = i
            myssidA = allSSID [a]
            print (b)
            break
        else:
            print ("getout")

    # Creating Scheme with my SSID.
    myssid= Scheme.for_cell('wlan0', 'accespoint', myssidA, '3ze7GvdI') # vive1234 is the password to my wifi myssidA is the wifi name 

    print (myssid)
    myssid.save()
    myssid.activate()

wifiscan()   
