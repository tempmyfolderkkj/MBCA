
#1. error(오류) - 문법적으로 문제가 있어서 처음부터 실행조차 불가능한 문제
#2. exception(예외) - 실행은 가능하지만 실행 중(RunTime) 문제 발생

print("예외처리에 대해 알아봅니다")

#1) error인 경우
# 10 = a # 실행시 error 발생
# 해결방법은 문법에 맞게 코드를 수정

#2) exception(예외)인 상황
print(10 / 0) # 산수연산에서 0 나눗셈은 불가능한 연산

#예외가 발생하면 프로그램 다운
# [예외처리]라는 것은 예외가 발생하더라도
# 예외가 발생해도 앱이 다운되지 않게 하는 문법

#3. 다른 자료형의 연산[숫자 + 문자
try:
    print(10 + '5')
except:
    print('문자와 숫자는 연산이 불가능')

#4. 바꿀 수 없는 자료형으로 형변환 시도
try:
    print(10 + int('3.14'))
except:
    print('정수모양의 문자열만 int로 변환 가능')

# 결국 예외처리라는 것은 예외가 발생되지 않도록 하는 것이 아니라, 예외가 발생해도 다운되지 않도록 하는 기술

#3 코드의 가독성을 위해 등장한 else 영역 추가
# 예외가 발생하지 않았을때 수행할 작업을 try 영역안에 모아서 쓰는 것이 가독성이 떨어진다고 봐서 등장한 문법

#try 구문으로만 처리
try:
    # 예외발생 가능성이 있는 코드
    number = int(input('정수 입력 : '))

    print(number ** 2)
except:
    print('정수만 입력하세요')


#try 영역안에 모든 성공코드를 작성하지않고 예외발생 가능성 코드만 try영역에 예외가 아닐때(성공했을때) 수행할 코드를 다른 영역에 작성하여 가독성 향상 - else
try:
    # 예외발생 가능성이 있는 코드
    number = int(input('정수 입력 : '))

except:
    print('정수만 입력하세요')

else:
    print(number ** 2)

#4) 예외발생 여부와 상관없이 무조건 수행할 작업이 있다면 사용하는 finally
# 파일 읽기 작업중 작업 중 예외발생, close()의 미스
try:
    file = open("files/aaa.txr", 'r', encoding='utf-8')
    print(file.read())
    
except:
    print('파일 읽기 작업중에 오류가 발생')

finally:
    file.close()

#5) 예외가 발생했을때 그 이유를 알고싶다면
try:
    print(10 / 0)
except Exception as e: # Exception 예외 객체 사용 및 e라는 이름의 변수로 참조하여 제어
    print('에러 발생')
    print('에러 종류 :', type(e))
    print('에러 이유 :', e)

try:
    aaa = [10, 20, 30]
    print(aaa[3])

except Exception as e: # Exception 예외 객체 사용 및 e라는 이름의 변수로 참조하여 제어
    print('에러 발생')
    print('에러 종류 :', type(e))
    print('에러 이유 :', e)

# 이런식으로 에러의 종류를 알수 있다면 에러별로 대응하는 코드가 가능함
#6) try영역안에 2개 이상의 에러가 발생할 가능성이 있는 경우도 존재함
try:
    num1 = int(input('입력 : '))
    num2 = int(input('입력 : '))

    div = num1 / num2

    print("나눗셈 결과 :", div)

except ValueError as e:
    print("숫자만 입력하세요 :", e)
except ZeroDivisionError as e:
    print("0 나눗셈 불가능 :", e)
except Exception as e:
    print("알수 없는 예외가 발생 :", e)

# [추가] raise - 예외 상황이 아닌데 개발자가 강제로 예외로 문제를 발생시키는 문법
#예) 원래 파이썬은 계산의 결과가 음수라고 해서 예외는 아님
num = int(input('number : '))

if num < 0:
    raise Exception

else:
    print(num)

# 예외처리로 위 음수값에 대한 예외를 처리해보기
try:
    num = int(input('number : '))

    if num < 0:
        raise Exception

    else:
        print(num)

except:
    print('양수만 입력')

# exception(예외)가 발생하면 그 줄 다음부터의 코드는 실행되지 않음
print('-' * 30)
print('프로그램 종료')























