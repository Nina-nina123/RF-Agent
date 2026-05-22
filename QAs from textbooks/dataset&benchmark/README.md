###

# Collection of dataset & benchmark

This document describes the processing of raw QTSA and benchmark. Processed dataset and benchark are saved under 
- /SFT/Qwen3-0.6B/validation_QTSA
- /SFT/Qwen3-0.6B/validation_QTSA_mix
- /SFT/Qwen3-0.6B/testbench

For the size of files, we divide them into smaller files, like xxx(1).jsonl.

## File Description

| File / Folder | Description |
|----------------|-------------|
| `mcQTSA_dataset_devision.ipynb` | Dividing mcQTSA into train dataset, validation dataset and 1000-question benchmark<br>Giving each question of benchmark original ID (getting their categorization) |
| `QTSA_dataset_devision.ipynb` | Dividing ndQTSA into train dataset and validation dataset<br>merge mcQTSA and ndQTSA into mixed dataset |
| `mcQTSA_new4.jsonl` | Final version of mcQTSA dataset |
| `QTSA_new1.jsonl` | Final version of ndQTSA dataset |
