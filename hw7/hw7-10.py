def make_request(keys, values):
    if len(keys) != len(values):
        return {}
    result_dict = {}
    for i in range(len(keys)):
      result_dict.update({keys[i] :values[i]})
    
    return result_dict