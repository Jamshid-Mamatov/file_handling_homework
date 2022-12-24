def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
    return [len(i) for i in data.split('\n')]
# Read data from file

with open('txt_file/data06.txt','r') as f:
    fr=f.read()
    main(data=fr)