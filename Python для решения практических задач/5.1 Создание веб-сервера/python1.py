"""Html files."""


def main():
    """My function."""
    num = 1
    rows, cols = 2, 2
    print("<html>", "<body>", "<table>")
    for _ in range(rows):
        print("<tr>")
        for _ in range(cols):
            print("<td>", num, "</td>")
            num += 1
        print("</tr>")
    print("</table>", "</body>", "</html>")


if __name__ == "__main__":
    main()
