"""Html files."""


def main():
    """My function."""
    rows, cols = 10, 10
    print("<html>", "<body>", "<table>")
    for i in range(1, rows + 1):
        print("<tr>")
        for j in range(1, cols + 1):
            result = i * j
            print(f"<td> <a href=http://{result}.ru>{result}</a> </td>")
        print("</tr>")
    print("</table>", "</body>", "</html>")


if __name__ == "__main__":
    main()
