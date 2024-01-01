This repo stores the codes for topic modeling on palliative care journals for the following paper:

[**Revelations from a Machine Learning Analysis of the Most Downloaded Articles Published in Journal of Palliative Medicine 1999–2018**](https://www.liebertpub.com/doi/full/10.1089/jpm.2022.0574) (Journal of Palliative Medicine, 2023) by *Suzanne Tamang, Zhijing Jin, Vyjeyanthi S Periyakoil*.

## Data Preparation
First, download the journal papers. For convenience, you can check the `papers_parsed/` folder, or you can also download the data on your own as follows.
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

In addition, we also saved the text for word cloud generation in the `outputs/` folder.

## Citation

```bib
@article{tamang2023revelations,
    author = "Tamang, Suzanne and Jin, Zhijing and Periyakoil, Vyjeyanthi S.",
    title = "Revelations from a Machine Learning Analysis of the Most Downloaded Articles Published in Journal of Palliative Medicine 1999--2018",
    journal = "Journal of Palliative Medicine",
    volume = "26",
    number = "1",
    pages = "13-16",
    year = "2023",
    doi = "10.1089/jpm.2022.0574",
    note = "PMID: 36607778",
    URL = "https://doi.org/10.1089/jpm.2022.0574",
    eprint = "https://doi.org/10.1089/jpm.2022.0574"
}
```

