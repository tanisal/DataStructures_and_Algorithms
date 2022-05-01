import unittest
from string_reversal import reverse_str

class ReverseTestCase(unittest.TestCase):
    
    def test_string_reversal(self):
        self.assertEqual(reverse_str('Hi'),'iH')
        self.assertEqual(reverse_str('I am here to help!'),'!pleh ot ereh ma I') 

if __name__ == "__main__" :
    unittest.main()