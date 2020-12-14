#PUT actionqueue help code here

class DPActionQueue():
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)


def _format_action_results(dict_):
    dp_objects = []
    for key, value in dict_.items():
        if key != '_links' and key != '_embedded':
            app_dict = { key : value }
            dp_objects.append(app_dict)
    if '_embedded' in dict_.keys():
        for dp_object in dict_['_embedded']['descendants']:
            dp_objects.append(dp_object)
    _scrub(dp_objects, 'href')
    _scrub(dp_objects, '_links')
    return dp_objects


def _scrub(obj, bad_key):
    """
    Removes specified key from the dictioary in place.
    :param obj: dict, dictionary from DataPowers get object config rest call
    :param bad_key: str, key to remove from the dictionary
    """
    if isinstance(obj, dict):
        for key in list(obj.keys()):
            if key == bad_key:
                del obj[key]
            else:
                _scrub(obj[key], bad_key)
    elif isinstance(obj, list):
        for i in reversed(range(len(obj))):
            if obj[i] == bad_key:
                del obj[i]
            else:
                _scrub(obj[i], bad_key)
    else:
        # neither a dict nor a list, do nothing
        pass