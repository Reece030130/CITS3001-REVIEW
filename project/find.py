def find(answers: str, correct_answer: str) -> int:
    dp_table = []
    point = 0
    max_points = 0
    for index, _ in enumerate(answers):
        if correct_answer[index] != answers[index]:
            if (answers[index], correct_answer[index]) not in dp_table:
                points = 0
                for i, _ in enumerate(answers):
                    if answers[index] == answers[i]:
                        if correct_answer[index] == correct_answer[i]:
                            points += 1
                    elif answers[i] == correct_answer[i]:
                        points += 1
                dp_table.append((answers[index], correct_answer[index]))
                max_points = max(max_points, points)
        else:
            point += 1

    return max(point, max_points)


if __name__ == '__main__':
    a = int(input())
    b = input()
    c = input()
    print(find(b, c))
