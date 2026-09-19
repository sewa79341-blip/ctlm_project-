name: CI Build

on:
  push:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Install System Dependencies & Java
      run: |
        sudo dpkg --add-architecture i386
        sudo apt-get update
        sudo apt-get install -y \
          build-essential \
          git \
          python3-pip \
          python3-dev \
          ffmpeg \
          libsdl2-dev \
          libsdl2-image-dev \
          libsdl2-mixer-dev \
          libsdl2-ttf-dev \
          portaudio19-dev \
          libswscale-dev \
          libavformat-dev \
          libavcodec-dev \
          zlib1g-dev \
          openjdk-17-jdk \
          autoconf \
          libtool \
          pkg-config \
          libncurses5:i386 \
          libstdc++6:i386 \
          libz1:i386

    - name: Upgrade Pip & Install Buildozer/Cython
      run: |
        python -m pip install --upgrade pip
        pip install --upgrade cython buildozer

    - name: Verify Buildozer Setup
      run: |
        buildozer --version

    - name: Run Buildozer Debug (Verbose Mode)
      run: |
        buildozer -v android debug

    - name: Upload APK Artifact
      uses: actions/upload-artifact@v4
      with:
        name: package-apk
        path: bin/*.apk
