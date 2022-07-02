from django.db import models


class ResponsavelManager(models.Manager):

    def get_queryset(self):
        return super(ResponsavelManager, self).get_queryset().filter(user__groups__name='responsavel_principal')
