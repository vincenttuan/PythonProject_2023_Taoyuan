import json
# 讀取 Json
json_str = '{"name": "John", "salary": 45000, "age": 25}'
emp = json.loads(json_str)  # 將 Json 字串轉為 dict 數組
# 進行分析/取值
print(emp, type(emp))
print(emp['name'])
print(emp['salary'])
print(emp['age'])
# 改變薪資
emp['salary'] = 88000
print(emp)
# 將 emp 數組轉 json 字串
json_str = json.dumps(emp)
print("json 字串 = {}".format(json_str))
