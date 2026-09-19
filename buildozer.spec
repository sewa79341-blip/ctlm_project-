name: CI Build

on:
  push:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
    - name: Checkout Repository
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Install System Dependencies
      run: |
        export DEBIAN_FRONTEND=noninteractive
        sudo apt-get update -y
        sudo apt-get install -y \
          build-essential \
          git \
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
  name: CTLM APK Build

on:
  push:
    branches: ["main"]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      - name: Install System Dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y \
            build-essential \
            git \
            zip \
            unzip \
            openjdk-17-jdk \
            autoconf \
            automake \
            libtool \
            pkg-config \
            cmake \
            libffi-dev \
            libssl-dev \
            zlib1g-dev \
            libncurses5-dev \
            libncursesw5-dev

      - name: Install Python Build Tools
        run: |
          python -m pip install --upgrade pip
          python -m pip install --upgrade setuptools wheel
          python -m pip install "Cython<3"
          python -m pip install --upgrade buildozer

      - name: Verify Build Environment
        run: |
          echo "=== OS ==="
          cat /etc/os-release
          echo "=== Python ==="
          python --version
          echo "=== Buildozer ==="
          buildozer --version
          echo "=== Java ==="
          java -version

      - name: Build CTLM APK
        run: |
          buildozer -v android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: CTLM-APK
          path: bin/*.apk
          if-no-files-found: error
