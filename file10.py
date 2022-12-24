def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    rows=data.split('\n')
    len_row=[]
    for subject in rows:
        len_row.append(len(subject))
    return max(len_row)
# Read data from file

with open('txt_file/data10.txt','r') as f:
    fr=f.read()
    main(data=fr)