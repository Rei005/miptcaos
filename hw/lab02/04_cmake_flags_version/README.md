# Управление флагами компиляции и вычисление версии проекта

## 📝 Условие
Напишите `CMakeLists.txt` для проекта калькулятора, который отвечает следующим требованиям:
1. Минимальная версия CMake — `3.15`, имя проекта — `CalcProject`, версия проекта — `1.2.3`.
2. Собирает исполняемый файл `calculator` из исходников `main.cpp` и `calc.cpp`.
3. С помощью `configure_file` генерирует заголовочный файл `version.h` из шаблона `version.h.in` в директории сборки (`CMAKE_CURRENT_BINARY_DIR`).
4. Подключает директорию со сгенерированным `version.h` к таргету `calculator` с помощью `target_include_directories`.
5. Добавляет генерацию макроса компилятора `DEBUG_MODE` для конфигурации `Debug` с использованием generator expressions (`$<$<CONFIG:Debug>:DEBUG_MODE>`) в `target_compile_definitions`.

## ⚙️ Быстрая сборка и запуск
```bash
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build
./build/calculator
```

Запуск автотестов:
```bash
pytest tests
```
