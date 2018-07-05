import requests
import json
import env

class Webhook:
    def send_message(self, **kwarg):
        url = env.discord_webhook_url

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
