import os
import subprocess
import pytest

# Директория самой задачи (на уровень выше директории tests)
TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture(autouse=True)
def clean_environment():
    """Автоматическая очистка скомпилированных файлов до и после выполнения теста."""
    subprocess.run(["make", "clean"], cwd=TASK_DIR, capture_output=True)
    yield
    subprocess.run(["make", "clean"], cwd=TASK_DIR, capture_output=True)


def test_compilation_and_execution():
    """Проверка правильности компиляции, структуры папок и работы программы."""
    # 1. Запуск make
    build_res = subprocess.run(
        ["make"], cwd=TASK_DIR, capture_output=True, text=True
    )
    assert (
        build_res.returncode == 0
    ), f"Команда make завершилась с ошибкой:\n{build_res.stderr}"

    # 2. Проверка наличия папки obj/ и .o файлов
    obj_dir = os.path.join(TASK_DIR, "obj")
    assert os.path.exists(obj_dir), "Папка obj/ не была создана"
    assert os.path.isdir(obj_dir), "Объект obj/ должен быть директорией"
    assert os.path.exists(
        os.path.join(obj_dir, "main.o")
    ), "Файл obj/main.o отсутствует"
    assert os.path.exists(
        os.path.join(obj_dir, "calc.o")
    ), "Файл obj/calc.o отсутствует"

    # 3. Проверка присутствия исполняемого файла calculator в корне задачи
    executable = os.path.join(TASK_DIR, "calculator")
    assert os.path.exists(
        executable
    ), "Исполняемый файл calculator не найден в корне задачи"

    # 4. Проверка запуска скомпилированного бинарного файла
    exec_res = subprocess.run([executable], capture_output=True, text=True)
    assert exec_res.returncode == 0, "Исполняемый файл вернул не нулевой код"
    assert "Result: 5" in exec_res.stdout


def test_make_clean():
    """Проверка выполнения цели make clean."""
    subprocess.run(["make"], cwd=TASK_DIR, capture_output=True)

    clean_res = subprocess.run(
        ["make", "clean"], cwd=TASK_DIR, capture_output=True, text=True
    )
    assert (
        clean_res.returncode == 0
    ), f"Команда make clean завершилась с ошибкой:\n{clean_res.stderr}"

    assert not os.path.exists(
        os.path.join(TASK_DIR, "obj")
    ), "Папка obj/ не была удалена при make clean"
    assert not os.path.exists(
        os.path.join(TASK_DIR, "calculator")
    ), "Файл calculator не был удален при make clean"
