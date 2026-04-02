from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    new_node = TextNode("Anchor text", TextType.LINK, "https://www.boot.dev")
    print(new_node)
    html_node = HTMLNode("a", "this is a value")
    print(html_node)
    html_props_node = HTMLNode("p", "value", children=None, props={"href": "https://www.d.com", "target": "_blank"})
    print(html_props_node.props_to_html())

if __name__ == "__main__":
    main()