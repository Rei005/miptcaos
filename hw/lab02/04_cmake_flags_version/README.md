# Управление флагами компиляции и вычисление версии проекта

## 📝 Условие
Напишите `CMakeLists.txt` для проекта калькулятора, который отвечает следующим требованиям:
* Минимальная версия CMake — `3.15`, имя проекта — `CalcProject`, версия проекта — `1.2.3`.
* Собирает исполняемый файл `calculator` из исходников `main.cpp` и `calc.cpp`.
* С помощью `configure_file` генерирует заголовочный файл `version.h` из шаблона `version.h.in` в директории сборки (`CMAKE_CURRENT_BINARY_DIR`).
* Подключает директорию со сгенерированным `version.h` к таргету `calculator` с помощью `target_include_directories`.
* Добавляет генерацию макроса компилятора `DEBUG_MODE` для конфигурации `Debug` с использованием generator expressions (`$<$<CONFIG:Debug>:DEBUG_MODE>`) в `target_compile_definitions`.

## ⚙️ Быстрая сборка и тесты
```bash
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build
./build/calculator
pytest tests                          # запустить тесты
```

## 🧹 Очистка
```bash
rm -rf build
```

## 🚀 Автотесты в GitHub Actions
```bash
git add CMakeLists.txt version.h.in
git commit -m "Решение задачи 04"
git push                              # результат проверки появится в Actions ✅
```
