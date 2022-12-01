import os


def test_create():
    assert os.system('crest create myapp') == 0


def test_migrate():
    assert os.system('crest migrate') == 0
