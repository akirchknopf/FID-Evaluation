import numpy as np

from sklearn.metrics import accuracy_score

def checkDataframe(df, batch_size):
    if (len(df) % batch_size) != 0:
        rest = len(df) % batch_size
        df = df[:(len(df)-rest)]
        print(f"Warning: Needed to remove {rest} elements to make it matching from dataframe")
        return df
    else:
        return df
    
    
def loadMeanFromFile(pathToConfigFile, verbose=False):
    f = open(pathToConfigFile, "r")
    txtRaw = f.readline()
    if verbose:
        print(f'Raw string: {txtRaw}')
    txtRaw = txtRaw.replace("[", '')
    txtRaw = txtRaw.replace("]", '')
    txtRaw = txtRaw.split(' ')
    if verbose:
        print(f'Spitted string: {txtRaw}')
    R = float(txtRaw[0])
    G = float(txtRaw[1])
    B = float(txtRaw[2])
    meansOfDataset = np.array([R, G, B])
    return (meansOfDataset)

def convertRowToDictionary(row, columns, hasIndex = False):
    dict = {}
    for idx, col in enumerate(columns):
        if hasIndex:
            dict['index'] = row[idx]
        dict[col] = row[idx + 1]
    return dict

def calcAccTextModel(model, data_x, data_y, name, GLOBAL_BATCH_SIZE):
    test = model.predict(data_x, use_multiprocessing=False, batch_size = GLOBAL_BATCH_SIZE, verbose=1)
    test_max = np.argmax(test,axis=1)
    unique_elements, counts_elements = np.unique(test_max, return_counts=True)
    y_true = []
    for index, element in enumerate(data_y):
        y_true.append(element)
    y_true = [int(i) for i in y_true]

    acc = accuracy_score(np.array(y_true), np.array(test_max))

    print(f'{name} Accuracy is {acc}')
    return f'{name} Accuracy is {acc}'