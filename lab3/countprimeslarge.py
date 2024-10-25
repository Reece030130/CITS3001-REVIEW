def count_primes_large(n: int) -> int:
    if n <= 2:
        return 0
    not_primes = [False] * (n + 1)
    not_primes[0] = True
    not_primes[1] = True
    #record number not primes in list not_primes default value is True.
    #the index of list not_primes is the current number which will be checked if not a primes.
    #Then find all not primes.
    for i in range(2, int(n ** 0.5) + 1):
        if not not_primes[i]:
            for j in range(i * i, n + 1, i):
                not_primes[j] = True
    #calculate the count.
    prime_count = sum(1 for i in range(2, n + 1) if not not_primes[i])
    return prime_count


if __name__ == '__main__':
    print(count_primes_large(int(input())))

#TestZone

# import os
#
# from countprimesmall import count_primes_small
# from countprimesmedium import count_primes_large
# from countprimeslarge import count_primes_large
#
# folderSmall = 'samplesmall'
# folderMedium = 'samplemedium'
# folderLarge = 'samplelarge'

# point2 = 0
# for filename in os.listdir(folderSmall):
#     if filename.endswith('.in'):
#         input_small_file = os.path.join(folderSmall, filename)
#         expected_output_file = os.path.join(folderSmall, filename.replace('.in', '.ans'))
#
#         with open(input_small_file, 'r') as f:
#             inputInt = f.readline()
#         with open(expected_output_file, 'r') as ansfile:
#             expected_result = ansfile.readline().strip()
#
#         if str(count_primes_small(int(inputInt))) == expected_result:
#             print(f"{filename}: Test passed!,got {count_primes_small(int(inputInt))}.")
#             point2 +=1
#         else:
#             print(f"{filename}: Test failed. Expected {expected_result}, got {count_primes_small(int(inputInt))}.")
# if point2 == 5:
#     print("All tests passed!")

#point1 = 0
# for filename in os.listdir(folderMedium):
#     if filename.endswith('.in'):
#         input_medium_file = os.path.join(folderMedium, filename)
#         expected_output_file = os.path.join(folderMedium, filename.replace('.in', '.ans'))
#
#         with open(input_medium_file, 'r') as f:
#             inputInt_medium = f.readline()
#         with open(expected_output_file, 'r') as ansfile:
#             expected_result_medium = ansfile.readline().strip()
#
#         if str(count_primes_medium(int(inputInt_medium))) == expected_result_medium:
#             print(f"{filename}: Test passed!,got {count_primes_medium(int(inputInt_medium))}.")
#             point1 +=1
#         else:
#             print(f"{filename}: Test failed. Expected {expected_result_medium}, got "
#                   f"{count_primes_medium(int(inputInt_medium))}.")
#     else:
#         continue
# if point1 == 7:
#     print("All tests passed!")

# point = 0
# for filename in os.listdir(folderLarge):
#     if filename.endswith('.in'):
#         input_large_file = os.path.join(folderLarge, filename)
#         expected_output_file = os.path.join(folderLarge, filename.replace('.in', '.ans'))
#
#         with open(input_large_file, 'r') as f:
#             inputInt_large = f.readline()
#         with open(expected_output_file, 'r') as ansfile:
#             expected_result_large = ansfile.readline().strip()
#         if str(count_primes_large(int(inputInt_large))) == expected_result_large:
#             print(f"{filename}: Test passed!,got {count_primes_large(int(inputInt_large))}.")
#             point += 1
#         else:
#             print(f"{filename}: Test failed. Expected {expected_result_large}, got "
#                   f"{count_primes_large(int(inputInt_large))}.")
#     else:
#         continue
# if point == 10:
#     print("All tests passed!")
