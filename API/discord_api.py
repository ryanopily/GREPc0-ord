import requests

API = "https://discord.com/api/v8"

CDN = "https://cdn.discordapp.com"
CDN_GUILD_ICON = CDN + "/icons/{}/{}"

class DiscordObject:
    
    def query(self, user, url, *vargs):
        for arg in vargs:
            url = url.format(arg)
            
        return requests.get(url, headers=user.token)
