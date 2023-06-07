import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheetsにアクセスするための認証情報を設定
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('.\python\quiz_project\my-project-quiz-387002-b19414d48646.json', scope)
client = gspread.authorize(creds)

# スプレッドシートを開く
spreadsheet = client.open_by_key('13t1uzl_DD9OYahyHSGw67ogps23oVjJqYrwtW8fAN-0')
worksheet = spreadsheet.get_worksheet(0)

# 問題と解答をスプレッドシートに書き込む
def write_question_and_answer(question, answer):
    try:
        worksheet.append_row([question, answer])
    except gspread.exceptions.APIError as e:
        if e.response.status_code == 429:
            # クォータ制限によるエラーの場合、待機してから再試行する
            print("Quota exceeded. Waiting for 1 minute...")
            time.sleep(60)  # 60秒待機
            write_question_and_answer(question, answer)  # 再試行
        else:
            # クォータ制限以外のエラーはそのまま例外を発生させる
            raise e

# テキストファイルを読み込んで問題と解答をスプレッドシートに書き込む
def process_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        question = ''
        answer = ''
        for line in lines:
            line = line.strip()
            if line.startswith('Q.'):
                if question != '':
                    write_question_and_answer(question, answer)
                question = line[3:].strip()
            elif line.startswith('A.'):
                answer = line[3:].strip()
        # 最後の問題と解答を書き込む
        write_question_and_answer(question, answer)

# テキストファイルを指定して問題と解答をスプレッドシートに書き込む
text_file_path = '.\python\quiz_project\quiz_discord2.txt'  # テキストファイルのパスを指定
process_text_file(text_file_path)
