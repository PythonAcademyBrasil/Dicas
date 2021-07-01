import aiohttp
import asyncio
import time


# Função para buscar um Pokemon
async def busca_pokemon(session, url):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        return pokemon['name'], resp.content_length


async def main():
    inicio = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for number in range(1, 152):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.ensure_future(busca_pokemon(session, url)))

        # Dispara as requisições assíncronas
        respostas = await asyncio.gather(*tasks)

        # Itera sobre o retorno
        for pokemon, tamanho in respostas:
            print(f'Pokemon: {str(pokemon).capitalize()} ({tamanho} bytes)')

        total = sum([r[1] for r in respostas])
        tempo_total = time.time() - inicio
        print(f'\n\n{len(respostas)} Requisições e {total} bytes baixados em {tempo_total:.3f}s')

if __name__ == '__main__':
    asyncio.run(main())
