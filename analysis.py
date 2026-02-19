all_rows= []
import pandas as pd
from pathlib import Path
import spacy

nlp = spacy.load("en_core_web_sm")

data_path = Path("data")
files = list (data_path.glob("*.txt"))


for file in files:
    text = file.read_text(encoding="utf-8").strip()

    if not text:
        print(f"skipping {file.name}, empty")
        continue
    print (f"{file.name}lenght", len(text))
    doc = nlp(text)


    for token in doc:
        all_rows.append({
            "story": file.name,
            "word": token.text,
            "pos": token.pos_,
            "lemma": token.lemma_,
        })
print ("total tokens collected", len(all_rows))

df = pd.DataFrame(all_rows)
for story in df["story"].unique():
    print(story,len(df[df["story"] == story]))
csv_path = Path.cwd() / "annotated_corpus_finally_final.csv"
df.to_csv(csv_path, index=False)
print("csv saved to", csv_path)
print("stories included:",df["story"].unique())
print("total tokens collected", len(df))




