import os
import subprocess
import time
import pytest

TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture(autouse=True)
def clean_environment():
    subprocess.run(["make", "clean"], cwd=TASK_DIR, capture_output=True)
    yield
    subprocess.run(["make", "clean"], cwd=TASK_DIR, capture_output=True)


def test_auto_sources_and_deps():
    # 1. Запуск make
    res = subprocess.run(["make"], cwd=TASK_DIR, capture_output=True, text=True)
    assert res.returncode == 0, f"make завершился с ошибкой:\n{res.stderr}"

    # 2. Проверка наличия .o и .d файлов в obj/
    obj_dir = os.path.join(TASK_DIR, "obj")
    assert os.path.exists(obj_dir), "Папка obj/ не создана"
    assert os.path.exists(
        os.path.join(obj_dir, "calc.o")
    ), "Файл obj/calc.o не найден"
    assert os.path.exists(
        os.path.join(obj_dir, "calc.d")
    ), "Файл зависимостей obj/calc.d не найден (проверьте -MMD)"

    # 3. Проверка автоматической пересборки при изменении calc.h
    calc_h_path = os.path.join(TASK_DIR, "calc.h")
    calc_o_path = os.path.join(obj_dir, "calc.o")

    initial_mtime = os.path.getmtime(calc_o_path)

    time.sleep(1)

    # Обновляем таймштамп заголовочного файла
    os.utime(calc_h_path, None)

    # Повторный запуск make
    res_rebuild = subprocess.run(
        ["make"], cwd=TASK_DIR, capture_output=True, text=True
    )
    assert res_rebuild.returncode == 0

    new_mtime = os.path.getmtime(calc_o_path)
    assert (
        new_mtime > initial_mtime
    ), "Объектный файл calc.o не был пересобран после изменения calc.h!"
