import os
import subprocess
import pytest

TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture(autouse=True)
def clean_environment():
    subprocess.run(["make", "clean"], cwd=TASK_DIR, capture_output=True)
    yield
    subprocess.run(["make", "clean"], cwd=TASK_DIR, capture_output=True)


def test_default_release_build():
    # Проверка сборки по умолчанию (Release)
    res = subprocess.run(["make"], cwd=TASK_DIR, capture_output=True, text=True)
    assert res.returncode == 0, f"make завершился с ошибкой:\n{res.stderr}"

    target = os.path.join(TASK_DIR, "calculator")
    assert os.path.exists(target), "Исполняемый файл calculator не создан"

    exec_res = subprocess.run([target], capture_output=True, text=True)
    assert exec_res.returncode == 0
    assert "Result: 5" in exec_res.stdout


def test_debug_build():
    # Проверка сборки с MODE=debug
    res = subprocess.run(
        ["make", "MODE=debug"], cwd=TASK_DIR, capture_output=True, text=True
    )
    assert res.returncode == 0, f"make MODE=debug завершился с ошибкой:\n{res.stderr}"

    target = os.path.join(TASK_DIR, "calculator")
    assert os.path.exists(target), "Исполняемый файл calculator не создан"


def test_invalid_mode():
    # Проверка обработки невалидного режима
    res = subprocess.run(
        ["make", "MODE=invalid_mode"], cwd=TASK_DIR, capture_output=True, text=True
    )
    assert res.returncode != 0, "make должен завершаться с ошибкой при невалидном MODE"
