from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path 
    source_URL: Path 
    local_data_file: Path
    unzip_dir: Path
    splited_data: Path

@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path 
    model_path: Path 
    epochs: int
    batch_size: int
    lr: float 
    imgsz: int 
    include_top: bool 
    weights: str
    dataset: Path

@dataclass(frozen=True)
class EvaluationConfig:
    path_of_model: Path
    test_data: Path
    all_params: dict
    mlflow_uri: str
    params_image_size: list
    params_batch_size: int