print("Starting")
print("Creating files")
with open('monke.txt', 'w') as f:
    for x in range(200000000):
        f.write('monke ')
print("finished monke")