import json

def converter(path):
    try:
        file = open(path)
    except FileNotFoundError:
        print("File not found")
    except (ValueError,TypeError):
        print("JSON format error")
    file_read = file.read()
    print(type(file_read))
    file.close()
    file_data = json.loads(file_read)
    #print(file_data)
    #print(type(file_data[0]))
    temp = []
    for x in  file_data:
        temp.append(x)
        return temp

    #return(print(temp))


converter("2.json")
















