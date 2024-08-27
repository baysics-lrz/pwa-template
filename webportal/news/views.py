from django.views.generic import TemplateView
from .models import Article


# Create your views here.
class ArticleView(TemplateView):
    template_name = 'news.html'

    def get_context_data(self, **kwargs):
        articles = Article.objects.all().order_by('-creation_time')
        return {'articles': articles}
