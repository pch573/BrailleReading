from PIL import Image
import os, glob, numpy as np
import tensorflow as tf
tf.compat.v1.global_variables
import keras.backend.tensorflow_backend as K
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.models import load_model
# 찍은 사진 저장되는곳 사용하려면 꼭! 경로바꾸기
caltech_dir = 'C:\\Users\\cksgh\\Documents\\jol\\test'
image_w = 32
image_h = 64

pixels = image_h * image_w * 3

filenames = []
files = glob.glob(caltech_dir+"/*.*")
def stringmaker():
    X = []
    name = []
    for i, f in enumerate(files):
        img = Image.open(f)
        img = img.convert("RGB")
        img = img.resize((image_w, image_h))
        data = np.asarray(img)
        filenames.append(f)
        X.append(data)

    X = np.array(X)
    ##학습모델이 저장된 경로 사용할때 꼭! 경로바꾸기
    model = load_model('C:\\Users\\cksgh\\Documents\\jol\\model\\multi_img_classification.model')

    prediction = model.predict(X)
    np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
    cnt = 0

#이 비교는 그냥 파일들이 있으면 해당 파일과 비교. 카테고리와 함께 비교해서 진행하는 것은 _4 파일.

    for i in prediction:
        pre_ans = i.argmax()  # 예측 레이블
        print(i)
        print(pre_ans)
        pre_ans_str = ''
        if pre_ans == 0: pre_ans_str = "1"
        elif pre_ans == 1: pre_ans_str = "2"
        elif pre_ans == 2: pre_ans_str = "3"
        elif pre_ans == 3: pre_ans_str = "4"
        elif pre_ans == 4: pre_ans_str = "5"
        elif pre_ans == 5: pre_ans_str = "6"
        elif pre_ans == 6: pre_ans_str = "7"
        elif pre_ans == 7: pre_ans_str = "8"
        elif pre_ans == 8: pre_ans_str = "9"
        elif pre_ans == 9: pre_ans_str = "10"
        elif pre_ans == 10: pre_ans_str = "11"
        elif pre_ans == 11: pre_ans_str = "12"
        elif pre_ans == 12: pre_ans_str = "13"
        elif pre_ans == 13: pre_ans_str = "14"
        elif pre_ans == 14: pre_ans_str = "15"
        elif pre_ans == 15: pre_ans_str = "16"
        elif pre_ans == 16: pre_ans_str = "17"
        elif pre_ans == 17: pre_ans_str = "18"
        elif pre_ans == 18: pre_ans_str = "19"
        elif pre_ans == 19: pre_ans_str = "20"
        elif pre_ans == 20: pre_ans_str = "21"
        elif pre_ans == 21: pre_ans_str = "22"
        elif pre_ans == 22: pre_ans_str = "23"
        elif pre_ans == 23: pre_ans_str = "24"
        elif pre_ans == 24: pre_ans_str = "25"
        elif pre_ans == 25: pre_ans_str = "26"
        elif pre_ans == 26: pre_ans_str = "27"
        elif pre_ans == 27: pre_ans_str = "28"
        elif pre_ans == 28: pre_ans_str = "29"
        elif pre_ans == 29: pre_ans_str = "30"
        elif pre_ans == 30: pre_ans_str = "31"
        elif pre_ans == 31: pre_ans_str = "32"
        elif pre_ans == 32: pre_ans_str = "33"
        elif pre_ans == 33: pre_ans_str = "34"
        elif pre_ans == 34: pre_ans_str = "35"
        elif pre_ans == 35: pre_ans_str = "37"
        elif pre_ans == 36: pre_ans_str = "38"
        elif pre_ans == 37: pre_ans_str = "39"
        elif pre_ans == 38: pre_ans_str = "40"
        elif pre_ans == 39: pre_ans_str = "41"
        elif pre_ans == 40: pre_ans_str = "42"
        elif pre_ans == 41: pre_ans_str = "43"
        elif pre_ans == 42: pre_ans_str = "44"
        elif pre_ans == 43: pre_ans_str = "45"
        elif pre_ans == 44: pre_ans_str = "46"
        elif pre_ans == 45: pre_ans_str = "47"
        elif pre_ans == 46: pre_ans_str = "48"
        elif pre_ans == 47: pre_ans_str = "49"
        elif pre_ans == 48: pre_ans_str = "50"
        elif pre_ans == 49: pre_ans_str = "51"
        elif pre_ans == 50: pre_ans_str = "52"
        elif pre_ans == 51: pre_ans_str = "53"
        elif pre_ans == 52: pre_ans_str = "54"
        elif pre_ans == 53: pre_ans_str = "55"
        elif pre_ans == 54: pre_ans_str = "57"
        elif pre_ans == 55: pre_ans_str = "58"
        elif pre_ans == 56: pre_ans_str = "59"
        elif pre_ans == 57: pre_ans_str = "61"
        elif pre_ans == 58: pre_ans_str = "62"
        elif pre_ans == 59: pre_ans_str = "63"
        # print(i.argmax()) #얘가 레이블 [1. 0. 0.] 이런식으로 되어 있는 것을 숫자로 바꿔주는 것.
        # 즉 얘랑, 나중에 카테고.000 0.000 0.000 0.000 0.000 0.000 0.000 1.000
        # split("\\")[숫자]는 숫자에 해당경로중 파일이름까지의 \\갯수를 쓰면 파일이름으로 나오게함
        if i[0] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[1] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"으로 추정됩니다.")
        if i[2] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[3] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[4] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[5] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[6] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[7] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[8] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[9] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[10] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[11] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[12] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[13] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[14] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[15] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[16] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[17] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[18] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[19] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[20] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[21] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[22] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[23] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[24] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[25] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[26] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[27] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[28] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[29] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[30] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[31] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[32] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[33] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[34] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[35] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[36] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[37] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[38] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[39] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[40] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[41] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[42] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[43] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[44] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[45] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[46] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[47] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[48] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[49] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[50] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[51] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[52] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[53] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[54] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[55] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[56] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[57] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[58] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        if i[59] >= 0.8: print("해당 "+filenames[cnt].split("\\")[6]+"이미지는 "+pre_ans_str+"로 추정됩니다.")
        #각각 문자를 숫자로 바꿔서 배열에 append
        name.append(int(pre_ans_str))
        cnt += 1
    return name