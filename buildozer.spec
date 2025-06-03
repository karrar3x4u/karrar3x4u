name: Build APK

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Setup Python 3.10
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install system dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y \
            python3-pip git zip unzip openjdk-11-jdk \
            build-essential autoconf automake libtool m4 pkg-config zlib1g-dev \
            libffi-dev libssl-dev libc6-dev libsqlite3-dev libpng-dev libjpeg-dev

      - name: Set JAVA_HOME to JDK 11
        run: echo "JAVA_HOME=/usr/lib/jvm/temurin-11-jdk-amd64" >> $GITHUB_ENV

      - name: Upgrade Buildozer and dependencies
        run: |
          pip install --upgrade cython
          pip install --upgrade buildozer python-for-android

      - name: Patch buildozer.spec for StreamSanctum
        run: |
          cat > buildozer.spec <<EOF
[app]
title = StreamSanctum
package.name = streamsanctum
package.domain = org.saden
source.dir = .
source.include_exts = py,html
version = 0.1
requirements = python3, flask
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.private_storage = True
android.accept_sdk_license = True
android.accept_ndk_license = True
log_level = 2
android.requirements = python3, flask
android.enable_multi_touch = True
EOF

      - name: Build APK with Buildozer
        run: |
          buildozer android debug

      - name: Upload APK artifact
        uses: actions/upload-artifact@v4
        with:
          name: StreamSanctum-APK
          path: bin/*.apk
