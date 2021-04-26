import sys, getopt

argv = sys.argv[1:]

# Initialize command line options
token = query = include = exclude = None

try:
    arguments, options = getopt.getopt(argv, "t:q:i:e:c")
except getopt.GetoptError:
    print("crawl.py -t <token> -q <params>")
    sys.exit(2)   

for arg, val in arguments:
    if arg in ('-t'): #Token
        token = val
        #print(f"token={token}")
            
    elif arg in ('-q'): #Query
        query = val
        #print(f"q={q}")
            
    elif arg in ('-i'): #Include guilds/channels
        include = val
        #print(f"i={i}")
            
    elif arg in ('-e'): #Exclude guilds/channels
        exclude = val
        #print(f"e={e}")
        
    elif arg in ('-c'): #Token from cred.py
        import cred
        token = cred.token   
        #print(f"cred={token}")
            
if not token:
    print("You need to provide a token")
    sys.exit(2)
        
if not query:
    # A query should be in the form term;arg=val,...;output,...+...
    # where term specifies type of data, arg=val filters the data, and output are the data fields to record
    #
    # A term will do a 'coarse filter' of the type of data, while arg=val filters it based on the data
    # There are predefined terms that you can use to build your query.
    #
    # TERMS:
    # I searches for invites
    #
    # Output is a list of fields to output from the filtered data objects
    
    print("You need to provide a query")
    sys.exit(2)

import re

query = query.split("+")

def tuplify(package):
    package = package.split(";")
    
    term = package[0]
    args = [] if len(package) < 2 else package[1].split(",")
    out  = [] if len(package) < 3 else package[2].split(",")
    
    result = []
    
    for pair in args:
        pair = pair.split("=")
        if len(pair) == 2:
            result.append((pair[0], pair[1]))
        
    return (term, result, out)

query = [tuplify(package) for package in query]

import grep

grep.search(token, query)






