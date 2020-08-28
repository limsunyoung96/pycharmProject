# salary 가장 큰 직원을 찾고
# id, name, salary 출력

from openpyxl import load_workbook

# data_only=True로 해줘야 수식이 아닌 값으로 받아온다
load_wb = load_workbook("emp.xlsx", data_only=True)

# 시트 이름으로 불러오기
load_ws = load_wb['sheet1']
info = {}

for col in load_ws.columns:
    row_value = []
    for cell in col:
        row_value.append(cell.value)

    strKey = row_value.pop(0)
    info[strKey] = row_value
    """if(strKey=='SALARY'):
        info[strKey] = map(int, row_value)
    else:
        info[strKey] = row_value"""

maxSal = 0

for sal in info.get('SALARY'):
    if sal != "":
        if maxSal < int(sal):
            maxSal = int(sal)

# print("최고 salary: ", maxSal)

# print(info.get('SALARY').index(maxSal))
indx = info.get('SALARY').index(maxSal)
for k in info:
    print(k, ':', info.get(k)[indx])

# print(info)
