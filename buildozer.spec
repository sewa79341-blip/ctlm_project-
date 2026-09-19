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

      - name: Install Android/Build Dependencies
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
          python --version
          buildozer --version
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
