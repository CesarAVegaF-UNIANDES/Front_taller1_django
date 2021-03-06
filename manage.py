#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from app.main import cargar_datos

cargados = False

def main():
    global cargados
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Front_django.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    """
    if not cargados:
        cargados = cargar_datos()"""
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    cargar_datos()
    main()
