T = int(input()) # 첫째줄 
input_values = list(input().split() for _ in range(T)) #테스트케이스줄

for input_value in input_values: #하나의 테스트 케이스마다
    x1,y1,r1,x2,y2,r2 = list(map(int,input_value))

    dist = ((x2-x1)**2 + (y2 -y1)**2)**0.5 # 거리
    rs1 = r1 +r2 # 원이 바깥에 있을 때
    rs2 = abs(r1 - r2) # 원이 안에 있을 때
    
    if dist == 0 and r1 == r2: # 같은 원
        print(-1)
    elif rs1 < dist or rs2 > dist: # 바깥멀리 or 완전안
        print(0)
    elif dist in [rs1,rs2]: # 닿아있을때
        print(1)
    elif dist < rs1: # 겹쳐있을때 rs2나 rs1이나 똑같다
        print(2)
