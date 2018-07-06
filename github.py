import requests
import json
import lxml.html
import re


class Github:
    def get(self, username):
        url = "https://github.com/%s" % username
        response = requests.get(url)
        if(response.status_code != 200):
            return False
        dom = lxml.html.fromstring(response.text)

        counters = []
        for counter in dom.xpath("//*[@class=\"Counter\"]"):
            text = counter.text.strip()
            text = text.replace(",", "")
            counters.append(text)

        contributions_in_last_year = dom.xpath(
            "//*[@class=\"js-contribution-graph\"]/h2")[0].text.strip()
        contributions_in_last_year = re.search(
            "(^\\d+(\\.\\d|))", contributions_in_last_year).group(0)

        return {
            "username": username,
            "public_repositories": int(counters[0]),
            "stars": int(counters[1]),
            "followers": int(counters[2]),
            "following": int(counters[3]),
            "contributions_in_last_year": int(contributions_in_last_year)
        }
