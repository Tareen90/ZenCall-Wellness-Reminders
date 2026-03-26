# ZenCall: Personal Wellness Voice Assistant 🚀

ZenCall is a specialized productivity and health tool designed to break the "screen trance" and help users maintain healthy habits through automated, interactive voice reminders.

## 🌟 Why ZenCall?
Standard mobile notifications are often ignored or silenced. A phone call is a high-priority interrupt that ensures the user actually performs the healthy habit (e.g., hydrating, stretching, or eye-rest).

## 🛠 Features
- **Smart Scheduling:** Users set their routine (e.g., Every 2 hours for water).
- **Interactive IVR (Twilio Gather):** Users can press '1' to confirm they completed the task.
- **Multilingual Support:** High-quality TTS in Arabic and English using Twilio's 'Alice' voice.
- **Progress Tracking:** Logs successful completions to provide weekly health insights.

## 🏗 Tech Stack
- **Backend:** Python (FastAPI / Flask)
- **Voice API:** Twilio Programmable Voice
- **Task Queue:** Celery with Redis (for scheduling)
- **Database:** PostgreSQL

## 🔒 Compliance & Safety
- **Strict Opt-in:** Calls are only made to users who explicitly verify their numbers and set a schedule.
- **No Marketing:** This is a utility service, not a telemarketing or promotional tool.
- **User Control:** Users can pause or cancel reminders instantly via the dashboard.
-
