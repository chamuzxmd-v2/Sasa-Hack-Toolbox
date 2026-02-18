#!/bin/bash

pkg update -y
pkg install python git -y
pip install colorama

chmod +x main.py
cp main.py $PREFIX/bin/sasa-dark
chmod +x $PREFIX/bin/sasa-dark

echo ""
echo "✅ Installed!"
echo "Type: sasa-hacker"
