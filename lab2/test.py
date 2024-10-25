from maxsumsubarraysmall import max_sum_subarray_better
from maxsumsubarraylarge import max_sum_subarray_divide_and_conquer
import os

folderLarge = 'samples-maxsumsubarraylarge'
folderSmall = 'samples-maxsumsubarraysmall'
for filename in os.listdir(folderSmall):
    if filename.endswith('.in'):
        input_small_file = os.path.join(folderSmall, filename)
        expected_output_file = os.path.join(folderSmall, filename.replace('.in', '.ans'))

        with open(input_small_file, 'r') as f:
            b = f.readline()
            arraylistSmall = list(map(int, f.readline().split()))
        with open(expected_output_file, 'r') as ansfile:
            expected_result = ansfile.readline().strip()

        if str(max_sum_subarray_better(arraylistSmall)) == expected_result:
            print(f"{filename}: Test passed!,got {max_sum_subarray_better(arraylistSmall)}.")
        else:
            print(f"{filename}: Test failed. Expected {expected_result}, got {max_sum_subarray_better(arraylistSmall)}."
                  )
print(f"passed all tests in {folderSmall}")

for filename in os.listdir(folderLarge):
    if filename.endswith('.in'):
        input_large_file = os.path.join(folderLarge, filename)
        expected_output_file = os.path.join(folderLarge, filename.replace('.in', '.ans'))
        with open(input_large_file, 'r') as f:
            b = f.readline()
            arraylistLarge = list(map(int, f.readline().split()))
        with open(expected_output_file, 'r') as ansfile:
            expected_result_large = ansfile.readline().strip()

        if str(max_sum_subarray_divide_and_conquer(arraylistLarge)) == expected_result_large:
            print(f"{filename}: Test passed!, got {max_sum_subarray_divide_and_conquer(arraylistLarge)}.")
        else:
            print(f"{filename}: Test failed. expected : {expected_result_large}, got "
                  f"{max_sum_subarray_divide_and_conquer(arraylistLarge)}."
                  )
print(f"passed all tests in {folderLarge}")
