from datasets import load_dataset

images = '/data/new-yorker/images-raw'

dataset = load_dataset("imagefolder", data_dir=images)
dataset.push_to_hub("annabelng/nymemes", private=True)
#print(dataset[:10]['text'])
