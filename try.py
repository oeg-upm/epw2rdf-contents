data = "GROUND TEMPERATURES,3,.5,,,,6.09,5.28,6.71,8.95,14.81,19.34,22.39,23.32,21.74,18.22,13.53,9.18,2,,,,9.06,7.62,7.91,9.10,13.03,16.57,19.41,20.93,20.61,18.61,15.38,11.95,4,,,,11.52,10.04,9.72,10.17,12.39,14.78,16.96,18.49,18.85,17.98,16.08,13.76"

def getGroundTemperatures(data):

    data = data.split(',')
    data.pop(0) # Remove first and second item
    data.pop(0) # Remove first and second item

    lists = [data[x:x+16] for x in range(0, len(data), 16)]

    for elem in lists:
        count = 0
        while count < len(elem):
            if elem[count] == "":
                elem[count] = "null"
            elif elem[count].startswith("."):
                elem[count] = "0"+elem[count]

            count+=1
        
    return lists

lists = getGroundTemperatures(data)

print(lists)