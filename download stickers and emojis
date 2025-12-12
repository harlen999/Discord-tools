# by harlen
# Keep the credits if you edit

import requests
import os
import aiohttp
import asyncio
import platform
import sys
import re

def limpar_tela():
    if platform.system()=="Windows":
        os.system("cls")
    else:
        os.system("clear")

def ng(name):
    return name.replace('/', '_').replace('\\', '_').replace(':', '_').replace('*', '_').replace('?', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_')

ASCII_ART = r"""
 █████   █████                     ████                                                 █████                      
░░███   ░░███                     ░░███                                                ░░███                       
 ░███    ░███   ██████   ████████  ░███   ██████  ████████       ██████  ████████      ███████    ██████  ████████ 
 ░███████████  ░░░░░███ ░░███░░███ ░███  ███░░███░░███░░███     ███░░███░░███░░███    ░░░███░    ███░░███░░███░░███
 ░███░░░░░███   ███████  ░███ ░░░  ░███ ░███████  ░███ ░███    ░███ ░███ ░███ ░███      ░███    ░███ ░███ ░███ ░███
 ░███    ░███  ███░░███  ░███      ░███ ░███░░░   ░███ ░███    ░███ ░███ ░███ ░███      ░███ ███░███ ░███ ░███ ░███
 █████   █████░░████████ █████     █████░░██████  ████ █████   ░░██████  ████ █████     ░░█████ ░░██████  ░███████ 
░░░░░   ░░░░░  ░░░░░░░░ ░░░░░     ░░░░░  ░░░░░░  ░░░░ ░░░░░     ░░░░░░  ░░░░ ░░░░░       ░░░░░   ░░░░░░   ░███░░░  
"""

limpar_tela()
print(ASCII_ART)

TOKEN=input("\nSeu TOKEN: ").strip()
limpar_tela()
print(ASCII_ART)

server_id = int(input("\nID do server: ").strip())
limpar_tela()
print(ASCII_ART)

pasta_downloads = os.path.join(os.path.expanduser("~"), "Downloads")
pasta_servidor = os.path.join(pasta_downloads, f"Servidor extraido ({server_id})")
pasta_emojis = os.path.join(pasta_servidor, "emojis")
pasta_stickers = os.path.join(pasta_servidor, "stickers")

for pasta in (pasta_servidor, pasta_emojis, pasta_stickers):
    os.makedirs(pasta, exist_ok=True)


async def baixar_arquivo(url, nome_arquivo, pasta, atual, total):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status==200:
                caminho = os.path.join(pasta, nome_arquivo)

                if os.path.exists(caminho):
                    base, ext = os.path.splitext(nome_arquivo)
                    nome_arquivo = f"{base}_dup{ext}"
                    caminho = os.path.join(pasta, nome_arquivo)
                    
                with open(caminho, 'wb') as f:
                    f.write(await resp.read())

                sys.stdout.write(f"\r[{atual}/{total}] Baixando: {nome_arquivo}      ")
                sys.stdout.flush()
            else:
                sys.stdout.write(f"\rErro ao baixar {nome_arquivo}: status {resp.status}")
                sys.stdout.flush()

class DiscordAPI:
    def __init__(self, token):
        self.base_url = "https://discord.com/api/v9"
        self.headers = {
            "Authorization": token,
            "User-Agent": "Mozilla/5.0"
        }

    def pegar_emojis(self, guild_id):
        url = f"{self.base_url}/guilds/{guild_id}/emojis"
        r = requests.get(url, headers=self.headers)
        return r.json()

    def pegar_stickers(self, guild_id):
        url = f"{self.base_url}/guilds/{guild_id}/stickers"
        r = requests.get(url, headers=self.headers)
        return r.json()


async def main():
    api = DiscordAPI(TOKEN)

    emojis = api.pegar_emojis(server_id)
    
    if isinstance(emojis, list) and len(emojis)>0:
        total = len(emojis)
        for i, emoji in enumerate(emojis, start=1):
            if emoji.get("animated"):
                ext = "gif"
            else:
                ext = "png"
                
            url_emoji = f"https://cdn.discordapp.com/emojis/{emoji['id']}.{ext}"
            arquivo = f"{ng(emoji['name'])}.{ext}"
            await baixar_arquivo(url_emoji, arquivo, pasta_emojis, i, total)
            
        print("\n")

    stickers = api.pegar_stickers(server_id)
    
    if isinstance(stickers, list) and len(stickers)>0:
        total = len(stickers)
        for i, sticker in enumerate(stickers, start=1):
            sticker_id = sticker.get("id")
            nome = sticker.get("name", f"sticker_{sticker_id}")
            formato = sticker.get("format_type", 1)

            if formato==1:
                ext = "png"
            elif formato==2:
                ext = "png"
            elif formato==3:
                ext = "json"
            elif formato==4:
                ext = "gif"
            else:
                ext = "dat"

            url_sticker = f"https://media.discordapp.net/stickers/{sticker_id}.{ext}"
            arquivo = f"{ng(nome)}.{ext}"
            await baixar_arquivo(url_sticker, arquivo, pasta_stickers, i, total)
            
        print("\n")

if __name__ == "__main__":
    asyncio.run(main())
