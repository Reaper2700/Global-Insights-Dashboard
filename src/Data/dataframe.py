import polars as pl


def dataframe():
    archive = "world_development_indicators.csv"
    return pl.read_csv(archive)