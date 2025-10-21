import pandas as pd


def load_php_dataset(php_file: str) -> tuple[pd.DataFrame, str]:

    php_path = Path(php_file).with_suffix(".php")
    csv_path = php_path.with_suffix(".csv")
    x = None
    print(csv_path)

    with open(php_path, "r") as f:
        lines = f.readlines()[1:]  # skip header line
        data = [line.strip().split(",") for line in lines]
        df = pd.DataFrame(data, columns=["x_1", "x_2", "output"])
        df.to_csv(csv_path, index=False)
        x = f.readlines()[0]
        print(x)
    return df, x

    
