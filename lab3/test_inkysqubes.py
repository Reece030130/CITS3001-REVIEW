from unittest import TestCase
import os
from inkysqubes import inky_squbes

folderSqubes = 'sampleSqubes'


class Test(TestCase):
    def test_inky_squbes(self):
        for filename in os.listdir(folderSqubes):
            if filename.endswith('.in'):
                input_small_file = os.path.join(folderSqubes, filename)
                expected_output_file = os.path.join(folderSqubes, filename.replace('.in', '.ans'))
                with open(input_small_file, 'r') as f:
                    a, b = map(int, f.readline().split())
                with open(expected_output_file, 'r') as ansfile:
                    expected_result = ansfile.readline().strip()
                    self.assertEqual(expected_result, inky_squbes(a, b))