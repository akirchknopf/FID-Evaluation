# FID-Evaluation

## Description

This is the repository for the master thesis 'Automated Identification of Information Disorder in Social Media from Multimodal Data'. With the help of [NetIdee](www.netidee.at) successfully implemented. 

This is the third repository of the master thesis. Its main purpose is the evaluation part. The other repositories are:

 - [Preprocessing of the Fakeddit Dataset](https://github.com/akirchknopf/FID-Preprocessing)
 - [Model Calculations and Experiments](https://github.com/akirchknopf/FID-Model-Handling)


## License


* This project is licensed under the GNU General Public License version 3 (GPL v3) - see the [GPL.txt](gpl.txt) file for details.
* This document is distributed under CC-BY-Sharelike-3.0 AT

## Installation Instructions

### Virtual Environment
```
python3 -m venv ./venv

source venv/bin/activate

pip install --upgrade pip

pip3 install jupyter

pip3 install tensorflow-gpu==2.3.0

pip3 install SQLAlchemy

pip3 install PyMySQL

pip3 install pandas

pip3 install bert-for-tf2

pip3 install scikit-learn
```
## Directory Structure
```
.
├── best_models
│   ├── 01_mono_modal
│   │   ├── comments
│   │   │   └── weights-improvement-03-0.87.hdf5
│   │   ├── meta
│   │   │   └── weights-improvement-100-0.62.hdf5
│   │   ├── title
│   │   │   └── weights-improvement-02-0.88.hdf5
│   │   └── visual
│   │       └── weights-improvement-02-0.81.hdf5
│   ├── 02_dual_modal
│   │   ├── title_meta
│   │   │   └── weights-improvement-09-0.88.hdf5
│   │   └── title_visual
│   │       └── weights-improvement-02-0.91.hdf5
│   ├── 03_triple_modal
│   │   └── titleCommentsVisual
│   │       └── weights-improvement-06-0.95.hdf5
│   ├── 04_four_modal
│   │   └── weights-improvement-12-0.95.hdf5
│   ├── final_models.py
├── Evaluation.ipynb
├── multi_cased_L-12_H-768_A-12
│   ├── bert_config.json
│   ├── bert_model.ckpt.data-00000-of-00001
│   ├── bert_model.ckpt.index
│   ├── bert_model.ckpt.meta
│   └── vocab.txt
├── README.md
├── utils
│   ├── datagenUtils
│   │   ├── DataSeqFourModels.py
│   │   ├── DataSeqImageTitle.py
│   │   ├── DataSeqMetaModel.py
│   │   ├── DataSeqTitleMeta.py
│   │   ├── DataSequenceTitleCommentsVisual.py
│   └── utils.py
```

## Download Google BERT Base Model
Please see [Readme Google Bert Models](https://github.com/google-research/bert/blob/master/README.md) for further information about the BERT Models.

For this repository please download: [Download BERT Model](https://storage.googleapis.com/bert_models/2018_11_23/multi_cased_L-12_H-768_A-12.zip)

