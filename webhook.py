import requests
import json


class Webhook:
    def send_message(self, **kwarg):
        url = "https://discordapp.com/api/webhooks/434019939096068096/eNAQClgsy55tU38fgDbe0OIpMXzz8Ty6Fni4lUyHNG5RgCOssjItiv2yLxyTWTCdfRIS"

        if("username" in kwarg):
            username = kwarg.pop("username")
        else:
            username = "Stats Maid"

        if("avatar_url" in kwarg):
            avatar_url = kwarg["avatar_url"]
        else:
            avatar_url = "https://img.crypko.ai/daisy/d884e6585012ba9cbf2397af28bde2f2644debee_lg.jpg"

        if("content" in kwarg):
            content = kwarg["content"]
        else:
            content = "Today's Stats is here, Master. I hope tomorrow is also a nice day."

        if("embeds" in kwarg):
            embeds = kwarg["embeds"]
        else:
            embeds = ""

        payload = {
            "username": username,
            "avatar_url": avatar_url,
            "content": content,
            "embeds": embeds
        }

        headers = {
            "content-type": "application/json"
        }

        response = requests.post(
            url=url,
            data=json.dumps(payload),
            headers=headers
        )

        if(response.status_code == 204):
            return True
        else:
            return False
