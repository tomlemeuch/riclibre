from django.contrib import admin
from django.utils.html import format_html

from referendum.models import Referendum, Category, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice


@admin.register(Referendum)
class ReferendumAdmin(admin.ModelAdmin):
    """
    admin class for Referendum model.
    """
    list_display = ("title", "description", "question", "creation_date", "last_update", "publication_date",
                    "event_start", "event_end", "nb_votes", "results")
    list_filter = ("categories", "creation_date", "last_update", "publication_date",
                   "event_start", "event_end",)
    search_fields = ("title", "description", "question")
    inlines = [ChoiceInline, ]

    def results(self, obj):
        """
        Display referendum results as string
        :param obj:
        :return:
        """
        return format_html("<br>".join([f"{choice.title} : {choice.votes_percentage}%" for choice in sorted(
            obj.choice_set.all(),
            key=lambda choice:
            choice.nb_votes,
            reverse=True)]))


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    admin class for Category model.
    """
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    """
    admin class for Choice model.
    """
    list_display = ("referendum", "title", "nb_votes", "percentage")
    search_fields = ("referendum", "title")
    autocomplete_fields = ["referendum"]

    def percentage(self, obj):
        return f"{obj.votes_percentage}%"

    percentage.short_description = "Pourcentage"
