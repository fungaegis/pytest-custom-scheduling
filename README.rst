pytest-custom-scheduling: pytest plugin
=======================================

Rewrite pytest-xdist pytest_xdist_make_scheduler function, Modify load scheduling.

Support custom grouping.

Rename testcases name and testcases nodeid, support allure report.

Change testcases nodeid and testcases name encoding to UTF-8 and unicode escape

Format:
  - name: ids
  - nodeid: ``group_name::ids``

install
=======

``pip install pytest-custom-scheduling``

Usage
=====

command line:``pytest --switch={on:off} --rename={on:off} -n=auto``

tip: pytest-xdist must be turned on

options:
  - switch: Used to open plugin, default "off"
  - rename: Used to open rename, default "off"

Use ``{...}`` as a marker custom grouping.

Support "{ filename::classname }" format for multi-level settings

Demo
====
.. code-block:: python

    import pytest
    @pytest.mark.parametrize("group",
                             ["group_1", "group_2", "group_3", "group_4", "group_5", "group_6",
                              "group_7", "group_8", "group_9", "group_10", "group_11", "group_12"],
                             ids=["group_1{group_1}", "group_2{group_2}", "group_3{group_3}",
                                  "group_4{group_4}", "group_5{group_5}", "group_6{group_6}",
                                  "group_7{group_7}", "group_8{group_8}", "group_9{group_9}",
                                  "group_10{group_10}", "group_11{group_11}", "group_12{group_12}"])
    @pytest.mark.parametrize("group", ["group_4", "group_5", "group_6"],
                             ids=["group_4{group_5}", "group_5{group_5}", "group_6{group_5}"])
    def test_05(group):
        a = "hello"
        b = "world"
        assert a == b

cmd line: ``pytest --switch=on --rename=on -n=auto``