import time
from discord_webhook import DiscordWebhook
from screen_search import *


searchIMG = Search("blessing.png")
webhook_urls = ['https://discordapp.com/api/webhooks/xxx']
bless_msgs = ["Toad has been given a blessing, increasing experience by 1.5x!",
"Toad's blessing has 45 minutes remaining!",
"Toad's blessing has 30 minutes remaining!",
"Toad's blessing has 15 minutes remaining!",
"Toad's blessing has 5 minutes remaining!",
"Toad's blessing has ended!"]

def blessing():
    for i in range(6):
        webhook = DiscordWebhook(url=webhook_urls, content=bless_msgs[i])
        webhook.execute()
        print(bless_msgs[i])
        if (i < 3):
            print('Delay 15min')
            time.sleep(900)
        elif (i < 4):
            print("Delay 10min")
            time.sleep(600)
        elif (i == 4):
            print("Delay 5min")
            time.sleep(300)

while True:
    pos = searchIMG.imagesearch()
    time.sleep(30)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        blessing()
    else:
        print("blessing not found")
        





