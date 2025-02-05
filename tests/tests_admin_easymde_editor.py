from django.forms import Media
from django.test import TestCase
from django.utils.safestring import SafeString

from easymde.widgets import AdminEasyMDEEditor


class AdminEasyMDEEditorTests(TestCase):
    def setUp(self):
        self.widget = AdminEasyMDEEditor()

    def test_admin_media(self):
        """Test that admin widget includes additional CSS"""
        media = self.widget.media
        self.assertIsInstance(media, Media)
        self.assertIn("easymde/easymde_admin.min.css", str(media))
        # Should still include base media
        self.assertIn("easymde/easymde.min.js", str(media))
        self.assertIn("easymde/easymde.min.css", str(media))

    def test_admin_render(self):
        """Test that admin widget renders correctly"""
        rendered = self.widget.render("test", "content", {"class": "test"})
        self.assertIsInstance(rendered, SafeString)
        self.assertIn("easymde-box", rendered)
        self.assertIn("data-easymde-options", rendered)
