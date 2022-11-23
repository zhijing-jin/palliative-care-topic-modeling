# reference: https://github.com/titipata/scipdf_parser
from efficiency.log import show_var

def get_args():
    import argparse
    parser = argparse.ArgumentParser('Parameters for topic modeling on journal articles')
    parser.add_argument('-journal_name', default='jpm', choices=['jpm', 'jwh'], help='Input a journal name: either "jpm" or "jwh".')
    args = parser.parse_args()
    return args

args = get_args()
journal_name = args.journal_name

class Constants:
    # journal_name = 'jpm'
    # journal_name = 'jwh'
    journal_name = journal_name

    year_sep = 2010 if journal_name == 'jpm' else 2018

    pdf_folder = f'papers_{journal_name}/'
    paper_json = f'papers_parsed/papers_{journal_name}.json'
    file_writeout = 'outputs/text_for_word_cloud_' + journal_name + '_{}.txt'
    file_tmp = 'outputs/tmp_writeout.txt'
    year_seps = list(range(1995, 2025, 5))
    common_meaningless_words = {'patient', 'patients', 'palliative', 'study', 'studies', 'conclusion', 'review', 'method', 'sex', 'factor', 'identify', 'common', 'compare', 'significant', 'increase'}
    common_meaningless_words |= {'also', 'see', 'include', 'may', 'self', 'likely', 'day', 'year', 'datum', 'gender', 'age', 'result'}
    common_meaningless_words |= {'hospice', 'item', 'result', 'outcome', 'less', 'make', 'cope', 'measure', 'rate', 'male', 'female', 'examine', 'group', 'well', 'last', 'high', 'low'}
    common_meaningless_words |= {'set', 'material', 'provide', 'trial', 'time', 'control', 'base', 'level', 'research', 'test'}
    common_meaningless_words |= {'score', 'treatment', 'program', 'service', 'use', 'life', 'care', 'disorder', 'life', 'health', 'woman', 'use', 'program', 'report', 'gain', 'care', 'health', 'man', }
    common_meaningless_words |= {'issue', 'receive', 'role', 'need', 'great', 'fact', 'rslp', 'similar', 'early',
                                 'late', 'background', 'month', 'relate', 'related', 'correlate' }

    useless_pos_tags = {'CC', 'DT', 'IN', 'POS', 'PRP', 'PRP$', 'TO', } # https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
    def __init__(self):
        import os
        if os.path.isdir(self.pdf_folder):
            self.pdf_files = sorted([i for i in os.listdir(self.pdf_folder) if i.endswith('.pdf')])

    @staticmethod
    def paper_json2year(one_paper_json):
        pdf_file_name = one_paper_json['pdf_file_name']
        if pdf_file_name.startswith(C.journal_name + '.'):
            jpm, year, others = pdf_file_name.split('.', 2)
        else:
            years = [int(i['year'][:4]) for i in one_paper_json['references'] if i['year']]
            if not years:
                import pdb;pdb.set_trace()
            year = max(years)
        return int(year)


class PaperAnalyzer:
    def pdf2json(self):
        paper_infos = []
        import scipdf
        from tqdm import tqdm
        for file in tqdm(C.pdf_files):
            one_paper_json = scipdf.parse_pdf_to_dict(C.pdf_folder + file)  # return dictionary
            one_paper_json['pdf_file_name'] = file
            paper_infos.append(one_paper_json)

            # xml = scipdf.parse_pdf('example_data/futoma2017improved.pdf', soup=True)  # option to parse full XML from GROBID

            # output example
            {
                'title': 'Proceedings of Machine Learning for Healthcare',
                'abstract': '...',
                'sections': [
                    {'heading': '...', 'text': '...'},
                    {'heading': '...', 'text': '...'},
                    ...
                ],
                'references': [
                    {'title': '...', 'year': '...', 'journal': '...', 'author': '...'},
                    ...
                ],
                'figures': [
                    {'figure_label': '...', 'figure_type': '...', 'figure_id': '...', 'figure_caption': '...',
                     'figure_data': '...'},
                    ...
                ],
                'doi': '...'
            }

            with open(C.paper_json, 'w') as f:
                import json
                json.dump(paper_infos, f)
        self.paper_infos = paper_infos

    def json2topics(self):
        import json
        with open(C.paper_json) as f:
            paper_infos = json.load(f)
            print('[Info] Obtained {} papers'.format(len(paper_infos)))

        for paper_ix, one_paper_json in enumerate(paper_infos):
            year = C.paper_json2year(one_paper_json)
            paper_infos[paper_ix]['year'] = year

        section_types = ['title', 'abstract', 'sections']
        titles, titles_2010a, titles_2010b = [], [], []
        for one_paper_json in paper_infos:
            secs = [one_paper_json[i] for i in section_types[:2]]
            # secs += [i['text'] for i in one_paper_json['sections']]
            secs = [i.strip() for i in secs if i.strip()]
            one_paper_txt = '\n'.join(secs)

            titles.append(one_paper_txt)
            if one_paper_json['year'] < C.year_sep:
                titles_2010a.append(one_paper_txt)
            else:
                titles_2010b.append(one_paper_txt)
        show_var(['len(titles)', 'len(titles_2010a)', 'len(titles_2010b)', ])
        '''
        (Pdb) article_dict['title']
        'Educational Interventions to Improve Cancer Pain Control: A Systematic Review'
        (Pdb) article_dict['abstract']
        "Objectives: To review studies on cancer pain control interventions, and describe their findings with respect to participants' attitudes and knowledge, pain management, and pain levels."
        '''

        import nltk
        from efficiency.log import fwrite
        from efficiency.nlp import NLP
        from gensim.utils import simple_preprocess

        nlp = NLP(disable=['parser', 'ner'])
        en_stop = set(nltk.corpus.stopwords.words('english'))

        def process_words_version2(sent, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
            """Remove Stopwords, Lemmatization"""

            filter1 = lambda w: w[0].isalpha() \
                                and (w.lower() not in en_stop | C.common_meaningless_words) \
                                and (len(w) > 2)

            sent = [word for word in simple_preprocess(sent) if filter1(word)]
            sent = ' '.join(sent)
            # toks = [(token, token.lemma_, token.pos_) for token in nlp.nlp(sent)]

            texts_out = [token.lemma_ for token in nlp.nlp(sent)
                         if token.pos_ in allowed_postags]
            # import pdb;pdb.set_trace()

            # remove stopwords once more after lemmatization
            texts_out = [word for word in simple_preprocess(' '.join(texts_out)) if filter1(word)]
            return texts_out
        def process_words_verson1(sent):
            from efficiency.nlp import NLP
            nlp = NLP(disable=['parser', 'ner'])

            txt = nlp.word_tokenize(sent, lower=True)
            txt = [i.split() for i in txt]
            pos_tags = nltk.pos_tag(txt)
            # remove prepositions, articles, and pronouns.  Also, stemming or lemmitization.
            txt = [w for w, p in zip(txt, pos_tags)
                    if w[0].isalnum() and (w.lower() not in en_stop | C.common_meaningless_words)
                    and (len(w) > 2) and (p not in C.useless_pos_tags)
                    ]
            return txt
        for time_group, corpus in [('all', titles), ('before', titles_2010a), ('after', titles_2010b)]:
            txt = [process_words_version2(sent) for sent in corpus]
            printout = '\n'.join([' '.join(i) for i in txt])
            fwrite(printout, C.file_writeout.format(time_group), verbose=True)

            print('Topics before/after {} (from {} full-text papers):'.format(C.year_sep, len(txt)))
            for NUM_TOPICS in (5, 10):
                self.txt2topics(txt, NUM_TOPICS=NUM_TOPICS)
                print('=======')

            # import pdb;
            # pdb.set_trace()
            # show_var(['year_seps'])

    @staticmethod
    def get_ngrams(list_txt, num_gram=2):
        grams = [tuple(sent[i:i + num_gram]) for sent in list_txt
                 for i in range(len(sent) - num_gram + 1)]

        from collections import Counter
        cnt = Counter(grams)
        freq_tuples = cnt.most_common(30)
        freq_ngrams = [(' '.join(k), v) for k, v in freq_tuples]
        show_var(['freq_ngrams'])
        return freq_ngrams

    @staticmethod
    def txt2topics(corpus, NUM_TOPICS=10):
        # https://towardsdatascience.com/topic-modelling-in-python-with-nltk-and-gensim-4ef03213cd21
        import gensim
        from gensim import corpora

        dictionary = corpora.Dictionary(corpus)
        corpus = [dictionary.doc2bow(text) for text in corpus]
        # import pickle
        # pickle.dump(corpus, open('corpus.pkl', 'wb'))
        # dictionary.save('dictionary.gensim')

        ldamodel = gensim.models.ldamodel.LdaModel(
            corpus, num_topics=NUM_TOPICS, id2word=dictionary, passes=15)
        # (corpus=corpus, id2word=id2word, num_topics=20, random_state=100, update_every=1, chunksize=100, passes=10, alpha='auto', per_word_topics=True)
        # ldamodel.save('model5.gensim')
        topics = ldamodel.print_topics(num_words=10)
        doc_lda = ldamodel[corpus]

        topics = [i[-1] for i in topics]
        print('\n'.join(['Topic {}:\t{}'.format(i+1, str(t)) for i, t in enumerate(topics)]))
        return topics

    def txt2word_clouds(self):
        # reference: https://www.jasondavies.com/wordcloud/
        pass

if __name__ == '__main__':
    from efficiency.function import set_seed
    set_seed()

    C = Constants()
    print('[Info] Journal name:', journal_name)
    p2j = PaperAnalyzer()
    # p2j.pdf2json()
    p2j.json2topics()
