__author__ = 'Narvi'
import pytest
from  api.register import Registration

def test(base_url):
    registerLoad = Registration(base_url)
