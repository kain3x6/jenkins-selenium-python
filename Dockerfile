FROM python:3.11-slim

# Обновление и установка зависимостей
RUN apt-get update && apt-get install -y \
    chromium chromium-driver \
    curl unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Установка переменных окружения для Selenium
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Копирование зависимостей и установка
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование всего проекта
WORKDIR /app
COPY . .

# Команда по умолчанию (можно поменять на свою)
CMD ["pytest", "--browser_name=chrome"]
