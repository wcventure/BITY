#-*- encoding: UTF-8 -*-
#Neural Nets Can Learn Function Type Signatures From Binaries
#https://github.com/wcventure/EKLAVYA
import pickle

# Load the dictionary back from the pickle file.
pickle_file = open('gcc-32-O0-findutils-xargs.pkl', "r+b")
binary_info = pickle.load(pickle_file, encoding='latin1')

#Display the binary filename
print(binary_info["binary_filename"])
print('')

#Display the function
for eachFunction in binary_info["functions"]:
    
    if(binary_info["functions"][eachFunction]['args_type']==[]):
        pass
    else:
        print(eachFunction, end="()")
        for eachItem in binary_info["functions"][eachFunction]['args_type']:
            print('\t', end='')
            print(eachItem, end="\n")

print('')

'''
#Display the structures
print("Display Structures:")
for eachStruct in binary_info["structures"]:
    print(eachStruct, end=': ')
    print(binary_info["structures"][eachStruct])
print('')
'''
