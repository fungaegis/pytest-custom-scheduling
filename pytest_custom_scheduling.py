import re
import pytest
from xdist.scheduler import (
    EachScheduling,
    LoadScheduling,
    LoadScopeScheduling,
    LoadFileScheduling,
)


class LoadCustomNameScheduling(LoadScopeScheduling):

    def _split_scope(self, nodeid):
        pattern = r"{(\w*)}"
        res = re.search(pattern, nodeid)
        if res:
            return res.group(1)
        else:
            return "default"


def pytest_addoption(parser):
    group = parser.getgroup("custom-xdist", "Custom grouping for pytest-xdist")
    group.addoption("--switch",
                    action="store",
                    default="off",
                    choices=["on", "off"],
                    help="open loads custom name scheduling"
                    )
    group.addoption("--rename",
                    action="store",
                    default="off",
                    choices=["on", "off"],
                    help="open rename testcase name and nodeid"
                    )


@pytest.mark.trylast
def pytest_xdist_make_scheduler(config, log):
    if config.getvalue("switch") == "on":
        return LoadCustomNameScheduling(config, log)

    dist = config.getvalue("dist")
    schedulers = {
        "each": EachScheduling,
        "load": LoadScheduling,
        "loadscope": LoadScopeScheduling,
        "loadfile": LoadFileScheduling
    }
    return schedulers[dist](config, log)


@pytest.mark.trylast
def pytest_collection_modifyitems(items):
    value = items[0].config.getvalue("rename")
    if value == "on":
        group_pattern = r"{([\w:]*)}"
        for item in items:
            item.name = item.name.encode("utf-8").decode("unicode_escape")
            item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
            res = re.search(group_pattern, item.name)
            if res:
                name = res.group(1)
                id_name = item.callspec.id.encode("utf-8").decode("unicode_escape")
                item.name = id_name
                item._nodeid = name.capitalize() + "::" + id_name
