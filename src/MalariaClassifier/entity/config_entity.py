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