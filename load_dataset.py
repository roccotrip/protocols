import pickle
import argparse
import pandas as pd


def get_ds(Dataset, ds_type, sentence_type, lang):
    if ds_type == 'dataset':
        data = {'protocols sentences' : Dataset[lang]['prot_dataset'][sentence_type],
                'dialogue sentences': Dataset[lang]['dial_dataset'][sentence_type],
                'scores': Dataset[lang]['scores']
                }
    elif ds_type == 'books':
        data = {'protocols sentences': Dataset[lang]['prot_book'][sentence_type],
                'dialogue sentences': Dataset[lang]['dial_book'][sentence_type],
                'scores': Dataset[lang]['scores']
                }
    else:
        print('Unsupported dataset type. It can be "dataset" or "books"')
        raise
    return pd.DataFrame(data)

def load_protocols(ds_path, ds_type, sentence_type, lang):
    with open(ds_path, 'rb') as f:
        Dataset = pickle.load(f)
    ds = get_ds(Dataset, ds_type, sentence_type, lang)
    print(ds.to_string)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ds_path', type=str, default='data/Protocoles_Dataset.pkl', help="the path to the dataset .pkl file")
    parser.add_argument('--ds_type', type=str, default='dataset',
                        help='It can be "dataset" (to get only the plagiarized sentences); "books" (to get all the sentences of the books) ')
    parser.add_argument('--sentence_type', type=str, default='sentences', help='It can be "sentences" (to get the sentences of the dataset); "tokens_splitted" (to get the original sentences splitted using SpaCy sentencizer and SpaCy tokenizer; "tokens" (to get the sentences tokenized using SpaCy tokenizer) ')
    parser.add_argument('--lang', type=str, default='FR', help="It can be either EN or FR")

    args = parser.parse_args()
    ds = load_protocols(args.ds_path, args.ds_type, args.sentence_type, args.lang)