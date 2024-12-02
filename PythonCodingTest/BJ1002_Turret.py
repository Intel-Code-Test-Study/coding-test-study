#sys.stdin.readline() 사용하기 위해 sys import
import sys

# 케이스 수 T 입력받기
T = int(sys.stdin.readline())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    
    # 두 중심 좌표 사이의 거리 d 정의
    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    
    # 두 반지름의 차이 및 합
    dr = abs(r1 - r2)
    sr = r1 + r2

    # 두 원의 교점 개수 판별
    if d == 0 and r1 == r2:  # 두 원이 완전히 겹침
        print(-1)
    elif d == 0 and r1 != r2:  # 중심이 같지만 반지름이 다름
        print(0)
    elif d > sr:  # 두 원이 서로 떨어져 있음
        print(0)
    elif d == sr:  # 두 원이 외접
        print(1)
    elif d < sr and d > dr:  # 두 원이 두 점에서 만남
        print(2)
    elif d == dr and d != 0:  # 두 원이 내접
        print(1)
    elif d < dr:  # 한 원이 다른 원 내부에 있음 (교점 없음)
        print(0)