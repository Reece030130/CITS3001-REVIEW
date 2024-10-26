import os

from flavoursgalore import flavoursgalore

def run_test(input_file, answer_file):
    with open(input_file, 'r') as f:
        flavours = int(f.readline().strip())
        relationship = int(f.readline().strip())
        galore = {int(key): int(value) for _ in range(relationship) for key, value in [f.readline().strip().split()]}

    result = flavoursgalore(galore)

    with open(answer_file, 'r') as f:
        expected = f.read().strip()

    print(f"Test {input_file}: {'Passed' if str(result) == expected else 'Failed'}")

if __name__ == '__main__':
    folder = 'samples-flavoursgalore'
    test_files = [(os.path.join(folder, f), os.path.join(folder, f.replace('.in', '.ans')))
                  for f in os.listdir(folder) if f.endswith('.in')]

    for input_file, answer_file in test_files:
        run_test(input_file, answer_file)