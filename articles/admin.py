from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ScopesInArticle, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main') == True:
                count += 1
        if count > 1:
            raise ValidationError('Укажите один основной тег')
        if count < 1:
            raise ValidationError('Обязательно должен быть один основной тег')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = ScopesInArticle
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass
