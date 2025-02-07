import operator

# write your code here

most_popular = sorted(student_list.items(), key=operator.itemgetter(1))[0][0]

print(most_popular)

