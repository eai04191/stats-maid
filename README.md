Stats Maid
===

She loves stats, and you too.


## Usage

`Now Printing.`


## Supported Services and Variables

### Twitter

* `int` followers
* `int` following
* `int` id
* `int` likes
* `int` listed
* `str` screen_name
* `int` tweets

### Mastodon (Deprecated)

Scraping can not acquire detailed numbers. (1000 or more will be displayed as 1K)

*  `int` followers
*  `int` following
*  `str` instance
*  `int` toots
*  `str` username

### GitHub

*  `int` contributions_in_last_year
*  `int` followers
*  `int` following
*  `int` public_repositories
*  `int` stars
*  `str` username

### Steam

*  `int` artwork
*  `int` badges
*  `int` comments
*  `int` friends
*  `int` games
*  `int` groups
*  `int` guides
*  `int` id
*  `int` level
*  `str` name
*  `float` recent_playtime
*  `int` reviews
*  `int` screenshots
*  `int` workshop_items
*  `int` xp

### osu!

*  `str` country
*  `int` id
    * statistics
        *  grade_counts
            * `int` a
            * `int` s
            * `int` sh
            * `int` ss
            * `int` ssh
    * `float` hit_accuracy
    * level
        * `int` current
        * `int` progress
    * `int` maximum_combo
    * `int` play_count
    * `int` play_time
    * `str` play_time_str
    * `float` pp
    * `int` pp_rank
    * rank
        * `int` country
        * `int` global
    * `int` ranked_score
    * `int` replays_watched_by_others
    * scoreRanks
        * `int` A
        * `int` S
        * `int` SH
        * `int` X
        * `int` XH
    * `int` total_hits
    * `int` total_score
*  `int` username


## License

This project is licensed under the MIT License.