# Rektify - Bot
ChatBot API for powering the Rektify platform.

## Built Using
| Tools | Version |
| ----- | ------- |
| Python | 3.6.0
| Flask | 1.1.2 |
| Azure QnAMaker | - |

## Getting Started

* Fork this repository

* Clone your repository forked from this one

```bash
git clone https://github.com/:username/Rektify_Bot
```

* Install requirements.txt

```bash
pip install requirements.txt
```

* In order to host your own API, you'll need to make your own QnAMaker Service on Azure.

* Add the following as Environment Variables in a file named `.env`. You can read more about Environment Variables [here](https://pypi.org/project/python-dotenv/)

```bash
QNA_URL=https://example.azurewebsites.net/qnamaker/knowledgebases/sdkfjnsakfjn
QNA_AUTH_KEY=example#-23423
QNA_COOKIE=ARRAffinityexampleexample
```

* Run the included app.py file

```bash
python app.py
```

* You can ping the locally hosted API at `localhost:5000/` in your browser.

---
If you found this repo cool and/or useful, please ⭐ the repo, and if you want to contribute please 🍴.
