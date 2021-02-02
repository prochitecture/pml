from . import getPythonCode, compare
import ast

input = """
facade[item.front and style.count<=1] {
    class: facade_with_door;
}
"""

referenceOutput = """
Facade(
    condition = lambda item : item.front and self.count <= 1,
    cl = "facade_with_door"
)
"""


def test_style_variable():
    output = getPythonCode(input)
    ast.parse(output)
    assert compare(output, referenceOutput)