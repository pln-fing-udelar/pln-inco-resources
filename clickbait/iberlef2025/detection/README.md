# TA1C (Te Ahorré Un Click): Clickbait Detection Dataset

Clickbait is a technique for generating headlines and teasers that deliberately omit part of the information with the goal of raising the readers' curiosity, capturing their attention and enticing them to click.

We present a dataset for the task of clickbait detection, classifying whether a news teaser is clickbait or not, in Spanish.

Even though clickbait is a widely employed term, there remains a lack of consensus regarding its precise definition. Despite the different criteria about what clickbait is, there is some common ground: it differs from traditional headlines in their objective and style, leaving behind the goal of informing in favor of attracting attention. For these datasets, we use the definition introduced earlier and presented in [(Mordecki, Moncecchi, y Couto, 2024)](https://doi.org/10.1007/978-3-031-80366-6_32), based on Loewenstein's information gap theory, as well as the annotation criteria.

We release a corpus of 4,200 tweets divided into three subsets. The training and development sets, comprising 2,800 and 700 examples respectively, are from the previously published [TA1C dataset](https://github.com/gmordecki/TA1C).

The test set consists of 700 newly annotated tweets extracted from the same corpus but that were not previously published.

All tweets were collected throughout a year between October 2020 and October 2021 from 18 well known media outlets in Spanish, including many geographic varieties. Three independent annotators labeled each tweet with a set of annotation guidelines that ensures a high inter-annotator agreement, presented in [(Mordecki, Moncecchi, y Couto, 2024)](https://doi.org/10.1007/978-3-031-80366-6_32).

The dataset contains:

- Tweet ID
- Tweet Date
- Media Name
- Media Origin
- Teaser Text, the article's title followed by the tweet text or one of them if they are the same
- Tag Value, can be "Clickbait" or "No"

A more detailed description of the datasets, tasks, and competition can be found in (Overview of TA1C at IberLEF 2025: Detecting and Spoiling Clickbait in Spanish-Language News). A more detailed description of the clickbait definition, criterias and detection task can be found in [Te ahorré un click: Caracterización y detección automática de clickbait en español.](https://hdl.handle.net/20.500.12008/48614)


### Citation

```
@InProceedings{10.1007/978-3-031-80366-6_32,
    author = {Mordecki, Gabriel and Moncecchi, Guillermo and Couto, Javier},
    title = {Te Ahorr\'{e} Un Click: A Revised Definition of&nbsp;Clickbait and&nbsp;Detection in&nbsp;Spanish News},
    year = {2025},
    isbn = {978-3-031-80365-9},
    publisher = {Springer-Verlag},
    address = {Berlin, Heidelberg},
    url = {https://doi.org/10.1007/978-3-031-80366-6_32},
    doi = {10.1007/978-3-031-80366-6_32},
    booktitle = {Advances in Artificial Intelligence – IBERAMIA 2024: 18th Ibero-American Conference on AI, Montevideo, Uruguay, November 13–15, 2024, Proceedings},
    pages = {387–399},
    numpages = {13},
    keywords = {clickbait, clickbait definition, clickbait detection, corpus, news articles, social media, spanish, natural language processing},
    location = {Montevideo, Uruguay}
}
```
