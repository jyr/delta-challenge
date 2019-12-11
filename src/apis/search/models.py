from django.db import models

# TODO: django-dynamic-scraper use python_2_unicode_compatible and djdango
#       Removed private Python 2 compatibility APIs
#       https://github.com/holgerd77/django-dynamic-scraper/issues/138

# from dynamic_scraper.models import Scraper, SchedulerRuntime


class NewsWebsite(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    # scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
    # scraper_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    news_website = models.ForeignKey(NewsWebsite,on_delete=models.PROTECT)
    reference = models.URLField()
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


# class ArticleItem(DjangoItem):
#     django_model = Article
