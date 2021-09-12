import unittest
import sys, os

class TestConsumer(unittest.TestCase):
    def test_transcript_format(self):
        """
        Test that the transcript's format is correct
        """
        
        transcripts = open('./data/Transcripts.txt', 'r', encoding = "utf-8")
        okay = len(transcripts.readlines()) == len(os.listdir('./data/audio'))
        self.assertEqual(result, True)

    



if __name__ == '__main__':
    unittest.main()
