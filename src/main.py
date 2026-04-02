from textnode import TextNode, TextType

def main():
    new_node = TextNode("Anchor text", TextType.LINK, "https://www.boot.dev")
    print(new_node)

if __name__ == "__main__":
    main()