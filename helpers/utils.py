import pandas as pd
import ast

def grand_average(df,descriptors):
    df_groupbyCID=df.groupby('CID')[descriptors].mean().reset_index()

    df_groupbyCID['y'] = df_groupbyCID.loc[:, '0.1':descriptors[-1]].values.tolist()
    df_embeddings=df.drop_duplicates(subset=['CID'])
    df_embeddings=df_embeddings[['CID','embeddings']]
    df_groupbyCID = pd.merge(df_groupbyCID, df_embeddings, on='CID', how='left')
    return df_groupbyCID


def average_per_subject(df,descriptors):
    df_groupbyCID=df.groupby(['CID','subject'])[descriptors].mean().reset_index()

    df_groupbyCID['y'] = df_groupbyCID.loc[:, '0.1':descriptors[-1]].values.tolist()
    df_embeddings=df.drop_duplicates(subset=['CID'])
    df_embeddings=df_embeddings[['CID','embeddings']]
    df_groupbyCID = pd.merge(df_groupbyCID, df_embeddings, on='CID', how='left')
    return df_groupbyCID

def prepare_dataset(ds):
    ds['y'] = ds['y'].apply(ast.literal_eval)
    ds['embeddings'] = ds['embeddings'].apply(ast.literal_eval)

    return ds