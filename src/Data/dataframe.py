import polars as pl


def dataframe():
    archive = "Data/world_development_indicators.csv"
    return pl.read_csv(archive)