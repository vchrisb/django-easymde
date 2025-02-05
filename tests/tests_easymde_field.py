from django.contrib.admin import widgets as admin_widgets
from django.test import TestCase

from easymde.fields import EasyMDEField
from easymde.widgets import AdminEasyMDEEditor, EasyMDEEditor


class EasyMDEFieldTests(TestCase):
    def test_field_initialization(self):
        """Test that the field initializes with correct widget"""
        field = EasyMDEField()
        self.assertIsInstance(field.widget, EasyMDEEditor)

    def test_field_with_custom_options(self):
        """Test field initialization with custom options"""
        options = {"spellChecker": False}
        field = EasyMDEField(easymde_options=options)
        self.assertEqual(field.widget.custom_options, options)

    def test_formfield_in_admin(self):
        """Test formfield method when used in admin"""
        field = EasyMDEField()
        form_field = field.formfield(widget=admin_widgets.AdminTextareaWidget)
        self.assertIsInstance(form_field.widget, AdminEasyMDEEditor)
