import importlib.util
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch


class ManageTest(TestCase):
    def test_main_executes_django_command(self):
        manage_path = Path(__file__).resolve().parents[2] / "manage.py"

        spec = importlib.util.spec_from_file_location("manage", manage_path)
        manage = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(manage)

        with patch("django.core.management.execute_from_command_line") as execute:
            with patch("sys.argv", ["manage.py", "check"]):
                manage.main()

        execute.assert_called_once_with(["manage.py", "check"])
