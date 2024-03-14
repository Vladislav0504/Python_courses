"""XML files."""
from xml.etree.ElementTree import fromstring


def main():
    """My function."""
    with open("map2.osm", "r", encoding="utf8") as file:
        xml = file.read()
    root = fromstring(xml)
    fuel = sum(tag.attrib["v"] == "fuel" for tag in root.findall("node/tag"))
    print(fuel)


if __name__ == "__main__":
    main()
