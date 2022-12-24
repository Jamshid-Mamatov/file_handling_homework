def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    num_list=[]
    for character in data:
        if character.isdigit():
            num_list.append(character)
    return num_list
# Read data from file
with open("txt_file\data03.txt",'r') as f:
    fr=f.read()
    main(data=fr)
   