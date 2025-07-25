#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tuuziane.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
