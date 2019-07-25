


def requestParse(req):
    reqString = req.decode()
    print(reqString)
    
    # fff = reqString.lstrip('b\'')
    # fff = fff.rstrip('\'')
    # fff = reqString[2:-1]
    
    # print(fff)
    array = reqString.split('\r')
    # print(array)
    dic = {} 
    dic['method'] = array[0]

    for obj in array:
        newObj = obj.split(':')
        if len(newObj) > 1:
            # print(obj)
            # print(newObj[0].strip())
            # print(newObj[1].strip())
            key = newObj[0].strip()
            value = newObj[1].strip()
            dic[key] = value

    array1 = array[len(array) - 1].split('&')
    body = {}
    for obj in array1:
        newObj = obj.split('=')
        if len(newObj) > 1:
            key = newObj[0].strip()
            value = newObj[1].strip()
            # print(key)
            body[key] = value

    dic['body'] = body
    print(dic)
    # print(dic['body']['firstname'])
    return dic

# requestParse(req)
