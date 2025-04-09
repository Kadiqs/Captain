# 🏟️ Captin "Saudi World Cup Info Assistant"
---

## 📋 Features

- 🎙️ Voice-based interaction using text-to-speech (gTTS) (ongoing)
- 📍 Get stadium details (name, location, capacity, notes) (Done)
- 🎫 Ticket-related interactions with simulated QR prompt (Done)
- 🤖 Gemini-powered assistant for general World cup football-related queries
- 

---

## ⚙️ Requirements

- Python 3.7+
- pandas
- gTTS
- Google Generative AI SDK (`genai`)

Install dependencies:

```bash
pip install -r requirements.txt

```

---

## 🗂️ Files

- `stadiums_qatar.csv`: CSV file containing stadium info
- `stadium_facilities_qatar.csv`: CSV file with facilities by stadium
- `main.py`: The core application script


## 🔊 Text-to-Speech

Responses are converted to speech using `gTTS` and played using the system’s default media player.


---

## 🧪 Running the Assistant

From terminal:

```bash
python main.py
```

Then type your questions! Example prompts:
- `"Tell me about Lusail stadium"`
- `"What facilities are in Al Bayt stadium?"`
- `"Where is my seat?"`

---

## 📌 Notes

- Designed for a **Saudi-hosted World Cup**, with instructions customized for that context.
- Gemini is primed with a system message to stay concise and on-topic about football.

---

## 🛠️ To Do

- Integrate actual QR code scanner
- Add error handling for missing CSVs
- Support voice input (e.g., using `speech_recognition`)
- text to speech
"# Captain" 
