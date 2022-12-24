def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    numb_list=[]
    for i in data.split(','):
        numb_list.append(int(i))
    return numb_list
    
# Read data from file
with open("txt_file/data01.txt",'r') as f:
    rf=f.read()
    print(main(data=rf))
    

