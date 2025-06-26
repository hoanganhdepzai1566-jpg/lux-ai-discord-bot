# ✨ Lux AI — Discord-Bot Powered by Gemini AI

Lux AI adalah bot Discord cerdas yang dibangun menggunakan teknologi **Google Gemini (Generative AI)**. Dirancang awal untuk server **Ashura Heaven**, Lux AI hadir sebagai asisten interaktif yang mampu menjawab berbagai pertanyaan pengguna dalam bahasa natural.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square)
![Discord.py](https://img.shields.io/badge/discord.py-2.x-blueviolet?style=flat-square)
![Gemini API](https://img.shields.io/badge/Google%20Gemini-API-brightgreen?style=flat-square)
![Status](https://img.shields.io/badge/status-online-brightgreen?style=flat-square)

---

## 🧠 Fitur Utama

- 🎙️ Menjawab perintah pengguna melalui prompt `!lux`
- 💡 Terhubung ke **Gemini API** untuk menghasilkan jawaban berbasis AI
- 🔒 Aman melalui token environment `.env`
- 🌐 Online 24/7 via Replit + UptimeRobot
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
```bash
git clone https://github.com/username/lux-ai-discord-bot.git
cd lux-ai-discord-bot
```

### 2. Siapkan Environment
Buat file `.env` di root folder dengan isi:
```env
GEMINI_API_KEY=your_google_gemini_api_key
DISCORD_TOKEN=your_discord_bot_token
```

> ❗ Tidak boleh ada spasi setelah tanda `=`.

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Jalankan Bot
```bash
python main.py
```

---

## 🧾 Struktur Project

```
lux-ai-discord-bot/
│
├── main.py              # Script utama bot
├── keep_alive.py        # Flask server untuk menjaga uptime di Replit
├── .env                 # File berisi token API (tidak diupload ke GitHub)
├── requirements.txt     # Daftar library yang dibutuhkan
└── README.md            # Dokumentasi ini
```

---

## 🌐 Deployment Online (Opsional)

### Menggunakan Replit + UptimeRobot

1. Upload seluruh file ke [https://replit.com](https://replit.com)
2. Tambahkan file `keep_alive.py` dan panggil `keep_alive()` di `main.py`
3. Jalankan project dan pastikan muncul URL publik `.repl.co`
4. Daftarkan URL tersebut di [https://uptimerobot.com](https://uptimerobot.com) sebagai monitor setiap 5 menit.

---

## 📚 Teknologi yang Digunakan

- [Python 3.11](https://www.python.org/)
- [discord.py](https://discordpy.readthedocs.io/en/stable/)
- [Google Generative AI (Gemini)](https://ai.google.dev/)
- [Replit](https://replit.com/)
- [UptimeRobot](https://uptimerobot.com/)

---

## 🙌 Kontribusi

Pull request dan masukan sangat terbuka! Jangan ragu untuk fork project ini dan menambahkan fitur baru.

---

## 📄 Lisensi

MIT License © 2025 — [YourName](https://github.com/yourusername)
