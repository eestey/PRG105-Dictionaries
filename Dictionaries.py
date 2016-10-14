holiday = dict()
print holiday

holiday = {'Christmas': 'December 25', 'Thanksgiving': 'November 24', 'Labor Day': 'September 4',
           'New Year Day': 'January 1'}
print holiday
# The order does not match what I put in


len(holiday)
print (len(holiday))
# len calculates the results of how many key value pairs there are in the function


if 'Labor Day' in holiday:
    print "True"
else:
    print "False"

if 'Independence Day' in holiday:
    print "True"
else:
    print "False"

vals = holiday.values()
'Thanksgiving' in vals
print vals


# 11.2 Looping and Dictionaries

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def print_hist(h):
    for a in h:
        print a, h[a]


h = histogram('little')
print_hist(h)


