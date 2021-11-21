from django.db import models
from django.utils.translation import gettext_lazy as _


class CategoryDepth(models.IntegerChoices):
    FIRST = 0, _("대분류")
    SECOND = 1, _("중분류")
    THIRD = 2, _("소분류")

class ProductCategory(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    depth = models.IntegerField(choices=CategoryDepth.choices)
    parent_category = models.ForeignKey('self', related_name="parent_category_name", on_delete=models.CASCADE,
                                        null=True, blank=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name