#!/bin/bash
set -e

NAME=$1
VERSION=$2

if [ -z "$NAME" ] || [ -z "$VERSION" ]; then
    echo "الاستخدام: $0 <اسم-المكتبة> <الإصدار>"
    exit 1
fi

PKG_DIR="${NAME}-${VERSION}"
mkdir -p "$PKG_DIR/include" "$PKG_DIR/lib"

echo "📦 بناء الحزمة ${NAME}-${VERSION}..."

if [ -f "${NAME}.c" ]; then
    gcc -shared -fPIC -I. "${NAME}.c" -o "$PKG_DIR/lib/lib${NAME}.so"
    echo "✓ تم بناء lib${NAME}.so"
fi

if [ -f "${NAME}.h" ]; then
    cp "${NAME}.h" "$PKG_DIR/include/"
    echo "✓ تم نسخ ${NAME}.h"
fi

cat > "$PKG_DIR/manifest.json" <<EOF
{
    "name": "${NAME}",
    "version": "${VERSION}",
    "description": "مكتبة ${NAME}",
    "type": "shared",
    "headers": ["include/${NAME}.h"],
    "libs": ["lib/lib${NAME}.so"],
    "dependencies": []
}
EOF

tar -czvf "${PKG_DIR}.tar.gz" "$PKG_DIR/"
echo "🎉 الحزمة جاهزة: ${PKG_DIR}.tar.gz"
