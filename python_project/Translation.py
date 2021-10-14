import hgtk
import jamo
import server
from unicode import join_jamos
import deeplearning
MATCH_B2H_CHO = {8: ['ㄱ'],
                 9: ['ㄴ'],
                 10: ['ㄷ'],
                 16: ['ㄹ'],
                 17: ['ㅁ'],
                 24: ['ㅂ'],
                 32: ['ㅅ'],
                 40: ['ㅈ'],
                 48: ['ㅊ'],
                 11: ['ㅋ'],
                 19: ['ㅌ'],
                 25: ['ㅍ'],
                 26: ['ㅎ'],
                 43:[], 7:[] #약어 '가'때문에 추가
                 }

MATCH_B2H_CHO_1 = {8: ['ㄲ'],
                  10: ['ㄸ'],
                   24: ['ㅃ'],
                   32: ['ㅆ'],
                   40: ['ㅉ']
                   }
#ㄲ = 32 if 8, ㄸ = 32 if 10, ㅃ = 32 if 24, ㅆ = 32 if 32, ㅉ = 32 if 40


MATCH_B2H_JOONG = {
    35: ['ㅏ'],
    28: ['ㅑ'],
    14: ['ㅓ'],
    49: ['ㅕ'],
    5: ['ㅗ'],
    44: ['ㅛ'],
    13: ['ㅜ'],
    41: ['ㅠ'],
    42: ['ㅡ'],
    21: ['ㅣ'],
    23: ['ㅐ'],
    29: ['ㅔ'],
    12: ['ㅖ'],
    39: ['ㅘ'],
    61: ['ㅚ'],
    15: ['ㅝ'],
    58: ['ㅢ']
}
MATCH_B2H_JOONG_1 ={
    28: ['ㅒ'],
    39: ['ㅙ'],
    15: ['ㅞ'],
    13: ['ㅟ']
}
#ㅒ= 28 if 23, ㅙ= 39 if 23, ㅞ=15 if 23, ㅟ= 13 if 23  자음과 다르게 앞이아닌 뒤에 23값이 공통적으로 붙음.
MATCH_B2H_JONG = {1: ['ㄱ'],
                  18: ['ㄴ'],
                  20: ['ㄷ'],
                  2: ['ㄹ'],
                  34: ['ㅁ'],
                  3: ['ㅂ'],
                  4: ['ㅅ'],
                  54: ['ㅇ'],
                  5: ['ㅈ'],
                  6: ['ㅊ'],
                  22: ['ㅋ'],
                  38: ['ㅌ'],
                  50: ['ㅍ'],
                  52: ['ㅎ'],
                  }

MATCH_B2H_JONG_1 = {1: ['ㄲ'],
                    4: ['ㄳ']
                    }
#ㄲ= 1 if 1 ㄳ= 1 if 4

MATCH_B2H_JONG_2 = {5: ['ㄵ'],
                    52: ['ㄶ']
                    }
#ㄵ= 18 if 5, ㄶ= 18 if 52

MATCH_B2H_JONG_3 = {1: ['ㄺ'],
                    34: ['ㄻ'],
                    3: ['ㄼ'],
                     4: ['ㄽ'],
                    38: ['ㄾ'],
                    50: ['ㄿ'],
                    52: ['ㅀ']
                    }
#ㄺ = 2 if 1, ㄻ = 2 if 34, ㄼ = 2 if 3, ㄽ= 2 if 4, ㄾ = 2 if 38, ㄿ = 2 if 50, ㅀ = 2 if 52

MATCH_B2H_JONG_4 = {4: ['ㅄ']
                   }
#ㅄ= 3 if 4

MATCH_B2H_JONG_5 = {12: ['ㅆ']}

MATCH_B2H_Simple_1 = {43: ['ㄱ', 'ㅏ'],
                      9: ['ㄴ', 'ㅏ'],
                      10: ['ㄷ', 'ㅏ'],
                      24: ['ㅂ', 'ㅏ'],
                      7: ['ㅅ', 'ㅏ'],
                      40: ['ㅈ', 'ㅏ'],
                      19: ['ㅌ', 'ㅏ'],
                      25: ['ㅍ', 'ㅏ'],
                      26: ['ㅎ', 'ㅏ'],
                      56: ['것']
}#'것'은 다음 리스트에 14가 나와야지 것이 형성됨 /// 56이랑 겹치는 것이 없어서 약어에 포함 // '가'형식으로 저장하면 종성이 붙지 않음


MATCH_B2H_Simple_2 ={57: ['ㅓㄱ'],
                     62: ['ㅓㄴ'],
                     30: ['ㅓㄹ'],
                     33: ['ㅕㄴ'],
                     51: ['ㅕㄹ'],
                     59: ['ㅕㅇ'],
                     45: ['ㅗㄱ'],
                     55: ['ㅗㄴ'],
                     63: ['ㅗㅇ'],
                     27: ['ㅜㄴ'],
                     47: ['ㅜㄹ',],
                     53: ['ㅡㄴ'],
                     46: ['ㅡㄹ'],
                     31: ['ㅣㄴ']
} #'울'이 49가 중성 'ㅕ'랑 겹침

MATCH_B2H_Simple_3 ={14: ['그래서'],
                     9: ['그러나'],
                     18: ['그러면'],
                     34: ['그러므로'],
                     29: ['그런데'],
                     35: ['그리고'],
                     49: ['그리하여']
}




'''
MATCH_B2H_ALPHABET = {
}
'''
#Test1= 초성, Test2= 중성, Test3=종성

test = stringmaker()#기계학습모델사용해서 문자열을 넘겨받음

# ㄱ쌍자음: 32 if 32, 16 ****** ㄴ쌍자음: 18 if 40, 11 ********* ㄹ 쌍자음: 16 if 32, 17, 48, 8, 25, 19, 11 ****** ㅂ 쌍자음: 48 if 8
result = []
for index, i in enumerate(test): #리스트 for문
    print(i) #리스트 값
    print(index) #리스트 순서

    if i == 1 and test[index+1] in MATCH_B2H_Simple_3: # 1 다음 Simple_3의 약어 변수에 맞는 값이 있으면 삽입
        result += MATCH_B2H_Simple_3[test[index+1]]
        del test[index + 1]

    elif i in MATCH_B2H_CHO: #초성일 때
        if i == 32 and test[index+1] in MATCH_B2H_CHO_1: #된소리일때
            print(MATCH_B2H_CHO_1[test[index+1]])
            result += MATCH_B2H_CHO_1[test[index+1]]
            del test[index+1] #확인하고 다시 읽는 것을 방지하기 위해 삭제

        elif test[index+1] in MATCH_B2H_CHO or test[index+1] in MATCH_B2H_JONG: # 초성다음에 중성이 오지 않을 때 //미완성
            result += MATCH_B2H_Simple_1[i]

        else:
            print(MATCH_B2H_CHO[i])
            result += MATCH_B2H_CHO[i]

    elif i in MATCH_B2H_JOONG: #중성
        if test[index+1] == 23 and test[index] in MATCH_B2H_JOONG:#중성 다음에 23이 나올경우 JOONG_1의 값 출력
            print(MATCH_B2H_JOONG_1[test[index]])
            result += MATCH_B2H_JOONG_1[test[index]]
            del test[index + 1]
        elif i == 12 and test[index-1] in MATCH_B2H_JOONG: #12일때 앞에 중성이면 ㅆ추가
            result += MATCH_B2H_JONG_5[test[index]]

        else:
            if index == 0 and MATCH_B2H_JONG: #'ㅏ' 'ㄴ'= 안 인덱스가 0일때 'ㅇ'추가
                result +='ㅇ'
            elif test[index-1] in MATCH_B2H_JONG or test[index-1] in MATCH_B2H_JOONG or test[index-1] in MATCH_B2H_Simple_2: #앞에 문자가 중성이나 종성으로 끝날때
                result +='ㅇ'


            print(MATCH_B2H_JOONG[i])
            result += MATCH_B2H_JOONG[i]

    elif i in MATCH_B2H_JONG: #종성
        if i == 1 and test[index+1] in MATCH_B2H_JONG_1:
            print(MATCH_B2H_JONG_1[test[index+1]])
            result += (MATCH_B2H_JONG_1[test[index+1]])
            del test[index + 1]

        elif i == 18 and test[index+1] in MATCH_B2H_JONG_2:
            print(MATCH_B2H_JONG_2[test[index+1]])
            result += (MATCH_B2H_JONG_2[test[index+1]])
            del test[index + 1]
        elif i == 2 and test[index+1] in MATCH_B2H_JONG_3:
            print(MATCH_B2H_JONG_3[test[index+1]])
            result += (MATCH_B2H_JONG_3[test[index+1]])
            del test[index + 1]
        elif i == 3 and test[index+1] in MATCH_B2H_JONG_4:
            print(MATCH_B2H_JONG_4[test[index+1]])
            result += (MATCH_B2H_JONG_4[test[index+1]])
            del test[index + 1]

        else:
            print(MATCH_B2H_JONG[i])
            result += (MATCH_B2H_JONG[i])

    elif i == 33: #아예 았 구분 문자 ex) 아예 ⠣⠤⠌, 았 ⠣⠌
        result += 'ㅇ'

    elif i in MATCH_B2H_Simple_2: #약어_2
        if test[index-1] not in MATCH_B2H_CHO:
            result += 'ㅇ'
            result += MATCH_B2H_Simple_2[i]

        else:
            result += MATCH_B2H_Simple_2[i]


print(test)# ㅇㅏㄴㄴㅕㅇ
print(result)
print(''.join(result))
com = ''.join(result) # List to str ㅇㅏㄴㄴㅕㅇ
Hangle = join_jamos(com)
print(Hangle) # str 한글로 합침 안녕하세요 과

