from functools import wraps


def komandan(func):
    @wraps(func)
    def wrapped(context, message, trigger, args, kwargs):
        nick = message.nick

        if not context.acl.allowed(trigger, message.channel, nick):
            message.reply("Maaf {0}, saya tidak dapat melaksanakan perintah Anda.".format(nick))
            return
        return func(context, message, trigger, args, kwargs)
    return wrapped

