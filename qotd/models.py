from django.db import models


class BaseQuote(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False, help_text='Name of the quote')
    quote_type = models.CharField(max_length=10, null=False, blank=False, help_text='Type of concrete quote')

    @classmethod
    def get_quote_type_string(cls):
        return f'{cls._meta.app_label}.{cls._meta.model_name}'

    class Meta:
        verbose_name = 'Base Quote'
        verbose_name_plural = 'Base Quotes'


class MOTD(BaseQuote):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quote_type = f'{self.__class__._meta.app_label}.{self.__class__._meta.model_name}'

    class Meta:
        proxy = True
        verbose_name = 'Message of the Day'
        verbose_name_plural = 'Daily Messages'


class MOTW(BaseQuote):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quote_type = f'{self.__class__._meta.app_label}.{self.__class__._meta.model_name}'

    class Meta:
        proxy = True
        verbose_name = 'Message of the Week'
        verbose_name_plural = 'Weekly Messages'
