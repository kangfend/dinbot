from django.core.management.base import BaseCommand
from pyaib.ircbot import IrcBot


class Command(BaseCommand):
    help = 'Run Django Indonesia Bot'

    def handle(self, *args, **options):
        bot = IrcBot('config.bot')
        bot.run()

