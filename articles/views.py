import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.conf import settings
import datetime
from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ViewSet):
    def list(self, request):
        query = request.query_params.get('query')
        language = request.query_params.get('language')

        if not query or not language:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        response = requests.get(f'https://newsapi.org/v2/everything?q={query}&language={language}&from={get_from_date()}&sortBy=publishedAt&apiKey={settings.API_KEY}')
        data = response.json()
        articles = []

        for article_data in data['articles']:
            article = Article(
                source_id=article_data['source']['id'] if article_data['source']['id'] else None,
                source_name=article_data['source']['name'],
                author=article_data['author'],
                title=article_data['title'],
                description=article_data['description'],
                url=article_data['url'],
                url_to_image=article_data['urlToImage'],
                published_at=article_data['publishedAt'],
                content=article_data['content']
            )
            articles.append(article)

        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

def get_from_date():
  today = datetime.date.today()
  from_date = today - datetime.timedelta(days=7)
  return from_date.strftime("%Y-%m-%d")
