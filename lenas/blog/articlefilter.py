from django import forms

from .models import Article


class ArticleFilter(forms.Form):
    tag = forms.ChoiceField(choices=[], required=False) 
    year = forms.ChoiceField(choices=[], required=False)
    month = forms.ChoiceField(choices=[], required=False)
    
    def __init__(self, *args, **kwargs):
        super(ArticleFilter, self).__init__(*args, **kwargs)
        tags = []
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
        articles = Article.objects.all()
        for article in articles:
            for tag in article.tags.all():
                if tag not in tags:
                    tags.append(tag)
        TAG_CHOICES += [(x,x) for x in tags]

        years = Article.objects.dates('created','year')
        YEAR_CHOICES += [(x.year,x.year) for x in years]

        self.fields['tag'].choices = TAG_CHOICES
        self.fields['year'].choices = YEAR_CHOICES
        self.fields['month'].choices = MONTH_CHOICES

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
