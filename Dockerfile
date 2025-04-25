# Docker для локальной отладки, на случай если тесты крашатся в пайплайне
# Нужно собрать этот образ и запушить его на докерхаб, а потом запустить
# Команды:
# docker build -t <имя_образа>:<тег> . Пример: docker build -t myapp:latest .
# docker login
# docker push <ваш_логин>/<имя_образа>:<тег> . Пример: docker push myusername/myapp:latest
# docker run -d --name <имя_контейнера> <ваш_логин>/<имя_образа>:<тег>. Пример: docker run -d --name myapp-container myusername/myapp:latest


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
CMD ["pytest", "-n", "2", "--browser_name=chrome"]

