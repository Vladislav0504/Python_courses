"""XML files."""
from xmltodict import parse


def main():
    """My function."""
    with open("map1.osm", "r", encoding="utf8") as file:
        xml = file.read()
    parsed_xml = parse(xml)
    print(parsed_xml["osm"]["node"][100]["@id"])


if __name__ == "__main__":
    main()
