[![code-best-practices image](https://library.brown.edu/good_code/project_image/ils_location_mapper/)](https://library.brown.edu/good_code/project_info/ils_location_mapper/)


#### overview

This is the web-app code for an API that maps codes in our Sierra [ILS](https://en.wikipedia.org/wiki/Integrated_library_system) to 'building' and 'display' and 'format' strings useful for other applications.

It is used by a [tech-services-reports](https://github.com/birkin/ts_reporting_project) application and a [new-titles application](https://github.com/Brown-University-Library/kochief_titles_project).

- Usage:

    - `api-url/v1/?code=arc` returns data including results for the submitted code, like...

            {
              "items": [
                {
                  "building": "Hay",
                  "code": "arc",
                  "display": "HAY ARCHIVES",
                  "format": "Book"
                }
              ]
            }

    - `api-url/v1/?data=dump` returns over 250 entries including...

            {
              "items": {
                "arc": {
                  "building": "Hay",
                  "display": "HAY ARCHIVES",
                  "format": "Book"
                },
                "arccd": {
                  "building": "Hay",
                  "display": "HAY ARCHIVES CD",
                  "format": "CD (Sound Recording)"
                }
              }
            }


- Permitted staff may edit entries via the url `api-url/login/`.

- code contact: [birkin](mailto:birkin_diana@brown.edu)
