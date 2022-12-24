def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """

    str_count=0
    dig_count=0

    for character in data:
        if character.isdigit():
            dig_count+=1
        else:
            str_count+=1
    
    return [dig_count,str_count]
# Read data from file

with open('txt_file/data05.txt','r') as f:
    rf=f.read()
    main(rf)