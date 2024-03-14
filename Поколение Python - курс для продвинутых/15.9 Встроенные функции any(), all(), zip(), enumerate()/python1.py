"""Functions."""


def ignore_command(command: str) -> bool:
    """Ignore command."""
    ignore = ["alias", "configuration", "ip", "sql", "select", "update",
              "exec", "del", "truncate"]
    return any(word in command for word in ignore)


def main():
    """My function."""
    assert ignore_command("get ip")
    assert ignore_command("select all")
    assert ignore_command("delete")
    assert not ignore_command("trancate")


if __name__ == "__main__":
    main()
