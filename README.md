# Pechinchator Scraper App

This app extracts from websites that have discount coupons and products on sale.
 
Project made with **Python** and **Scrapy**.

## How to run?

_If you use Windows, the best way is install some linux distro._

First of all, clone this project.

```bash
$ git checkout https://github.com/leonardocouy/pechinchator-scraper.git
$ cd penchichator-scraper
```

Now, choose below your preferred way to make your dev environment:

**Ensure that you had docker and docker-compose installed**

### Docker way

Build
```bash
$ docker-compose build
```

If you want to run one of the spiders you may use this command:
```
$ docker-compose run --rm crawler scrapy run <SPIDER_NAME>
$ docker-compose run --rm crawler scrapy run hardmob
```

If you want to run all spiders you may use only:
```
## by default it will run all
$ docker-compose up 

## or
$ docker-compose run --rm crawler python run.py
```

### Virtualenv way

**Ensure that you had virtualenv installed (if you don't know, google it!).**

**Run this commands:**
```
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
