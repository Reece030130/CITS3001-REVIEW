def loudest(volume_list: list, sequence_list: list[str]) -> str:
    total_sound = []
    for seq in sequence_list:
        sound = 1
        for j in range(len(seq)):
            sound += int(volume_list[int(seq[j])])
        total_sound.append(sound)

    return sequence_list[total_sound.index(max(total_sound))]


if __name__ == '__main__':
    sequence = []
    count = input()
    volume = input().split()
    for i in range(int(count)):
        sequence.append(input())
    print(loudest(volume, sequence))



