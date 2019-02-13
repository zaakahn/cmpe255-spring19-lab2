def mean_num_friends(x):
    return(sum(x)/len(x))

def median_num_friends(x):
    l = len(x)
    m = l - 1
    # Even
    if l % 2 == 2:
        return (x[m] + x[m+1])/2
    # Odd
    else:
        return x[m]
        
num_friends=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]
print("mean=" + str(mean_num_friends(num_friends)))
print("median=" + str(median_num_friends(num_friends)))
