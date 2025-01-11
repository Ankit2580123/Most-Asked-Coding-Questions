#Filter the city name using endswith and startswith functions
def filter_out_city(list):
    ans=[]
    for item in list:
        if item.endswith('pur') or 'an' in item or item.startswith('Hy'):
            ans.append(item)

    return ans


city=['Nagpur','Kanpur','Ranchi','Dhanbad','Chandigarh','Hyderabad','Pune','Goa']

filtered=filter_out_city(city)
print(filtered)