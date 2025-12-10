

#1] 별도의 .py에 변수 1개와 함수 1개를 만들어 사용해보기

import mymodule.module_a

print(mymodule.module_a.title)
mymodule.module_a.show()

#2] 모듈용 파일만 모아 놓은 폴더를 만들어 사용

import mymodule.module_b as mo

print(mo.title)
mo.show()

from mymodule import module_b
print(module_b.title)
module_b.show()


#3] 모듈 파일을 만들때 주의점 - 모듈을 파일을 import만 해도 그 파일안의 모둔 코드가 실행됨
import mymodule.module_c # 이 순간 모듈c의 파이썬 코드는 실행됨