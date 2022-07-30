def lonleyInteger(a):
    """Given an array of integers, 
        where all elements but one occur twice, 
        find the unique element.

    Args:
        a (_INTEGER_ARRAY_):  integer array
    Return:
        unique element
    """
    for a_item in set(a):
        if a.count(a_item) == 1:
            print(a_item)
        

lonleyInteger([1,2,3,4,3,2,1])