def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
            print(f"created new instance of {class_}")
        return instances[class_]
    return getinstance