#! python3
# random_quiz.py ランダムに問題と答えを並べ問題集と解答集をつくる

import random
import os

os.chdir(r"C:\Users\shira\Desktop\python\boring")

national_holiday = {"元日": "1月1日", "成人の日": "1月の第2月曜日", "建国記念の日": "2月11日", "天皇誕生日": "2月23日", "春分の日": "3月20日頃", "昭和の日": "4月29日", "憲法記念日": "5月3日", "みどりの日": "5月4日", "こどもの日": "5月5日", "海の日": "7月の第3月曜日", "山の日": "8月11日", "敬老の日": "9月の第3月曜日", "秋分の日": "9月23日頃", "スポーツの日": "10月の第2月曜日", "文化の日": "11月3日", "勤労感謝の日": "11月23日"}


for quiz_num in range(2):
    quiz_file = open("national_holiday_quiz{}.txt".format(quiz_num + 1), "w")
    answer_key_file = open("national_holiday_answers{}.txt".format(quiz_num + 1), "w")

    quiz_file.write("名前:\n\n日付:\n\n")
    quiz_file.write((" ")*15 + "国民の祝日クイズ (問題番号 {})".format(quiz_num + 1))
    quiz_file.write("\n\n")

    holiday = list(national_holiday.keys())
    random.shuffle(holiday)

    for question_num in range(len(holiday)):
        correct_answer = national_holiday[holiday[question_num]]
        wrong_answers = list(national_holiday.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

        quiz_file.write("{}. {}っていつだったっけ？\n".format(question_num + 1, holiday[question_num]))
        for i in range(4):
            quiz_file.write(" {}. {}\n".format("ABCD"[i], answer_options[i]))
        quiz_file.write("\n")

        answer_key_file.write("{}. {}\n".format(question_num + 1, "ABCD"[answer_options.index(correct_answer)]))

    quiz_file.close()
    answer_key_file.close()
