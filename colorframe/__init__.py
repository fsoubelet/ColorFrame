"""
Created on 2020.07.30
:author: Felix Soubelet
"""

from .api import BorderCreator
from .__main__ import app  # noqa: F401  # imported for script creation at package installation

__title__ = "colorframe"
__description__ = "A simple package to add colored borders on pictures."
__url__ = "https://github.com/fsoubelet/ColorFrame"
__version__ = "0.3.1"
__author__ = "Felix Soubelet"
__author_email__ = "felix.soubelet@cern.ch"
__license__ = "MIT"

__all__ = ["BorderCreator"]
