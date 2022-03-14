from google_trans_new import google_translator
from tqdm import tqdm
import time
tran = []

#t = Translator()
t = google_translator()
text = input("输入要生草内容(中文)>>> ")
#print("检测到"+ t.detect(text))
# for a in text:
#     tran_a.append(a)
print("共 " + str(len(text)) + " 个字符")
#print(tran_a)

print("正在生草...")
for i in tqdm(text , desc = "1/2"):
    #print(i)
    tran.append(t.translate(i,lang_tgt='en'))
    time.sleep(1)

print(tran)

text_grass = ""
for i in tqdm(tran , desc = "2/2"):
    #print(i)
    text_grass += (t.translate(i,lang_tgt='zh-cn').strip())
    time.sleep(1)

print("完成！结果：")
print(text_grass)
AAAAAAA = input("\n回车以关闭")