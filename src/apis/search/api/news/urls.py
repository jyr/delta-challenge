from django.urls import path

from apis.search.api.news import endpoints

urlpatterns = ([
    path(
        route='',
        view=endpoints.NewsEndpoint.as_view(),
        name='retrieve_news_by_keywords'
    )
])
