from tqdm import tqdm

if __name__ == '__main__':
    numeros = range(int(10e7))
    for i in tqdm(numeros, colour='blue', desc="Processando"):
        pass
