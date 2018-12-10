# myproject/apps.py

from wiki.apps import WikiConfig

class MyWikiConfig(WikiConfig):
    default_site = 'testproject.sites.MyWikiSite'
