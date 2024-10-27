import os
from collections import defaultdict
from flavoursgalore import flavoursgalore


def run_test(input_file, answer_file):
    with open(input_file, 'r') as f:
        flavours = int(f.readline())
        relation = int(f.readline())
        relations = [tuple(map(int, f.readline().split())) for _ in range(relation)]
    result = flavoursgalore(flavours, relations)
    with open(answer_file, 'r') as f:
        expected = f.read().strip()
    print(f"Test {input_file}: {'Passed' if str(result) == expected else 'Failed                     retry'}")


if __name__ == '__main__':
    folder = 'samples-flavoursgalore'
    test_files = [(os.path.join(folder, f), os.path.join(folder, f.replace('.in', '.ans')))
                  for f in os.listdir(folder) if f.endswith('.in')]
    for input_file, answer_file in test_files:
        run_test(input_file, answer_file)
