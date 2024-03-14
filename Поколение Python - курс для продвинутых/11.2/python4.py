"""Exam."""
from typing import TypeVar

T = TypeVar("T")


def build_query_string(params: dict[str, T]) -> str:
    """Query string."""
    return "&".join(f"{key}={value}" for key, value in sorted(params.items()))


def main():
    """My function."""
    assert build_query_string({"name": "timur",
                               "age": 28}) == "age=28&name=timur"
    assert build_query_string({"sport": "hockey", "game": 2,
                               "time": 17}) == "game=2&sport=hockey&time=17"


if __name__ == "__main__":
    main()
