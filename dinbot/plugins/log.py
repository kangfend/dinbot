from django.utils import timezone
from bot.models import History
from pyaib.plugins import observe


@observe('IRC_MSG_PRIVMSG')
def message(irc, message):
    data = {
        'nick': message.nick,
        'channel': message.channel,
        'content': message.message,
        'created': timezone.now(),
    }
    History.objects.create(**data)

