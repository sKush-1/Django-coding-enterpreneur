from django import forms  
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        
    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        qs = Article.objects.all().filter(title__icontains=title)
        # print("query",len(qs))
        if len(qs)>0:
            self.add_error("title", f"{title} is already in use.")
        return data

class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    
    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     title = cleaned_data.get('title')
    #     if title.lower() == 'office':
    #         raise forms.ValidationError('This title is taken.')
    #     return title 
    
    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == 'office':
            self.add_error('title', 'This title is taken.')
        if "office" in content:
            self.add_error('content', "Office can't be in content")
        return cleaned_data
        
    
    
    
    