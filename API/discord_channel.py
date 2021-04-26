from . import discord_api

import json

CHANNELS = discord_api.API + "/channels"
CHANNELS_ = CHANNELS + "/{}"

CHANNELS_PINS           = CHANNELS_ + "/pins"
CHANNELS_TRIGGER_TYPING = CHANNELS_ + "/typing"
CHANNELS_INVITES        = CHANNELS_ + "/invites"
CHANNELS_MESSAGES       = CHANNELS_ + "/messages"
CHANNELS_FOLLOWERS      = CHANNELS_ + "/followers"
CHANNELS_DM             = CHANNELS_ + "/recipients/{}"
CHANNELS_PERMISSION     = CHANNELS_ + "/permissions/{}"

CHANNELS_MESSAGE     = CHANNELS_MESSAGES + "/{}"
CHANNELS_BULK_DELETE = CHANNELS_MESSAGES + "/bulk-delete"

CHANNELS_MESSAGE_CROSSPOST  = CHANNELS_MESSAGE + "/crosspost"

CHANNELS_MESSAGE_EMOJIS     = CHANNELS_MESSAGE + "/reactions"
CHANNELS_MESSAGE_EMOJI      = CHANNELS_MESSAGE_EMOJIS + "/{}"
CHANNELS_MESSAGE_EMOJI_FROM = CHANNELS_MESSAGE_EMOJI + "/{}"


CHANNELS_PIN_MESSAGES = CHANNELS_PINS + "/{}"

class discord_channel_(discord_api.DiscordObject):
    
    def __init__(self, channel):
        if 'id' not in channel:
            raise Exception('Invalid channel')

        self.channel = channel
        
    def __str__(self):
        return json.dumps(self.channel)
    
    def query(self, user, url, *vargs):
        return super().query(user, url, self.channel['id'], vargs)

    def messages(self, user):
        response = self.query(user, CHANNELS_MESSAGES)

        if response.status_code != 200:
            return []
        
        return [discord_message_(message) for message in response.json()]

class discord_message_(discord_api.DiscordObject):

    def __init__(self, message):
    
        if 'id' not in message:
            raise Exception('Invalid message')

        self.message = message
        
    def __str__(self):
        return json.dumps(self.message)

    def query(self, user, url, *vargs):
        return super().query(user, url, self.message['id'], vargs)




