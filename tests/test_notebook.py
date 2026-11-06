import json
from pathlib import Path


NOTEBOOK_PATH = Path(__file__).resolve().parents[1] / "Machine_Learning_Linear_Regression.ipynb"


def test_notebook_is_valid_json_with_code_cells():
    notebook = json.loads(NOTEBOOK_PATH.read_text(encoding="utf-8"))
    assert notebook["cells"]
    assert any(cell.get("cell_type") == "code" for cell in notebook["cells"])


def test_notebook_uses_portable_dataset_path():
    notebook = json.loads(NOTEBOOK_PATH.read_text(encoding="utf-8"))
    source = "\n".join(
        "".join(cell.get("source", []))
        for cell in notebook["cells"]
        if cell.get("cell_type") == "code"
    )
    assert 'Path("student_exam_data_v1.csv")' in source
    assert "drive/MyDrive" not in source


def test_notebook_has_no_stale_execution_outputs():
    notebook = json.loads(NOTEBOOK_PATH.read_text(encoding="utf-8"))
    for cell in notebook["cells"]:
        if cell.get("cell_type") == "code":
            assert cell.get("execution_count") is None
            assert cell.get("outputs", []) == []
