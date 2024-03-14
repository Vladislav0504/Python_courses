"""Classes."""
from typing import List, Callable


class ExtendedStack(List):
    """ExtendedStack."""

    __methods = {"sum": "__add__", "sub": "__sub__", "mul": "__mul__",
                 "div": "__floordiv__"}

    def __getattr__(self, attr: str) -> Callable[..., None]:
        """Attribute correction."""
        method = self.__methods.get(attr)
        return lambda: self.append(getattr(self.pop(), method)(self.pop()))


def main():
    """My function."""
    stack = ExtendedStack(range(2, 7))
    print(stack)
    stack.sum()
    print(stack)
    stack.sub()
    print(stack)
    stack.mul()
    print(stack)
    stack.div()
    print(stack)


if __name__ == "__main__":
    main()
