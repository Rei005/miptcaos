# Создание и подключение GoogleTest для unit-тестирования

## 📝 Условие
У вас есть библиотека `math_lib` (`calc.cpp`, `calc.h`). Напишите `CMakeLists.txt`, который отвечает следующим требованиям:
* Использует модуль `FetchContent` для автоматического скачивания библиотеки GoogleTest (версия `v1.14.0`, репозиторий `https://github.com/google/googletest.git`) при конфигурации проекта.
* Создает статическую библиотеку `math_lib` из файлов `calc.cpp` и `calc.h`.
* Создает тестовый исполняемый файл `calc_tests` из файла `tests.cpp`.
* Связывает `calc_tests` с библиотекой `math_lib` и таргетом `gtest_main`.
* Включает интеграцию с CTest через `include(CTest)` / `enable_testing()` и регистрирует тесты с помощью `gtest_discover_tests(calc_tests)`.

## ⚙️ Быстрая сборка и тесты
```bash
cmake -B build
cmake --build build
ctest --test-dir build --output-on-failure
pytest tests                          # запустить внешнюю проверку задачи
```

## 🧹 Очистка
```bash
rm -rf build
```

## 🚀 Автотесты в GitHub Actions
```bash
git add CMakeLists.txt tests.cpp
git commit -m "Решение задачи 05"
git push                              # результат проверки появится в Actions ✅
```
