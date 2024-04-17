FROM ubuntu22:python

RUN  apt-get update \
  && apt-get install -y \
  libgstreamer1.0-0 \
  gstreamer1.0-plugins-base \
  gstreamer1.0-plugins-good \
  gstreamer1.0-plugins-bad \
  gstreamer1.0-plugins-ugly \
  gstreamer1.0-tools \
  python3-gi \
  gir1.2-gstreamer-1.0 \
  libgstreamer-plugins-base1.0-dev \
  # Cleanup
  && rm -rf /var/lib/apt/lists/*  

RUN  apt-get update \
  && apt-get install -y \
    libgl1-mesa-glx \
    qtbase5-dev \
    libxcb-cursor0 \
  # Cleanup
  && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt