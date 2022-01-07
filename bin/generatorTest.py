import click
import re


test1 = """tests [[SoftLayer_Product_Package]] some more"""
test2 = """See [[SoftLayer_Product_Package/getCategories|getCategories]] or [[SoftLayer_Product_Package/getItems|getItems]] for more information. """
test3 = """some other test [[SoftLayer_Account::id]]"""

def wikiToMarkdownFilter(text):
    # [[SoftLayer_Account]] -> reference/datatypes/SoftLayer_Account
    text = re.sub(r'\[\[(?P<one>\w+)( \(type\))?(\|.*)?\]\]', "[\g<one>]({{<ref \"reference/datatypes/\g<one>\">}})", text)
    # [[SoftLayer_Account/getObject]] -> reference/services/SoftLayer_Account/getObject
    text = re.sub(r'\[\[(?P<one>\w+)\/(?P<two>\w+)(\|.*)?\]\]', "[\g<one>::\g<two>]({{<ref \"reference/services/\g<one>/\g<two>\">}})", text)
    # [[SoftLayer_Account::id]] -> reference/datatypes/SoftLayer_ACccount/#id
    text = re.sub(r'\[\[(?P<one>\w+)::(?P<two>\w+)(\|.*)?\]\]', "[\g<one>::\g<two>]({{<ref \"reference/datatypes/$1/#$2\">}})", text)
    
    return text



@click.command()

def main():
    text = wikiToMarkdownFilter(test3)
    print(text)


if __name__ == "__main__":
    main()