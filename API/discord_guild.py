from . import discord_api
from . import discord_channel

import json

GUILDS_ = discord_api.API + '/guilds/{}'

GUILDS_CHANNELS = GUILDS_ + '/channels'

GUILDS_PREVIEW = GUILDS_ + '/preview'

GUILDS_MEMBERS = GUILDS_ + '/members'
GUILDS_MEMBER  = GUILDS_MEMBERS + '/{}'

GUILDS_BANS = GUILDS_ + '/bans'
GUILDS_BAN  = GUILDS_BANS + '/{}'

GUILDS_ROLES = GUILDS_ + '/roles'
GUILDS_ROLE  = GUILDS_ROLES + '/{}'

GUILDS_PRUNE_COUNT = GUILDS_ + '/prune'
GUILDS_VOICE_REGIONS = GUILDS_ + '/regions'
GUILDS_INVITES = GUILDS_ + '/invites'
GUILDS_INTEGRATIONS = GUILDS_ + '/integrations'
GUILDS_WIDGET = GUILDS_ + '/widget'
GUILDS_VANITY = GUILDS_ + '/vanity-url'

GUILDS_WIDGET_IMG = GUILDS_WIDGET + ".png"

class discord_guild_(discord_api.DiscordObject):
    
    def __init__(self, guild):
        if 'id' not in guild:
            raise Exception('Invalid guild.')
        
        self.guild = guild

    def __str__(self):
        return json.dumps(self.guild)

    def query(self, user, url, *vargs):
        return super().query(user, url, self.guild['id'], vargs)

    def channels(self, user):
        response = self.query(user, GUILDS_CHANNELS).json()
        return [discord_channel.discord_channel_(channel) for channel in response]






