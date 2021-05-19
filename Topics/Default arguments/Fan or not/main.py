def add_viewer(name, fan_list=None):
    if fan_list is None:
        return [name]
    else:
        fan_list.append(name)
        return fan_list
