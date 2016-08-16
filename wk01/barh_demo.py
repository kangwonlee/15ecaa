# -*- coding: utf8 -*-
"""
Simple demo of a horizontal bar chart.
간단한 수평 막대 그래프 예제
"""
# TODO : citation

# matplotlib.pyplot 이라는 모듈에 그래프 관련 기능이 담겨 있음
# 해당 모듈의 기능을 사용하기 위해 plt 라는 이름으로 불러 옴
import matplotlib.pyplot as plt

# rc 관련 설정을 초기화 해 줌
plt.rcdefaults()

# 배열, 행렬 관련 기능을 담고 있는 numpy 모듈을 불러 들임
import numpy as np

# 그래프로 표시할 데이터 예
# y 축 : 사람 이름
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))

# x 축 : 성능
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

plt.barh(y_pos, performance, xerr=error, align='center', alpha=0.4)
plt.yticks(y_pos, people)
plt.xlabel('Performance')
plt.title('How fast do you want to go today?')

plt.show()
