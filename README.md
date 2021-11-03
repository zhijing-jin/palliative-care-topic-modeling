This repo stores the codes for topic modeling on palliative care journals.

## Data Preparation
You first need to download the journal papers.
```bash
bash 1_download_pdfs.sh # To download papers from the journal `jpm`
bash 1_download_pdfs_jwh.sh # To download papers from the journal `jwh`
```
## Environment Setup
Install all the necessary python packages.
```bash
bash 2_pdf2json_prep_env.sh
```

## How to Run the Topic Model
Run the topic modeling on the default journal `jpm`:
```bash
python 3_pdf2json2topics.py
```
Or you can also run the topic modeling on the other journal `jwh`:
```bash
python 3_pdf2json2topics.py -journal_name jwh
```

