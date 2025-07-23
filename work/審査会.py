# ランダムな数字
import random


# カードを引く関数を定義
def draw_card():

    # 1から13までの数値（トランプのA〜K）をランダムに引く
    return random.randint(1, 13)


def hi_and_low_game():
    print("=== Hi and Low ゲームへようこそ！===")
    # 最初のカードを引く
    current_card = draw_card()

    # ループ
    while True:
        print(f"\n現在のカードは: {current_card}")
        guess = input("次のカードは High (H) か Low (L) か？（終了したい場合は Q）：")

        # ゲーム終了
        if guess == "Q":
            print("ゲームを終了します。お疲れ様でした！")
            break
        # 入力が間違っている時
        if guess not in ["H", "L"]:
            print("無効な入力です。'H' または 'L' を入力してください。")
            continue
        # 次のカードを引く
        next_card = draw_card()
        print(f"次のカードは: {next_card}")

        # 勝敗判定
        if next_card == current_card:
            print("同じ数字！今回は引き分けです。")
        elif (guess == "H" and next_card > current_card) or (
            guess == "L" and next_card < current_card
        ):
            print("正解！")
        else:
            print("不正解...")

        # カードの更新
        current_card = next_card


# 関数の呼び出し　実行
hi_and_low_game()



# Hi and low 

# def を使った関数の定義

# while ループ

# if文 条件分岐

# random モジュール

# input() でユーザーの入力を受け取る
