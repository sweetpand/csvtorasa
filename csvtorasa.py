import pandas as pd
def create_rasa_nlu(path, nlu_md_path):
    """
    Converts an CSV file created with the specified format to RASA accepted nlu.md format
    :param path: path where the CSV file is present
    :param nlu_md_path: path where the nlu.md file needs to be created
    :return: return nothing. A file is created in the path specified via nlu_md_path
    """
    df = pd.read_csv(r"{}".format(path))
    file = open(r'{}\nlu.md'.format(nlu_md_path), "w")
    intents = list(df.columns)
    for item in intents:
        file.write("## intent: {intent_name}\n".format(intent_name = item))
        for sent in df[item]:
            file.write("- {}\n".format(sent))
    file.close()
    return None

