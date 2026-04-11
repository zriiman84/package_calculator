#!/bin/bash
# Script de prueba para el workflow de CI

echo "=========================================="
echo "  🚀 Ejecutando pruebas del proyecto..."
echo "=========================================="

# Verificar versión de bash
echo "✅ Bash version: $BASH_VERSION"

# Verificar que un archivo existe
if [ -f "README.md" ]; then
  echo "✅ README.md encontrado"
else
  echo "❌ README.md no encontrado"
  exit 1
fi

# Simular una "prueba" de suma
resultado=$((3 + 4))
if [ "$resultado" -eq 7 ]; then
  echo "✅ Prueba matemática: 3 + 4 = $resultado (correcto)"
else
  echo "❌ Prueba matemática fallida"
  exit 1
fi

echo ""
echo "✅ Todas las pruebas pasaron exitosamente 🎉"
exit 0