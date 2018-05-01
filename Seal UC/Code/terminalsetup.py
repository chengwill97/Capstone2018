import os

class_names = [x[1] for x in os.walk('./nn_images/training')][0]

print("prep_train START")
os.system('python3 prep_train.py')
print("prep_train END")

print("pt_train START")
os.system('python3 sealnet_nas_scalable.py')
print("pt_train END")