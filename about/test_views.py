from django.urls import reverse
from django.test import TestCase
from .models import About
from .forms import CollaborateForm

class TestABoutViews(TestCase):

    def setUp(self):
        self.about_content = About(title="About Me", content="This is about me.")
        self.about_content.save()

    def test_render_about_page_with_collaborate_form(self):
        response = self.client.get(reverse(
            'about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About Me", response.content)
        self.assertIn(b"This is about me.", response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)

    
    def test_successful_collaborate_submission(self):
        """Test for posting a comment on a post"""
        form_data = {
            'name': 'Name',
            'email': 'name@name.com',
            'message': 'message'
        }
        response = self.client.post(reverse(
            'about'), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.',
            response.content
        )