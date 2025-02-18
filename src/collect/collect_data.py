import pandas as pd

def collect_data() -> pd.DataFrame:
    # まず手打ちでデータを作成
    with open("../data/one_book.txt", "r") as f:
        data = f.read().splitlines()

    book_title = data[0]
    body = "".join(data[1:]).replace("\n", "").replace("##", "\n##")

    data_dict = {"book_title": book_title, "body": body}
    df = pd.DataFrame(data_dict, index=[0])
    df.to_csv("../data/articles.csv", index=False)

if __name__ == "__main__":
    collect_data()