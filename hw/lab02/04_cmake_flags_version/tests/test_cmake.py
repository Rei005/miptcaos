import os
import shutil
import subprocess
import pytest

TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD_DIR = os.path.join(TASK_DIR, "build")


@pytest.fixture(autouse=True)
def clean_build_dir():
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
    yield
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)


def test_cmake_release_build():
    # 1. Конфигурация Release
    config_res = subprocess.run(
        ["cmake", "-B", "build", "-DCMAKE_BUILD_TYPE=Release"],
        cwd=TASK_DIR,
        capture_output=True,
        text=True,
    )
    assert config_res.returncode == 0, f"CMake config failed:\n{config_res.stderr}"

    # 2. Проверка генерации version.h
    generated_header = os.path.join(BUILD_DIR, "version.h")
    assert os.path.exists(generated_header), "version.h не был сгенерирован"

    with open(generated_header, "r", encoding="utf-8") as f:
        content = f.read()
        assert '"1.2.3"' in content, "Версия 1.2.3 не найдена в сгенерированном version.h"

    # 3. Сборка
    build_res = subprocess.run(
        ["cmake", "--build", "build"],
        cwd=TASK_DIR,
        capture_output=True,
        text=True,
    )
    assert build_res.returncode == 0, f"CMake build failed:\n{build_res.stderr}"


def test_cmake_debug_build():
    # Конфигурация Debug
    config_res = subprocess.run(
        ["cmake", "-B", "build", "-DCMAKE_BUILD_TYPE=Debug"],
        cwd=TASK_DIR,
        capture_output=True,
        text=True,
    )
    assert config_res.returncode == 0, f"CMake config failed:\n{config_res.stderr}"

    build_res = subprocess.run(
        ["cmake", "--build", "build"],
        cwd=TASK_DIR,
        capture_output=True,
        text=True,
    )
    assert build_res.returncode == 0, f"CMake build failed:\n{build_res.stderr}"
