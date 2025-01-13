import pandas as pd
#sort the dictionary based on values of keys
dicts={
    'a':1,
    'b':5,
    'c':2,
    'd':10
}

#approach 1-->use pandas library
series=pd.Series(dicts)
sorted_series=series.sort_values()

new_dict=sorted_series.to_dict()
print(new_dict)

#approach 2-->use sorted and Lambda function
print(dicts.items())
ans1=dict(sorted(dicts.items(),key=lambda x: x[1]))  #sort on the basis of values
print(ans1)
ans2=dict(sorted(dicts.items(),key=lambda x: x[0]))  #sort on the basis of keys
print(ans2)

