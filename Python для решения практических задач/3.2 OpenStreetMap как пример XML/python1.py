"""XML files."""
from xmltodict import parse


def main():
    """My function."""
    with open("map1.osm", "r", encoding="utf8") as file:
        xml = file.read()
    parsed_xml = parse(xml)
    count_tag = sum("tag" in node for node in parsed_xml["osm"]["node"])
    print(count_tag, len(parsed_xml["osm"]["node"]) - count_tag)


if __name__ == "__main__":
    main()
