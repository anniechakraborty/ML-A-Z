import pandas as pd

def change_delimiter_csv(file_path):
    df = pd.read_csv(file_path, delimiter=';')
    # Save the cleaned CSV with standard comma-separated format
    df.to_csv('winequality_cleaned.csv', index=False)


if __name__ == '__main__':
    change_delimiter_csv('winequality.csv')