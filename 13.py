# Generate the the custom exception using Exception handling

def custom_exception():
    array=[1,2,3,5,6]
    try:
        array[8]=100
        print(array)
    except Exception as e:
        raise Exception(e)
        # print(e)
    else:
        print("Executed")
custom_exception()
