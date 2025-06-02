FROM python:3.9-slim
# Install system dependencies required by Playwright
RUN apt-get update && apt-get install -y \
   wget gnupg libnss3 libatk-bridge2.0-0 libxss1 libasound2 \
   libxcomposite1 libxrandr2 libgtk-3-0 libgbm-dev libxdamage1 libx11-xcb1 \
&& apt-get clean
WORKDIR /app
COPY . /app
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Install Playwright and its browser binaries
RUN python -m playwright install --with-deps
EXPOSE 5000
CMD ["python", "app.py"]
