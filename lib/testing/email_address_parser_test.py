from lib.email_address_parser import EmailAddressParser

def test_parse_comma_separated():
    email_addresses = "john@doe.com, person@somewhere.org"
    parser = EmailAddressParser(email_addresses)
    assert parser.parse() == ["john@doe.com", "person@somewhere.org"]

def test_parse_space_separated():
    email_addresses = "john@doe.com person@somewhere.org"
    parser = EmailAddressParser(email_addresses)
    assert parser.parse() == ["john@doe.com", "person@somewhere.org"]

def test_parse_duplicates():
    email_addresses = "john@doe.com, person@somewhere.org, john@doe.com"
    parser = EmailAddressParser(email_addresses)
    assert parser.parse() == ["john@doe.com", "person@somewhere.org"]

def test_parse_mixed_separators():
    email_addresses = "john@doe.com, person@somewhere.org john@doe.com"
    parser = EmailAddressParser(email_addresses)
    assert parser.parse() == ["john@doe.com", "person@somewhere.org"]
