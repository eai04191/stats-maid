Stats Maid
===

She loves stats, and you too.


## Feature

![Screenshot](https://pbs.twimg.com/media/DhUu3gCVQAAmdEm.jpg)

* Collect daily statistics
* Send statistics to Discord.

### Other features that are planned

* Slack support.
* Customizable Stats and Formats.


## Usage

Now Printing.


## Supported Services and Variables

### Twitter

<details>
  <summary>Valiables</summary>

* `int` followers
* `int` following
* `int` id
* `int` likes
* `int` listed
* `str` screen_name
* `int` tweets

</details>

### Mastodon (Deprecated)

Scraping can not acquire detailed numbers. (1000 or more will be displayed as 1K)

<details>
  <summary>Valiables</summary>

*  `int` followers
*  `int` following
*  `str` instance
*  `int` toots
*  `str` username

</details>

### GitHub

<details>
  <summary>Valiables</summary>

*  `int` contributions_in_last_year
*  `int` followers
*  `int` following
*  `int` public_repositories
*  `int` stars
*  `str` username

</details>

### Steam

<details>
  <summary>Valiables</summary>

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

</details>

### osu!

<details>
  <summary>Valiables</summary>

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

</details>


## Contribution

Are you interested in contributing to this project? It's Awesome!

An issue, pull request, others are always welcome!

I'm just started using Python, it may take a while to understand your code. But I will do my utmost to improve this project!


## License

This project is licensed under the MIT License.


## Author

[Eai](https://github.com/eai04191)