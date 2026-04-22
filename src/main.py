from textnode import *
from htmlnode import *
from inline_markdown import *

def main():
    # new_node = TextNode("Anchor text", TextType.LINK, "https://www.boot.dev")
    # print(new_node)
    
    # html_node = HTMLNode("a", "this is a value")
    # print(html_node)
    
    # html_props_node = HTMLNode("p", "value", children=None, props={"href": "https://www.d.com", "target": "_blank"})
    # print(html_props_node.props_to_html())

    # grandchild_node = LeafNode("b", "grandchild")
    # child_node = ParentNode("span", [grandchild_node])
    # parent_node = ParentNode("div", [child_node])
    # print(parent_node.to_html())

    # child_node1 = LeafNode("span", "child")
    # child_node2 = LeafNode("p", "some text")
    # parent_node = ParentNode("div", [child_node1, child_node2])
    # print(parent_node.to_html())

    # node = TextNode("This is a text node", TextType.BOLD)
    # html_node = text_node_to_html_node(node)
    # print(html_node)

    # node = TextNode("This is text with a `code block` word", TextType.TEXT)
    # new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    # print(new_nodes)

    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))

    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text))

    print(text_to_textnodes(f"This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"))


if __name__ == "__main__":
    main()