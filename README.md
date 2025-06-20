# Масштабируемая система автоматизации

Проект состоит из модулей, объединенных в проекты. Каждый проект автономен и может быть запущен независимо.
Команда для быстрого комита
'''
git commit -m "Auto-update"
'''

## Основные компоненты

- **core**: Общие модули (конфиг, БД, шина сообщений, AI-клиенты)
- **projects**: Проекты (project1_tg_bot, project2_future, project3_future)
- **ai_config**: Конфигурация AI (провайдеры, промпты)

## Проект 1: Telegram бот

Функционал:
1. Сбор новостей из различных источников
2. Улучшение контента с помощью AI
3. Публикация в Telegram канал

### Запуск

1. Скопируйте `.env.example` в `.env` и заполните настройки
2. Установите зависимости: `pip install -r requirements.txt`
3. Запустите основной скрипт: `python main.py`

### Настройка AI

Настройки AI находятся в `ai_config/providers.py`. По умолчанию используется YandexGPT.

Для смены провайдера:
```python
from ai_config.adapter import AIAdapter

adapter = AIAdapter()
adapter.switch_provider("openai")  # Переключение на OpenAI

