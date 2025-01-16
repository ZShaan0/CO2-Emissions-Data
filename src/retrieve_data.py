import kagglehub
from kagglehub import KaggleDatasetAdapter

path = kagglehub.dataset_download("ravindrasinghrana/carbon-co2-emissions")

print("Path to dataset files:", path)

df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    path,
    "Carbon_(CO2)_Emissions_by_Country.csv",
)

print (df)