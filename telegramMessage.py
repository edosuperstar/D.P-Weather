import pzgram
import request
import urllib

bot = pzgram.Bot("883446648:AAHGWLcnWooHtKjxk43isvh_2Y3k8kGAz6o")


def main():
    button1 = pzgram.create_button("Temperatura", data="temperatura")
    button2 = pzgram.create_button("Pressione", data="pressione")

    k = [[button1, button2]]
    keyboard = pzgram.create_inline(k)

    pzgram.Chat(bot, 693507806).send("Seleziona un dato da controllare: ", reply_markup=keyboard)


def temperatura2():
    pzgram.Chat(bot, 693507806).send("temperatura")


def pressione2():
    pzgram.Chat(bot, 693507806).send("pressione")


bot.set_query({"temperatura": temperatura2, "pressione": pressione2})
bot.set_commands({"stats": main})
bot.run()