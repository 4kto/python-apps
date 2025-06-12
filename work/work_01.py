import random
# １から１００でランダムな数字をNUMに覚えておく （正解の数字）
num = random.randint(1,100)
print(num)

# 何回挑戦したかの回数（カウント）を覚えておく変数を０で初期化
cnt = 0

# ５回繰り返す（０〜４の数字ごとにくりかえし）
for i in range(5):
  print(i)

  input_line = int(input("数字を入力してください:"))

  # 入力した回数をカウントアップ
  cnt = cnt + 1

  # 正解の数字かどうか
  if input_line == num:
    print("正解")
    break # ループから抜け出す
  else:
    print("不正解")

    if input_line < num:
      print("もっと大きい数字です")
      if num - input_line > 10:
        print("10以上大きいです")
      else:
        print()
print("正解は" + str(num))
print(str(cnt) + "回入力しました")
