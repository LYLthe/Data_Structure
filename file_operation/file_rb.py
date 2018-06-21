import pickle
lyst = []
with open('item.dat', 'rb') as f:
    while True:
        try:
            item = pickle.load(f)
            lyst.append(item)
        except EOFError:
            break
print(lyst)
