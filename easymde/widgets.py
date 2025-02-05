import uuid

from django import forms
from django.conf import settings
from django.contrib.admin import widgets as admin_widgets
from django.utils.safestring import mark_safe

from .utils import json_dumps

GLOBAL_OPTIONS = getattr(settings, "EASYMDE_OPTIONS", {})


class EasyMDEEditor(forms.Textarea):
    def __init__(self, *args, **kwargs):
        self.custom_options = kwargs.pop("easymde_options", {})
        super().__init__(*args, **kwargs)

    @property
    def options(self):
        options = GLOBAL_OPTIONS.copy()
        options.update(self.custom_options)
        if "autosave" in options and options["autosave"].get("enabled", False):
            options["autosave"]["uniqueId"] = str(uuid.uuid4())
        return options

    def render(self, name, value, attrs=None, renderer=None):
        if "class" not in attrs.keys():
            attrs["class"] = ""

        attrs["class"] += " easymde-box"

        attrs["data-easymde-options"] = json_dumps(self.options)

        html = super().render(name, value, attrs, renderer=renderer)

        # insert this style tag to fix the label from breaking into the toolbar
        html += "<style>.field-%s label { float: none; }</style>" % name

        return mark_safe(html)

    def _media(self):
        js = ("easymde/easymde.min.js", "easymde/easymde.init.js")

        css = {"all": ("easymde/easymde.min.css",)}
        return forms.Media(css=css, js=js)

    media = property(_media)


class AdminEasyMDEEditor(EasyMDEEditor, admin_widgets.AdminTextareaWidget):
    def _media(self):
        css = {
            "all": ["easymde/easymde_admin.min.css"],
        }
        return super().media + forms.Media(css=css)

    media = property(_media)
