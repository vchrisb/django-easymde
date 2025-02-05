from django.contrib.admin import widgets as admin_widgets
from django.db.models import TextField

from .widgets import AdminEasyMDEEditor, EasyMDEEditor


class EasyMDEField(TextField):
    def __init__(self, *args, **kwargs):
        self.options = kwargs.pop("easymde_options", {})
        self.widget = EasyMDEEditor(
            easymde_options=self.options,
        )
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {"widget": self.widget}
        defaults.update(kwargs)
        if defaults["widget"] == admin_widgets.AdminTextareaWidget:
            defaults["widget"] = AdminEasyMDEEditor(
                easymde_options=self.options,
            )
        return super().formfield(**defaults)
