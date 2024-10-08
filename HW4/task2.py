import csv

def read_csv(file_path):
    students = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for row in reader:
            students.append(row)
    return students

def add_exam_scores(students):
    for student in students:
        while True:
            try:
                exam_score = float(input(f"Введіть бал за іспит для {student[0]}: "))
                if 0 <= exam_score <= 50:
                    student.append(exam_score)
                    break
                else:
                    print("Бал має бути між 0 і 50.")
            except ValueError:
                print("Будь ласка, введіть число.")

def calculate_final_scores(students):
    final_scores = []
    for student in students:
        name = student[0]
        practicals = student[1:6]
        exam = student[6]
        practical_scores = [0 if score == 'п'
                            else int(score) for score in practicals]
        total_score = sum(practical_scores) + exam
        absences = practical_scores.count(0)

        final_scores.append([name, *practical_scores, exam, total_score, absences])

    return final_scores

def write_final_scores(file_path, final_scores):
    header = ["Ім'я", "Практика 1", "Практика 2", "Практика 3", "Практика 4", "Практика 5", "Іспит", "Підсумок",
              "Пропуски"]
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(final_scores)


def sort_key(student):
    total_score = student[7]
    absences = student[8]
    return (-total_score, absences)

def rank_students(final_scores, rank_file_path):
    ranked_students = sorted(final_scores, key=sort_key)

    with open(rank_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        header = ["Ім'я", "Практика 1", "Практика 2", "Практика 3", "Практика 4", "Практика 5", "Іспит", "Підсумок",
                  "Пропуски"]
        writer.writerow(header)
        writer.writerows(ranked_students)

if __name__ == "__main__":
    input_file = "students.csv"
    final_scores_file = "final_scores.csv"
    ranking_file = "ranking.csv"

    students = read_csv(input_file)

    add_exam_scores(students)

    final_scores = calculate_final_scores(students)

    write_final_scores(final_scores_file, final_scores)

    rank_students(final_scores, ranking_file)

    print("Роботу завершено. Підсумки і рейтинг записані у файли.")
