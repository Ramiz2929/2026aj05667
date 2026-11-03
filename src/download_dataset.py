from pathlib import Path
 
import pandas as pd
from ucimlrepo import fetch_ucirepo
 
 
def download_dataset():
    """Download the original UCI dataset and save it locally."""
 
    # Fetch the Online Shoppers dataset (UCI ID: 468)
    dataset = fetch_ucirepo(id=468)
 
    # Extract the 17 input features
    X = dataset.data.features
 
    # Extract the target column
    y = dataset.data.targets
 
    # Combine features and target into one DataFrame
    df = pd.concat([X, y], axis=1)
 
    # Resolve the project root independently of the terminal directory
    project_root = Path(__file__).resolve().parents[1]
    output_dir = project_root / "data" / "raw"
 
    # Create the folder if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
 
    output_file = output_dir / "online_shoppers_intention.csv"
 
    # Save the dataset
    df.to_csv(output_file, index=False)
 
    print("Dataset downloaded successfully!")
    print(f"Saved to: {output_file}")
    print(f"Dataset shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
 
 
if __name__ == "__main__":
    download_dataset()
