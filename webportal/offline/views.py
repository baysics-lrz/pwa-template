from django.views.generic import TemplateView


class StartPage(TemplateView):
    template_name = 'offline_startpage.html'

class Category1Interface(TemplateView):
    template_name = 'offline_category1_update.html'

class Category2Interface(TemplateView):
    template_name = 'offline_category2_update.html'

class Category3Interface(TemplateView):
    template_name = 'offline_category3_update.html'

class Category4Interface(TemplateView):
    template_name = 'offline_category4_update.html'



