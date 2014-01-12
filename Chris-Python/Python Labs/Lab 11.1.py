def startsWith(x,z):
    if x.find(z)==0:
        return True
    else:
        return False
print startsWith( "radar installation", "rad" )
print startsWith( "radar installation", "installation" )
print startsWith( "radar installation", "" )
print startsWith( "", "a" )
