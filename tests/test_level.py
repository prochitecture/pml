from . import makeTest


def test_level_only():
    makeTest(
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