from translate import translate_sentence
import unittest

class TestTranslateGenZToEnglish(unittest.TestCase):
    def test_basic_translation(self):
        # Test a simple Gen Z sentence
        sentence = "how art thou of breath when thou hast breath to say to me that thou art of breath"
        translation = translate_sentence(sentence)
        print_translation(sentence, translation)
        
        
    
        
def print_translation(sentence, translation):
    print(f"Original: {sentence}")
    print(f"Translation: {translation}")
        
if __name__ == '__main__':
    unittest.main()