import os
import discord
import google.generativeai as genai
from dotenv import load_dotenv
import asyncio

# Load API keys dari file .env
load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Inisialisasi Client AI Gemini
genai.configure(api_key = GEMINI_API_KEY)

# Setup bot discord
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Game(name = "Ask me with !lux <your question>"))
    print(f'{bot.user.name} telah online!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('!lux'):
        prompt = message.content[len('!lux'):].strip()
        if not prompt:
            await message.channel.send("Silahkan berikan perintah setelah '!lux'")
            return
        
        # Cek pertanyaan khusus dulu
        if prompt in ["perkenalkan dirimu", "kamu siapa", "siapa kamu", "siapa kamu?"]:
            await message.channel.send("Aku Lux, AI yang awal tercipta untuk server Discord Ashura Heaven. ✨")
            return
        if prompt in ["Siapa yang menciptakanmu?", "siapa yang menciptakanmu?"]:
            await message.channel.send("Aku diciptakan oleh Muhammad Ikhsan Nur Rafid mahasiswa BINUS Bandung, dengan bantuan teknologi AI dari Google Gemini.")
            return
    
        loading = await message.channel.send("Aku sedang memproses permintaanmu, sebentar yah...")

        try:
            model = genai.GenerativeModel("gemini-2.5-flash")
            response = model.generate_content(prompt)
            full_text = response.text

            MAX_CHARS = 2000
            chunks = [full_text[i:i + MAX_CHARS] for i in range(0, len(full_text), MAX_CHARS)]

            await asyncio.sleep(2) # Delay biar ada teks loading
            await loading.edit(content = chunks[0])

            for chunk in chunks[1:]:
                await message.channel.send(chunk)

        except Exception as e:
            await loading.edit(content = f"Terjadi kesalahan: {e}")

bot.run(DISCORD_TOKEN)