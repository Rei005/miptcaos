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


def test_googletest_build_and_ctest():
    # 1. CMake Configuration
    config_res = subprocess.run(
        ["cmake", "-B", "build"],
        cwd=TASK_DIR,
        capture_output=True,
        text=True,
    )
    assert config_res.returncode == 0, f"CMake config failed:\n{config_res.stderr}"

    # 2. Build
    build_res = subprocess.run(
        ["cmake", "--build", "build"],
        cwd=TASK_DIR,
        capture_output=True,
        text=True,
    )
    assert build_res.returncode == 0, f"CMake build failed:\n{build_res.stderr}"

    # 3. Run CTest
    ctest_res = subprocess.run(
        ["ctest", "--test-dir", "build", "--output-on-failure"],
        cwd=TASK_DIR,
        capture_output=True,
        text=True,
    )
    assert ctest_res.returncode == 0, f"CTest failed:\n{ctest_res.stdout}\n{ctest_res.stderr}"
    assert "Passed" in ctest_res.stdout
