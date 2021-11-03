pip install beautifulsoup4 # for pdf2json
pip install nltk # for topic modeling, delete stop words
pip install gensim # for topic modeling
pip install efficiency
python -m nltk.downloader stopwords
python -m nltk.downloader wordnet

pip install git+https://github.com/titipata/scipdf_parser # for pdf2json
python -m spacy download en_core_web_sm # as part of scipdf_parser

git clone https://github.com/titipata/scipdf_parser.git
bash serve_grobid.sh # as part of scipdf_parser

