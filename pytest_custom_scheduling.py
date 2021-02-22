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
        pattern = r"\${(\w*)}"
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