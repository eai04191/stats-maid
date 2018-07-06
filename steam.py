import requests
import json
import lxml.html
import re


class Steam:

    def get(self, id):
        url = "https://steamcommunity.com/profiles/%d?l=english" % id
        response = requests.get(url)
        if(response.status_code != 200):
            return False
        dom = lxml.html.fromstring(response.text)

        name = dom.xpath("//*[@class=\"actual_persona_name\"]")[0].text

        level = dom.xpath("//*[@class=\"friendPlayerLevelNum\"]")[0].text

        def get_xp(id):
            url = "https://steamcommunity.com/profiles/%d/badges/?l=english" % id
            response = requests.get(url)
            if(response.status_code != 200):
                return False
            dom = lxml.html.fromstring(response.text)

            xp = dom.xpath("//*[@class=\"profile_xp_block_xp\"]")[0].text
            xp = xp.replace("XP", "")
            xp = xp.replace(",", "")
            return int(xp)

        xp = get_xp(id)

        recentplaytime = dom.xpath(
            "//*[@class=\"recentgame_quicklinks recentgame_recentplaytime\"]/h2")[0].text
        recentplaytime = re.search("(^\\d+(\\.\\d|))", recentplaytime).group(0)

        comments = dom.get_element_by_id(
            "commentthread_Profile_%d_0_totalcount" % id).text
        comments = comments.replace(",", "")

        counters = []
        for counter in dom.xpath("//*[@class=\"profile_count_link_total\"]"):
            text = counter.text.strip()
            text = text.replace(",", "")
            counters.append(text)

        return {
            "id": id,
            "name": name,
            "level": int(level),
            "xp": xp,
            "badges": int(counters[0]),
            "games": int(counters[1]),
            # "inventory": int(counters[2]), # Nothing to show.
            "screenshots": int(counters[3]),
            # "videos": , # Will be shown after login.
            "workshop_items": int(counters[4]),
            "reviews": int(counters[5]),
            "guides": int(counters[6]),
            "artwork": int(counters[7]),
            "groups": int(counters[8]),
            "friends": int(counters[9]),
            "recent_playtime": float(recentplaytime),
            "comments": int(comments)
        }
