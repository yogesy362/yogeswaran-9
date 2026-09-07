#!/bin/bash

echo "======================================"
echo " CSS Selector Assignment Autograder"
echo "======================================"

MARKS=0
TOTAL=50

if [ ! -f index.html ]; then
    echo "❌ index.html not found"
    exit 1
fi

echo "✅ index.html found"
MARKS=$((MARKS + 5))

if grep -qi "<!DOCTYPE html>" index.html; then
    echo "✅ DOCTYPE found"
    MARKS=$((MARKS + 5))
else
    echo "❌ DOCTYPE missing"
fi

if grep -qi "<main>" index.html; then
    echo "✅ <main> element found"
    MARKS=$((MARKS + 5))
else
    echo "❌ <main> element missing"
fi

if grep -qi "<h1>" index.html; then
    echo "✅ <h1> element found"
    MARKS=$((MARKS + 5))
else
    echo "❌ <h1> element missing"
fi

if grep -qi 'class="blue"' index.html; then
    echo "✅ blue class found"
    MARKS=$((MARKS + 5))
else
    echo "❌ blue class missing"
fi

if grep -qi 'class="right"' index.html; then
    echo "✅ right class found"
    MARKS=$((MARKS + 5))
else
    echo "❌ right class missing"
fi

if grep -qi 'id="copyright"' index.html; then
    echo "✅ copyright ID found"
    MARKS=$((MARKS + 5))
else
    echo "❌ copyright ID missing"
fi

if grep -qi "Jeffrey Toobin" index.html; then
    echo "✅ Jeffrey Toobin found"
    MARKS=$((MARKS + 5))
else
    echo "❌ Jeffrey Toobin missing"
fi

if grep -qi "Andrew Ross Sorkin" index.html; then
    echo "✅ Andrew Ross Sorkin found"
    MARKS=$((MARKS + 5))
else
    echo "❌ Andrew Ross Sorkin missing"
fi

if grep -qi "Copyright 2015" index.html; then
    echo "✅ Copyright text found"
    MARKS=$((MARKS + 5))
else
    echo "❌ Copyright text missing"
fi

echo ""
echo "======================================"
echo " Final Score: $MARKS / $TOTAL"
echo "======================================"

if [ "$MARKS" -ge 40 ]; then
    echo "PASS"
    exit 0
else
    echo "FAIL"
    exit 1
fi
