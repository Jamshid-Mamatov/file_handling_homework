def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    str_list=[]
    for character in data:
        if not character.isdigit():
            str_list.append(character)
    return str_list
    
# Read data from file

with open('txt_file\data04.txt','r') as f:
    fr=f.read()
    main(data=fr)