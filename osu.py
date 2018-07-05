import requests
import json
import lxml.html
import datetime


class Osu:
    def get(self, id):
        url = "https://osu.ppy.sh/users/%d" % id
        response = requests.get(url)
        if(response.status_code != 200):
            return False
        dom = lxml.html.fromstring(response.text)
        json_data = dom.xpath("//*[@id=\"json-user\"]")[0].text_content()
        data = json.loads(json_data)

        play_time = int(data['statistics']['play_time'])
        dt = datetime.datetime.fromtimestamp(play_time)
        hour = int(play_time/60/60)
        min = dt.minute
        sec = dt.second
        play_time_str = "%s hrs %d mins %d secs" % (
            "{:,d}".format(hour),
            min,
            sec
        )

        return {
            "id": int(id),
            "country": data['country']['code'],
            "username": data['username'],
            "statistics": {
                "grade_counts": {
                    "a": int(data['statistics']['grade_counts']['a']),
                    "s": int(data['statistics']['grade_counts']['s']),
                    "sh": int(data['statistics']['grade_counts']['sh']),
                    "ss": int(data['statistics']['grade_counts']['ss']),
                    "ssh": int(data['statistics']['grade_counts']['ssh'])
                },
                "hit_accuracy": float(data['statistics']['hit_accuracy']),
                "level": {
                    "current": int(data['statistics']['level']['current']),
                    "progress": int(data['statistics']['level']['progress'])
                },
                "maximum_combo": int(data['statistics']['maximum_combo']),
                "play_count": int(data['statistics']['play_count']),
                "play_time": int(data['statistics']['play_time']),  # Sec
                "play_time_str": play_time_str,
                "pp": float(data['statistics']['pp']),
                "pp_rank": int(data['statistics']['pp_rank']),
                "rank": {
                    "country": int(data['statistics']['rank']['country']),
                    "global": int(data['statistics']['rank']['global'])
                },
                "ranked_score": int(data['statistics']['ranked_score']),
                "replays_watched_by_others": int(data['statistics']['replays_watched_by_others']),
                "scoreRanks": {
                    "A": int(data['statistics']['scoreRanks']['A']),
                    "S": int(data['statistics']['scoreRanks']['S']),
                    "SH": int(data['statistics']['scoreRanks']['SH']),
                    "X": int(data['statistics']['scoreRanks']['X']),
                    "XH": int(data['statistics']['scoreRanks']['XH'])
                },
                "total_hits": int(data['statistics']['total_hits']),
                "total_score": int(data['statistics']['total_score'])
            }
        }
