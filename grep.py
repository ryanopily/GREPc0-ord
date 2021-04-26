import re, requests   
from API import discord_api, discord_user, discord_guild, discord_channel

INVITE = "https\://discord\.gg/[a-zA-Z0-9]{8}"

def search(t, q, i=None, e=None):
    user = discord_user.discord_user_(token=t)

    if i:
        print("Include scan")
        
    elif e:
        print("Exclude scan")
        
    else:
        print("General scan")
        
        def scan_channel(channel):
            for message in channel.messages(user):
                options = get_pair(q, 'I')
                
                if options:
                    result = re.search(INVITE, message.__str__())
                            
                    if result:
                        print(f"match={result.group(0)}")
                        
                        out = options[2]
                        if len(out) > 0:
                            print("out:")
                            output(out, message.message)
                        print("\n")
                        
        print("Scanning user channels:\n")
        for channel in user.channels():
            scan_channel(channel)
            
        print("Scanning guild channels:\n")
        for guild in user.guilds():
            for channel in guild.channels(user):
                scan_channel(channel)
                        
        
            
def output(o, obj):
    for field in o:
        if field in obj:
            print(f"  {obj[field]}")
            
def get_pair(q, key):
    for arr in q:
        if key in arr:
            return arr
            
    return None