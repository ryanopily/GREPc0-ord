from . import discord_api, discord_guild, discord_channel

USERS_  = discord_api.API + "/users/{}"

USERS_GUILDS = USERS_ + "/guilds"
USERS_GUILDS_DELETE = USERS_GUILDS + "/{}"

USERS_DMS = USERS_ + "/channels"
USERS_CONNECTIONS = USERS_ + "/connections"

class discord_user_(discord_api.DiscordObject):
    
    def __init__(self, **kwargs):
        if 'token' not in kwargs:
            raise Exception('Token not provided')

        self.token = {'Authorization': kwargs['token']}
        
        if not self.valid_session():           
            raise Exception('Invalid token provided')

    def __str__(self):
        return info().json()
        
    def valid_session(self):
        if self.query(USERS_).status_code == 200:
            return True
        else:
            return False

    def query(self, url, *vargs):
        return super().query(self, url, "@me", vargs)

    def info(self):
        return self.query(USERS_).json()

    def channels(self):
        response = self.query(USERS_DMS)
        return [discord_channel.discord_channel_(channel) for channel in response.json()]
    
    def guilds(self):
        response = self.query(USERS_GUILDS)
        return [discord_guild.discord_guild_(guild) for guild in response.json()]
    
