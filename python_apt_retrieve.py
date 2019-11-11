#!/usr/bin/env python
from   urllib2  import urlopen,unquote
from   os       import stat
from   sys      import argv
import hashlib

argsz = len(argv)
if int(argsz) > 1:
   DEBLIST = argv[1]
else: 
   DEBLIST = 'deblist.txt'

with open(DEBLIST) as f:
    deblist = f.read().splitlines()

for line in deblist:
    spl = line.split()
    uri   = spl[0].split("'")[1]

    fillist = uri.split("/")
    last    = len(fillist)
    last    = last - 1
    filn    = fillist[last]
    # filn  = unquote(spl[1])

    filz    = spl[2]
    md5     = spl[3].split('MD5Sum:')[1]

    # print 'Getting          :', uri
    # print 'Expected filename:', filn
    # print 'Size             :', filz
    # print 'MD5              :', md5
    
    binr = urlopen(uri)
    fp  = open(filn, 'wb')     
    for line in binr:          
        fp.write(line)        
    fp.close() 
    
    fils = stat(filn).st_size
    if str(fils) != str(filz):
       print "ERROR: Bad file size for ", filn
 
    md5_returned = hashlib.md5(open(filn).read()).hexdigest()
    if md5 != md5_returned:
        print "MD5 verification failed for: ", filn

print "Finished."
