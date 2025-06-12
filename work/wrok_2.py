import random 
import time

byousuu = random.randint(3, 5) 
print(f"待つ秒数: {byousuu}秒")

time.sleep(byousuu)

start_time = time.time()
print(f"開始時刻: {start_time}")

print("!!!!!")
input("エンターキーを押してください:")
end_time = time.time()
print(f"終了時刻: {end_time}")

kakatta_byousuu = end_time - start_time
print(f"かかった時間: {kakatta_byousuu}秒")

if kakatta_byousuu < 0.01:
  print("不正")

print("エンターキーが押されました。")
