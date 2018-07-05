import requests
import json
import lxml.html


class Twitter:
    def get(self, screen_name):
        url = "https://twitter.com/%s" % screen_name
        response = requests.get(url)
        if(response.status_code != 200):
            return False
        dom = lxml.html.fromstring(response.text)
        json_data = dom.get_element_by_id("init-data").attrib["value"]
        dic = json.loads(json_data)

        return {
            "id": int(dic["profile_user"]["id"]),
            "screen_name": dic["profile_user"]["screen_name"],
            "tweets": int(dic["profile_user"]["statuses_count"]),
            "likes": int(dic["profile_user"]["favourites_count"]),
            "following": int(dic["profile_user"]["friends_count"]),
            "followers": int(dic["profile_user"]["followers_count"]),
            "listed": int(dic["profile_user"]["listed_count"])
        }
