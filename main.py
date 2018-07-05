import json
import webhook
import twitter
import mastodon
import github
import steam
import osu


def pjson(dic):
    print(json.dumps(dic, ensure_ascii=False, indent=4, sort_keys=True))


twitter = twitter.Twitter().get(screen_name="eai04191")

twitter_embed = {
    "author": {
        "name": "Twitter",
        "url": "https://twitter.com/%s" % twitter["screen_name"],
        "icon_url": "https://github.com/twitter.png"
    },
    "color": 1942002,
    "fields": [
        {
            "name": ":speech_balloon: Tweets",
            "value": "**%s** (%d)" % ("{:,d}".format(twitter["tweets"]), 0),
            "inline": True
        },
        {
            "name": ":two_hearts: Likes",
            "value": "**%s** (%d)" % ("{:,d}".format(twitter["likes"]), 0),
            "inline": True
        },
        {
            "name": ":busts_in_silhouette: Followers",
            "value": "**%s** (%d)" % ("{:,d}".format(twitter["followers"]), 0),
            "inline": True
        }
    ]
}

mastodon = mastodon.Mastodon().get(instance="mstdn.io", username="Eai")

mastodon_embed = {
    "author": {
        "name": "Mastodon",
                "url": "https://%s/@%s" % (mastodon["instance"], mastodon["username"]),
                "icon_url": "https://github.com/tootsuite.png"
    },
    "color": 2632759,
    "fields": [
        {
            "name": ":speech_balloon: Toots",
            "value": "**%d** (%d)" % (mastodon["toots"], 0),
            "inline": True
        },
        {
            "name": ":bust_in_silhouette: Following",
            "value": "**%d** (%d)" % (mastodon["following"], 0),
            "inline": True
        },
        {
            "name": ":busts_in_silhouette: Followers",
            "value": "**%d** (%d)" % (mastodon["followers"], 0),
            "inline": True
        }
    ]
}

github = github.Github().get(username="eai04191")

github_embed = {
    "author": {
        "name": "GitHub",
        "url": "https://github.com/%s" % github["username"],
        "icon_url": "https://github.com/github.png"
    },
    "color": 819,
    "fields": [
        {
            "name": ":pencil: Contributions in Last Year",
            "value": "**%s** (%d)" % ("{:,d}".format(github["contributions_in_last_year"]), 0),
            "inline": True
        },
        {
            "name": ":star: Stars",
            "value": "**%s** (%d)" % ("{:,d}".format(github["stars"]), 0),
            "inline": True
        }
    ]
}

steam = steam.Steam().get(id=76561198040100825)

steam_embed = {
    "author": {
        "name": "Steam",
        "url": "http://steamcommunity.com/profiles/%d" % steam["id"],
        "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Steam_icon_logo.svg/240px-Steam_icon_logo.svg.png"
    },
    "color": 1514017,
    "fields": [
        {
            "name": ":muscle: Level",
            "value": "Level **%s** (%d)\r**%s** XP (%d)" % (
                "{:,d}".format(steam["level"]),
                0,
                "{:,d}".format(steam["xp"]),
                0
            ),
            "inline": True
        },
        {
            "name": ":video_game: Owned Games",
            "value": "**%s** (%d)" % ("{:,d}".format(steam["games"]), 0),
            "inline": True
        },
        {
            "name": ":clock4: Recent Play Time",
            "value": "**%s hrs** (%d)" % ("{0:.1f}".format(steam["recent_playtime"]), 0),
            "inline": True
        }
    ]
}

osu = osu.Osu().get(id=1584443)

osu_embed = {
    "author": {
        "name": "osu!",
        "url": "https://osu.ppy.sh/users/%d" % osu["id"],
        "icon_url": "https://s.ppy.sh/apple-touch-icon.png"
    },
    "color": 13390472,
    "fields": [
        {
            "name": ":trophy: pp",
            "value": "**%s** (%d)" % ("{0:.2f}".format(osu["statistics"]["pp"]), 0),
            "inline": True
        },
        {
            "name": ":chart_with_upwards_trend: Rank",
            "value": "**#%s** (%d)\r**#%s** (%d) in :flag_%s:" % (
                    "{:,d}".format(osu["statistics"]["rank"]["global"]),
                    0,
                    "{:,d}".format(osu["statistics"]["rank"]["country"]),
                    0,
                    osu["country"].lower()
            ),
            "inline": True
        },
        {
            "name": ":clock4: Play Time",
            "value": "**%s** (%d)" % (osu["statistics"]["play_time_str"], 0),
            "inline": True
        }
    ]
}

webhook = webhook.Webhook()

embeds = []
embeds.append(twitter_embed)
embeds.append(mastodon_embed)
embeds.append(github_embed)
embeds.append(steam_embed)
embeds.append(osu_embed)


success = webhook.send_message(
    embeds=embeds
)

if(success):
    print("Success.")
else:
    print("Webhook Send Error. :(")
