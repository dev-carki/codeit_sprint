# download_dataset.py (한 번만 실행해서 다운로드 → 복사)
import kagglehub
import shutil
from pathlib import Path

BASE_DIR = Path().resolve()  # 현재 작업 디렉토리 기준
print(BASE_DIR)
DATA_DIR = BASE_DIR / 'common' / 'data'

# 1. kagglehub로 다운로드
source_path = kagglehub.dataset_download("zippyz/cats-and-dogs-breeds-classification-oxford-dataset")

# 2. 로컬 저장 위치
DATA_DIR = BASE_DIR / 'common' / 'data' / "cats_and_dogs_dataset"

# 3. 복사 (이미 존재하면 스킵 가능)
if not DATA_DIR.exists():
    shutil.copytree(source_path, DATA_DIR)
    print(f"✅ 데이터셋 복사 완료: {DATA_DIR}")
else:
    print(f"ℹ️ 이미 데이터셋이 존재합니다: {DATA_DIR}")
