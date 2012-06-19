=======================
Django Rich Text Editor
=======================

.. contents::

Overview
========

Built on top of the open source FCKEditor, django-rtf allows you to easily turn a plain Django TextField into a RichTextField (RTF) that's rendered with a rich text editor widget, with features such as bold text and bulleted lists. At the model level, you need to use the RichTextField class (which is derived from Django's TextField class) for those fields your want to be RTF's.  That's all there's to it if you use standard Django forms.


Demo App
========

A demontration app is included under the demo directory, together with a SQLite3 database containing George Washington's resume in rich text, simply go under the ``demo`` directory and type ``python manage.py runserver`` to run the demo application.


Usage
=====
Because RTF texts are stored in the database in HTML, when rendering them using the ``{{ field }}`` syntax, you need to have ``{% autoescape off %}`` around them.

To prevent exploits such as cross site scripting, RichTextFields are cleaned at the server side with the excellent lxml library (http://lxml.de/) to disinfect dangerous tags like ``<script>`` or ``iframe``. This cleaning operation is disabled when the ``ENABLE_RTF_CLEAN`` settings is set to False (as in the included demo app). Be sure to set ``ENABLE_RTF_CLEAN`` to ``True`` in production applications. To install lxml on Ubuntu, install the ``python-lxml`` apt package.


To customize the styles of the rendered rich text, you can assign a custom class to the DIV (or SPAN) involved and use CSS !important clause (for example, ::

  .rich li { list-style:disc !important; }

will ensure all bullet lists in a RTF has disc style bullets.


If you are using Django ModelForms, You may need to tell the form to use RichTextWidget class for certain fields.

Example ::

  class RichNewsForm(forms.ModelForm):
    ...
    class Meta:
        model = NewsArticle
        fields = ('title', 'date_published', 'content')
        widgets = {
            'date_published': DateDropdownWidget,
            'content': RichTextWidget,
        }


Dynamically Show/Hide Rich Editors
==================================

In JavaScript, calling ``showAllRichEditors()`` will show all hidden rich text editors, while ``hideAllRichEditors()`` will do the opposite.


Read RTF value from JavaScript
==============================
If you are bypassing normal HTML form submission (i.e. doing $.post() yourself), you need to read RTF values yourself::
  $('#edit-popup-form').find('textarea.rich').each(function(){
     var editor = FCKeditorAPI.GetInstance($(this).attr('name'));
     var rich_text = editor.GetData();
  });

Integration with Django South
=============================
If you uses the excellent Django South app to manage the migration of your database schemas, to make RichTextField work with South you need to include the code below, see https://bitbucket.org/carljm/django-markitup/src/tip/markitup/fields.py#cl-88  for details::

  from south.modelsinspector import add_introspection_rules
  add_introspection_rules(
    rules=[
        (
            (RichTextField,),
            [],
            {'no_frozen_fields': (True, {'is_value':True})},
            )
        ],
    patterns=["^rich_text\.RichTextField",
              "^RichTextField",
              ]
              )

Credits
=======
* Built by and for [Zanbato](https://zanbato.com). [Ping us](https://zanbato.com/careers/) if you're interested in working with us!
* Developed by [Zhenlei Cai]
