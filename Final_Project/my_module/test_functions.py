"""Test for my functions.

Note: Couldn't include many tests because my project consists of a chatbot which requires a lot of user inpu. Therefore additiional assert statements are given in the main scripts and functions files.

"""

import my_module.functions as fc

def test_add_task():
    assert callable(fc.add_task)

def test_archive_task():
    assert callable(fc.archive_task)
    
def test_display_list():
    assert callable(fc.display_list)
    
def test_status_update():
    assert callable(fc.status_update)
    
    
test_add_task()
test_archive_task()
test_display_list()
test_status_update()