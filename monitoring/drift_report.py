from evidently import Report
from evidently.presets import DataDriftPreset
import pandas as pd

reference = pd.read_csv("./data/Telco-Customer-Churn.csv").sample(500, random_state=1)
current = pd.read_csv("./data/Telco-Customer-Churn.csv").sample(500, random_state=2)

report = Report([
    DataDriftPreset()
])
my_results = report.run(reference_data=reference, current_data=current)
print(my_results)
# report.save_html("./monitoring/drift_report.html")
