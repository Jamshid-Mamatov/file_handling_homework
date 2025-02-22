def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    objects=data.split('\n')
    list_object=[]
    numbers=[]
    for i in objects:
        list_object.append(i.split(' '))
    for i in list_object:
        numbers.append(i[1].split('.'))
    

    min=int(numbers[0][0])
    for number in numbers:
        if min<int(number[0]):
            min=int(number[0])
    return min

# Read data from file

with open("txt_file/data08.txt",'r') as f:
    fr=f.read()
    print(main(data=fr))