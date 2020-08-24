from django import forms

from .models import Article

TAG_CHOICES = [(None,'----')]
YEAR_CHOICES = [(None,'----')]

MONTH_CHOICES = [
    (None,'----'),
    (1, 'January'),
    (2, 'February'),
    (3, 'March'),
    (4, 'April'),
    (5, 'May'),
    (6, 'June'),
    (7, 'July'),
    (8, 'August'),
    (9, 'September'),
    (10, 'Octomber'),
    (11, 'November'),
    (12, 'December')
]

class ArticleFilter(forms.Form):
    tags = []
    articles = Article.objects.all()
    for article in articles:
        for tag in article.tags.all():
            if tag not in tags:
                tags.append(tag)
    TAG_CHOICES += [(x,x) for x in tags]

    years = Article.objects.dates('created','year')
    YEAR_CHOICES += [(x.year,x.year) for x in years]

    tag = forms.ChoiceField(choices=TAG_CHOICES, required=False) 
    year = forms.ChoiceField(choices=YEAR_CHOICES, required=False)
    month = forms.ChoiceField(choices=MONTH_CHOICES, required=False)

    def get_articles(self,tags=None):
        query = {}
        if tags is None:
            data = self.cleaned_data
        else:
            query['tags__name__in'] = tags
            articles = Article.objects.filter(**query).order_by('created')
            return articles

        for k in data:
            if data[k] and data[k] is not '----':
                if k == 'month':
                    query['created__month'] = int(data[k])
                elif k == 'year':
                    query['created__year'] = int(data[k])
                elif k == 'tag':
                    query['tags__name__in'] = [data[k]]
        articles = Article.objects.filter(**query).order_by('created')
        return articles
