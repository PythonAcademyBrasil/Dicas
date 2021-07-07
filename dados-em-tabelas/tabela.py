from tabulate import tabulate

cabecalho = ["Planeta", "Raio (km)", "Massa (x 10^21 kg)"]
tabela = [
    ["Sol", 696000, 1989100000],
    ["Mercúrio", 2439, 330],
    ["Vênus", 6051, 641],
    ["Terra", 6371, 5973.6],
    ["Marte", 3390, 641.85],
    ["Júpiter", 69911, 1898600],
    ["Saturno", 58232, 568460],
    ["Urano", 25362, 86832],
    ["Netuno", 24622, 102430],
]

print(tabulate(tabela, headers=cabecalho, tablefmt="fancy_grid"))


