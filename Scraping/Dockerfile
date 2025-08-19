FROM python:3.8.10-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install necessary dependencies for Firefox and wget
RUN apt-get update && apt-get install -y wget bzip2

# Install Firefox ESR (Extended Support Release)
RUN apt-get install -y firefox-esr

# Determine the latest GeckoDriver version compatible with Firefox ESR
# (This step requires an internet connection during image build)
RUN apt-get install -y jq
# RUN apt-get install -y firefox
# RUN GECKODRIVER_VERSION=$(curl -s https://www.selenium.dev/downloads/ | jq -r '.browsers."firefox"[-1].version') && \
#     echo "GeckoDriver version: ${GECKODRIVER_VERSION}"

# RUN GECKODRIVER_VERSION=$(curl -s https://www.selenium.dev/ শাহ/api/v3/versions/geckodriver | jq -r '.browsers."firefox"[-1].version') && \
#     echo "GeckoDriver version: ${GECKODRIVER_VERSION}"

# # Download and install GeckoDriver
# RUN wget -q -O /tmp/geckodriver.tar.gz "https://github.com/mozilla/geckodriver/releases/download/${GECKODRIVER_VERSION}/geckodriver-${GECKODRIVER_VERSION}-linux64.tar.gz"
# RUN tar -xvzf /tmp/geckodriver.tar.gz -C /opt/
# RUN chmod +x /opt/geckodriver
# RUN ln -s /opt/geckodriver /usr/local/bin/geckodriver

COPY . .

CMD ["python", "main.py"]