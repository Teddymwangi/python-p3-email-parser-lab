import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        # Using regular expression to split the string based on comma or space
        addresses = re.split(r'[,\s]+', self.email_addresses)
        # Filtering out empty strings and duplicates, then sorting
        unique_addresses = sorted(set(filter(None, addresses)))
        return unique_addresses
