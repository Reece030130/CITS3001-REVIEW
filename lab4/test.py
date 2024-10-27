import os

from gostonepuzzle import gostonepuzzle

def run_test(input_file, answer_file):
    with open(input_file, 'r') as f:
        length = int(f.readline().strip())
        initial_stone = list(f.readline().strip()) + ['.'] * 2
        target_stone = list(f.readline().strip()) + ['.'] * 2

    result = gostonepuzzle(initial_stone, target_stone)

    with open(answer_file, 'r') as f:
        expected = f.read().strip()

    print(f"Test {input_file}: {'Passed' if str(result) == expected else 'Failed'}")

if __name__ == '__main__':
    folder = 'samples-gostonepuzzle'
    test_files = [(os.path.join(folder, f), os.path.join(folder, f.replace('.in', '.ans')))
                  for f in os.listdir(folder) if f.endswith('.in')]

    for input_file, answer_file in test_files:
        run_test(input_file, answer_file)