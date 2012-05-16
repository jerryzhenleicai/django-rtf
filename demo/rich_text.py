from django import forms
from django.db import models
from django.conf import settings

class RichTextWidget(forms.Textarea):
    def __init__(self, *args, **kwargs):
        defaults = {'attrs': {'class': 'zb_rich'}}
        defaults.update(kwargs)

        super(RichTextWidget, self).__init__(*args, **defaults)


class RichTextFormField(forms.CharField):
    def __init__(self, widget=None, *args, **kwargs):
        widget = RichTextWidget()
        if 'widget' in kwargs:
            del kwargs['widget']
        super(RichTextFormField, self).__init__( \
            widget=widget, *args, **kwargs)


class RichTextField(models.TextField):

    def __init__(self, **kwargs):
        # For faking the field for south ORM
        self.add_addl_fields = not kwargs.pop('no_frozen_fields', False)
        super(RichTextField, self).__init__(**kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': RichTextFormField}
        defaults.update(kwargs)
        return super(RichTextField, self).formfield(**defaults)

    def get_prep_value(self, value):
        if settings.ENABLE_RTF_CLEAN and value and len(value.strip()) > 0:
            from lxml.html.clean import clean_html
            html = clean_html(value)
        else:
            html = value

        return html


