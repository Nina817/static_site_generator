from extract_title import extract_title
import unittest

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        markdown = """random text

blahhhh blahblahblah
blah

# Heading 1

## Heading 2

### Heading 3"""    
        self.assertEqual(extract_title(markdown), 'Heading 1')

    def test_extract_title_2(self):
        markdown = '# Another heading'
        self.assertEqual(extract_title(markdown), 'Another heading')
    
    def test_extract_title_3(self):
        markdown = '          # A nice fun heading       '
        self.assertEqual(extract_title(markdown), 'A nice fun heading')
    
    def test_extract_title_4(self):
        markdown = '## Not heading 1'
        with self.assertRaises(Exception):
            extract_title(markdown)