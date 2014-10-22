import wolframalpha
from dinbot.utils.translate import translate
from pyaib.plugins import keyword


APP_ID = 'U83E3J-U6P7EYV8WG'


@keyword('tanya')
def tanya(context, message, trigger, args, kwargs):
    if len(args) > 0:
        client = wolframalpha.Client(APP_ID)
        pertanyaan = translate(' '.join(args), 'id', 'en')
        hasil = client.query(pertanyaan)
        if len(hasil.pods) > 0:
            pod = hasil.pods[1]
            if pod.text:
                pesan = pod.text
            else:
                pesan = "Maaf {0} saya tidak tahu.".format(message.nick)
            message.reply(translate(pesan, 'en', 'id'))
        else:
            message.reply("Maaf {0} saya tidak tahu.".format(message.nick))
