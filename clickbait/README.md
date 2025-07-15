# TA1C (Te Ahorré Un Click): Clickbait Datasets

Clickbait is a technique for generating headlines and teasers that deliberately omit part of the information with the goal of raising the readers' curiosity, capturing their attention and enticing them to click.

We present datasets for the tasks of clickbait detection (classifying whether a news teaser is clickbait) and spoiling (answering the implicit question posed on the clickbait) in Spanish.

Even though clickbait is a widely employed term, there remains a lack of consensus regarding its precise definition. Despite the different criteria about what clickbait is, there is some common ground: it differs from traditional headlines in their objective and style, leaving behind the goal of informing in favor of attracting attention. For these datasets, we use the definition introduced earlier and presented in [(Mordecki, Moncecchi, y Couto, 2024)](https://doi.org/10.1007/978-3-031-80366-6_32), based on Loewenstein's information gap theory, as well as the annotation criteria.

A more detailed description of the datasets, tasks, and competition can be found in (Overview of TA1C at IberLEF 2025: Detecting and Spoiling Clickbait in Spanish-Language News). A more detailed description of the clickbait definition, criterias and detection task can be found in [Te ahorré un click: Caracterización y detección automática de clickbait en español.](https://hdl.handle.net/20.500.12008/48614)

## [Detection](/clickbait/iberlef2025/detection)

For this task, we release a corpus of 4,200 tweets divided into three subsets. The training and development sets, comprising 2,800 and 700 examples respectively, are from the previously published [TA1C dataset](https://github.com/gmordecki/TA1C).

The test set consists of 700 newly annotated tweets extracted from the same corpus but that were not previously published.

All tweets were collected throughout a year between October 2020 and October 2021 from 18 well known media outlets in Spanish, including many geographic varieties. Three independent annotators labeled each tweet with a set of annotation guidelines that ensures a high inter-annotator agreement, presented in [(Mordecki, Moncecchi, y Couto, 2024)](https://doi.org/10.1007/978-3-031-80366-6_32).

The dataset contains:

- Tweet ID
- Tweet Date
- Media Name
- Media Origin
- Teaser Text, the article's title followed by the tweet text or one of them if they are the same
- Tag Value, can be "Clickbait" or "No"

## [Spoiling](/clickbait/iberlef2025/spoiling)

For the spoiling task we release another corpus with 500 manually written spoilers. All of the examples come from the detection dataset and were previously, and manually, classified as clickbait.

We followed a set of annotation guidelines to maximize consistency across the results:
- Make it as short as possible, keep it concise. No extra information, even if it is interesting and related.
- Extraction is preferred over generation.
- When the answer appears multiple times in the article, use its first occurrence.
- Even when generating text, try to paraphrase the article and use the same words. When an extracted text needs some edition to make sense, limit edits as much as possible.
- There are two special responses:
    - `No hay respuesta` when the article does not fill the information gap.
    - `La respuesta es la nota completa` when there is no possibility to reduce or summarize the response.
- The response can be a link to multimedia content (such as a photograph, video, or social network link).

Roughly half of the annotations of the annotated dataset are extracted, and the other half are generated, frequently with only minimal modifications to the extracted content.

The dataset contains:
- Tweet ID
- Tweet Date
- Media Name
- Media Origin
- Article URL
- Teaser Text, the article's title followed by the tweet text or one of them if they are the same
- Article Text JSON. A JSON with keys `'Title', 'Subtitle' and 'Text'` where Text is a cleaned version of the article's scraped body.
 the URL and clean HTML text of the linked news, alongside the scraped headline, sub-headline, clean text (only the news body), images with their captions and embedded URLs (usually social media links).
- Response, the manually extracted or generated spoiler.


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
