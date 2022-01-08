import click
import re


test1 = """tests [[SoftLayer_Product_Package]] some more"""
test2 = """See [[SoftLayer_Product_Package/getCategories|getCategories]] or [[SoftLayer_Product_Package/getItems|getItems]] for more information. """
test3 = """some other test [[SoftLayer_Account::id]]"""
test4 = """Retrieve a single [[SoftLayer_Account_Attribute]] record by its [[SoftLayer_Account_Attribute_Type|types's]] key name. """
test5 = """{"name":"getAttributeByType","type":"SoftLayer_Account_Attribute","doc":"Retrieve a single [[SoftLayer_Account_Attribute]] record by its [[SoftLayer_Account_Attribute_Type|types's]] key name. ","maskable":true,"parameters":[{"name":"attributeType","type":"string","""
def wikiToMarkdownFilter(text):
    # [[SoftLayer_Account]] -> reference/datatypes/SoftLayer_Account
    text = re.sub(r'\[\[(?P<one>\w+)( \(type\))?(\|[A-Za-z_\']*)?\]\]', '[\g<one>](reference/datatypes/\g<one>)', text)
    # [[SoftLayer_Account/getObject]] -> reference/services/SoftLayer_Account/getObject
    text = re.sub(r'\[\[(?P<one>\w+)\/(?P<two>\w+)(\|.*)?\]\]', "[\g<one>::\g<two>](reference/services/\g<one>/\g<two>)", text)
    # [[SoftLayer_Account::id]] -> reference/datatypes/SoftLayer_ACccount/#id
    text = re.sub(r'\[\[(?P<one>\w+)::(?P<two>\w+)(\|.*)?\]\]', "[\g<one>::\g<two>](reference/datatypes/$1/#$2)", text)
    
    return text



@click.command()

def main():
    text = wikiToMarkdownFilter(test5)
    print(text)


if __name__ == "__main__":
    main()