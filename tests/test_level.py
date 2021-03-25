from . import makeTest


level_only = (
"""
level {
    class: myclass;
}
""",
"""
Level(
    roofLevels = False,
    allLevels = False,
    cl = "myclass"
)
"""
)


def test_level_only():
    makeTest(level_only)