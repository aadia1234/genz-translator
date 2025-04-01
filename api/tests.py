from translate import translate_genz_to_english
import unittest

class TestTranslateGenZToEnglish(unittest.TestCase):
    def test_basic_translation(self):
        # Test a simple Gen Z sentence
        sentence = "Lit fam, no cap."
        translation = translate_genz_to_english(sentence)
        print_translation(sentence, translation)
        
        
    
        
def print_translation(sentence, translation):
    print(f"Original: {sentence}")
    print(f"Translation: {translation}")
        
if __name__ == '__main__':
    unittest.main()