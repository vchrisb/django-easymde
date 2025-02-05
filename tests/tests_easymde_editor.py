from django.forms import Media
from django.test import TestCase
from django.utils.safestring import SafeString

from easymde.widgets import EasyMDEEditor


class EasyMDEEditorTests(TestCase):
    def setUp(self):
        self.widget = EasyMDEEditor()
        self.test_name = "test"
        self.test_value = "Test content"
        self.test_attrs = {"class": "test-class"}

    def test_initialization_with_options(self):
        """Test widget initialization with custom options"""
        options = {"spellChecker": False}
        widget = EasyMDEEditor(easymde_options=options)
        self.assertEqual(widget.custom_options, options)

    def test_autosave_unique_id(self):
        """Test that autosave gets unique ID"""
        widget1 = EasyMDEEditor(easymde_options={"autosave": {"enabled": True}})
        widget2 = EasyMDEEditor(easymde_options={"autosave": {"enabled": True}})
        options1 = widget1.options
        options2 = widget2.options
        self.assertNotEqual(options1["autosave"]["uniqueId"], options2["autosave"]["uniqueId"])

    def test_render_output(self):
        """Test the rendered output of the widget"""
        rendered = self.widget.render(self.test_name, self.test_value, self.test_attrs)
        self.assertIsInstance(rendered, SafeString)
        self.assertIn("easymde-box", rendered)
        self.assertIn("data-easymde-options", rendered)
        self.assertIn(self.test_value, rendered)
        self.assertIn("style", rendered)

    def test_media_property(self):
        """Test that correct media files are included"""
        media = self.widget.media
        self.assertIsInstance(media, Media)
        self.assertIn("easymde/easymde.min.js", str(media))
        self.assertIn("easymde/easymde.min.css", str(media))
