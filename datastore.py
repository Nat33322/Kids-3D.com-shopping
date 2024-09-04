from datetime import datetime

now = datetime.now()

current_time = now.strftime("%D:%H:%M:%S")
print("Current Time =", current_time)

message = "(name) wants (product. requested at {current_time}"

with open("datastore.txt","w") as f: #in write mode
    f.write("{name} wants {product}.".format(list))

with open("datastore.txt") as f: #in read mode, not in write mode, careful
    rd=f.readlines()
print (rd)
