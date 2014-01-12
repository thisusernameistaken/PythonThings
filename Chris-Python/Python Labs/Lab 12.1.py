def writeDate(year, month,day,hours,minutes,seconds):
    out=str(month)+'/'
    if day>0:
        out+=str(day)+'/'
    out+=str(year)
    if hours>=0:
        out+=' '+str(hours)+':'
        minutes%=60
        if minutes<10:
            out+='0'
        out+=str(minutes)
    if seconds>=0:
        out+='.'
        seconds%=60
        if seconds<10:
            out+='0'
        out+=str(seconds)
    return out
print writeDate( 2008, 3, 26, 9, 12, 45 )
print writeDate( 2010, 11, -1, 0, 0, 17 )
print writeDate( 2005, 6, 1, 16, 3, -1 )	
