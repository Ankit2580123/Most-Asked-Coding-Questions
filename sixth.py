# Count the occurrences of each character in a string.
# Find the key with the maximum value in a dictionary.
def string_occurrence(str):
    freq={}

    for i in str:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq 

freq_count=string_occurrence("geeksforgeeks")

max_occ=0
for key,value in freq_count.items():
    if value>max_occ:
        max_occ=value
        max_key=key
print("Maximum occurrence character:",max_key,"Counts:",max_occ)
   
