# 🤖 Claude Fable 5 Agent

> Мощный ИИ-агент на основе [Claude Fable 5](https://www.anthropic.com/claude/fable) для решения сложных, многоэтапных задач.

Claude Fable 5 — Mythos-класс модель Anthropic (релиз 9 июня 2026), доступная через API как `claude-fable-5`. Способна работать автономно часами и днями: планирует по этапам, делегирует подзадачи, проверяет собственную работу.

## 📁 Структура репозитория

```
claude-fable-5-agent/
│
├── agent/
│   ├── core.py          # Основной агент
│   ├── tools.py         # Инструменты агента (tool use)
│   ├── vision.py        # Компьютерное зрение
│   └── memory.py        # Долгосрочная память / контекст
│
├── workflows/
│   ├── coding.py        # Агентное программирование
│   ├── research.py      # Глубокие исследования
│   └── enterprise.py    # Корпоративные рабочие процессы
│
├── examples/
│   ├── code_migration.py
│   ├── document_analysis.py
│   └── multi_day_task.py
│
├── .env.example
├── requirements.txt
└── main.py
```

## 🚀 Быстрый старт

```bash
git clone https://github.com/ivanm696/claude-fable-5-agent.git
cd claude-fable-5-agent

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt

cp .env.example .env
# Открой .env и вставь свой ANTHROPIC_API_KEY

python main.py
```

## ✨ Возможности

| Возможность | Описание |
|---|---|
| 🧠 Многоэтапные задачи | Планирование, выполнение, самопроверка |
| 💻 Агентное кодирование | Код + тесты + ревью автоматически |
| 👁️ Компьютерное зрение | Анализ изображений, PDF, диаграмм |
| 🏢 Корпоративные процессы | Исследования, аналитика, документы |
| 💬 Долгосрочная память | Сохранение контекста между сессиями |

## ⚠️ Важные технические детали

- **Adaptive thinking всегда включено** — Fable 5 не поддерживает явное отключение через `thinking: {"type": "disabled"}` (вернёт ошибку 400). Параметр `thinking` просто не передаётся.
- **Safety classifiers** — запросы по кибербезопасности, биологии, химии и ядерной тематике автоматически перенаправляются на Opus 4.8 (`stop_reason: "refusal"`). `agent/core.py` обрабатывает это явно.
- **Стоимость** — $10 / млн входных токенов, $50 / млн выходных (вдвое дороже Opus 4.8). Используй `max_tokens` разумно.

## 🧪 Тесты

```bash
python -m pytest  # если добавишь тесты
# или быстрая проверка структуры:
python -c "from agent.core import ClaudeFable5Agent; print('OK')"
```

## License

MIT
