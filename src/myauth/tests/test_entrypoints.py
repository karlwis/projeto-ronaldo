import importlib
import os
from unittest import TestCase
from unittest.mock import patch


class EntrypointsTest(TestCase):
    def test_asgi_application_is_created(self):
        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("DJANGO_SETTINGS_MODULE", None)
            module = importlib.import_module("meu_projeto.asgi")
            self.assertIsNotNone(module.application)

    def test_wsgi_application_is_created(self):
        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("DJANGO_SETTINGS_MODULE", None)
            module = importlib.import_module("meu_projeto.wsgi")
            self.assertIsNotNone(module.application)
