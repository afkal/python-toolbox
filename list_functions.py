### List utility functions

def filter_dict_list_with_values(key: str, valueList: list, targetList: list) -> list:
    '''
    Returns list of dicts that has key with matching value in value list
    Example:
    targetList = [{'type':'type1'},{'type':'type2'},{'type':'type2'}, {'type':'type3'}]
    valueList = ['type2','type3']
    key = 'type'
    -> resultList = [{'type': 'type2'}, {'type': 'type2'}, {'type': 'type3'}]
    Ref: https://stackoverflow.com/questions/29051573/python-filter-list-of-dictionaries-based-on-key-value
    '''
    resultList = [d for d in targetList if d[key] in valueList]
    return(resultList)