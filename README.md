# ✨ Lux AI — Discord-Bot Powered by Gemini AI

Lux AI adalah bot Discord cerdas yang dibangun menggunakan teknologi **Google Gemini (Generative AI)**. Dirancang awal untuk server **Ashura Heaven**, Lux AI hadir sebagai asisten interaktif yang mampu menjawab berbagai pertanyaan pengguna dalam bahasa natural.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square)
![Discord.py](https://img.shields.io/badge/discord.py-2.x-blueviolet?style=flat-square)
![Gemini API](https://img.shields.io/badge/Google%20Gemini-API-brightgreen?style=flat-square)

---

## 🧠 Fitur Utama

- 🎙️ Menjawab perintah pengguna melalui prompt `!lux`
- 💡 Terhubung ke **Gemini API** untuk menghasilkan jawaban berbasis AI
- 🔒 Aman melalui token environment `.env`
- 🧾 Support input panjang (otomatis dibagi per 2000 karakter)

---

## 🚀 Demo

Contoh penggunaan di server Discord:

```text
User: !lux Apa itu Linked List dan AVL Tree?
Lux AI: (Jawaban dari Gemini API akan muncul di sini dalam beberapa bagian jika panjang)
```

---

## 🛠️ Cara Menjalankan

### 1. Clone Repository
```
git clone https://github.com/username/lux-ai-discord-bot.git
cd lux-ai-discord-bot
```

### 2. Siapkan Environment
Buat file `.env` di root folder dengan isi:
```
GEMINI_API_KEY=your_google_gemini_api_key
DISCORD_TOKEN=your_discord_bot_token
```

> ❗ Tidak boleh ada spasi setelah tanda `=`.

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Jalankan Bot
```
python main.py
```

---

## 🧾 Struktur Project

```
lux-ai-discord-bot/
│
├── main.py              # Script utama bot
├── .env                 # File berisi token API (tidak diupload ke GitHub)
├── requirements.txt     # Daftar library yang dibutuhkan
└── README.md            # Dokumentasi ini
```
---

## 📚 Teknologi yang Digunakan

- [Python 3.11](https://www.python.org/)
- [discord.py](https://discordpy.readthedocs.io/en/stable/)
- [Google Generative AI (Gemini)](https://ai.google.dev/)
- [Replit](https://replit.com/)
- [UptimeRobot](https://uptimerobot.com/)

---

## 📄 Lisensi

MIT License © 2025 — [Ikhsaaan334](https://github.com/Ikhsaaan334)
