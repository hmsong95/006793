#-----------------------------------------------------------------------
# day.py
#-----------------------------------------------------------------------

import stdio
import sys

# 월(m), 일(d), 년(y)을 명령 줄 인자로 받는다.
# 그레고리안력에 따라 m/d/y날의 요일을 출력한다.
# 0은 일요일, 1은 월요일...

m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

y0 = y - (14 - m) // 12
x = y0 + y0//4 - y0//100 + y0//400
m0 = m + 12 * ((14 - m) // 12) - 2
d0 = (d + x + (31*m0)//12) % 7

stdio.writeln(d0)

#-----------------------------------------------------------------------

# python day.py 8 2 1953
# 0

