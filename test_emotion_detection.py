import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test Case 1
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        
        # Test Case 2
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        
        # Test Case 3
        result_3 = emotion_detector('I feel just terrible about this')
        self.assertEqual(result_3['dominant_emotion'], 'sadness')
        
        # Test Case 4
        result_4 = emotion_detector('I am just so scared about this')
        self.assertEqual(result_4['dominant_emotion'], 'fear')
        
        # Test Case 5
        result_5 = emotion_detector('I am thoroughly disgusted by this')
        self.assertEqual(result_5['dominant_emotion'], 'disgust')

if __name__ == '__main__':
    unittest.main()
