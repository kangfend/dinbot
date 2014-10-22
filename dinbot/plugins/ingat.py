from bot.models import Remember
from dinbot.utils.decorators import komandan
from pyaib.plugins import keyword


@komandan
@keyword('ingat')
def ingat(context, message, trigger, args, kwargs):
    list_penghubung = ['itu', 'adalah']
    if len(args) > 2 and args[1] in list_penghubung:
        nick = message.nick
        kata = args[0]
        penghubung = args[1]
        arti = ' '.join(args[2:])
        channel = message.channel
        ingat = Remember.objects.filter(word=kata).first()
        if not ingat:
            Remember.objects.create(
                word=kata, nick=nick, penghubung=penghubung,
                content=arti, channel=channel, type=Remember.TYPE.arti
            )
            pesan = "Terima kasih {0}, sekarang saya tahu apa itu {1}"\
                .format(nick, kata)
        else:
            penghubung = ingat.penghubung
            content = ingat.content
            if content == arti:
                pesan = "{0}: Saya sudah tau itu sebelumnya".format(nick)
            else:
                pesan = "Maaf {0}, yang saya ingat {1} {2} {3}"\
                    .format(nick, kata, penghubung, arti)
        message.reply(pesan)


@keyword('apa', 'siapa')
@keyword.sub('itu')
def apa_itu(context, message, trigger, args, kwargs):
    if len(args) == 1:
        kata = args[0][:-1:] if args[0][-1:] in ['?', '!', '.', ','] else args[0]
        nick = message.nick
        data = Remember.objects.filter(word=kata).first()
        if not data:
            pesan = "Maaf {0}, aku gak tau apa itu {1}"\
                .format(nick, kata)
        else:
            arti = data.content
            penghubung = data.penghubung
            pesan = "{0}: {1} {2} {3}".format(nick, kata, penghubung, arti)
        message.reply(pesan)


@komandan
@keyword('lupakan')
def lupakan(context, message, trigger, args, kwargs):
    if len(args) == 1:
        kata = args[0]
        nick = message.nick
        data = Remember.objects.filter(word=kata).first()
        if data:
            data.delete()
            pesan = "ok"
        else:
            pesan = "Maaf {0}, saya tidak pernah tau apa itu {1}"\
                .format(nick, kata)
        message.reply(pesan)


@keyword('kasih', 'beri')
@keyword.sub('tau', 'tahu')
def kasih_tau(context, message, trigger, args, kwargs):
    if len(args) == 4:
        nick_tujuan = args[0]
        kata = args[3]
        nick = message.nick
        data = Remember.objects.filter(word=kata).first()
        if not data:
            pesan = "Maaf {0}, aku gak tau apa itu {1}"\
                .format(nick, kata)
        else:
            arti = data.content
            penghubung = data.penghubung
            pesan = "{0}: {1} {2} {3}".format(nick_tujuan, kata, penghubung, arti)

        message.reply(pesan)
