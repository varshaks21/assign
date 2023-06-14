import json
f = open("sample_data.json","r")
data = json.load(f)
parameter=data["parametersList"]
for parametersList in parameter:
    val = parametersList["parameterName"]
    print("ParameterName:",val)
    val1 = parametersList["min"]
    print("min_value:",val1)
    val2 = parametersList["max"]
    print("max_value:",val2)
    val3 = parametersList["avg"]
    print("avg_value:",val3)