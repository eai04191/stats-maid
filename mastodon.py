import requests
import json
import lxml.html


class Mastodon:
    # 10Kなどでしか取れない
    def get(self, instance, username):
        url = "https://%s/@%s" % (instance, username)
        response = requests.get(url)
        if(response.status_code != 200):
            return False
        dom = lxml.html.fromstring(response.text)

        counters = []
        for counter in dom.xpath("//*[@class=\"counter-number\"]"):
            text = counter.text.strip()
            text = text.replace("K", "000")
            text = text.replace(",", "")
            counters.append(text)

        return {
            "instance": instance,
            "username": username,
            "toots": int(counters[0]),
            "following": int(counters[1]),
            "followers": int(counters[2]),
        }
