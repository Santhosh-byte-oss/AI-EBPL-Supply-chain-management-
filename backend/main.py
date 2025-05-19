import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from pathlib import Path

# Define the path to your data file relative to the backend directory
# This makes the path work regardless of where you run the script from
DATA_FILE_PATH = Path(__file__).parent / "data" / "inventory.csv"

# --- Data Loading ---
# Load the data globally when the app starts. This avoids reloading on every request.
try:
    inventory_df = pd.read_csv(DATA_FILE_PATH)
    print("Inventory data loaded successfully.")
except FileNotFoundError:
    print(f"Error: Data file not found at {DATA_FILE_PATH}")
    inventory_df = pd.DataFrame() # Create empty DataFrame if file not found
except Exception as e:
    print(f"Error loading data: {e}")
    inventory_df = pd.DataFrame()


# --- Pydantic Models for Data Structure ---
# Define how the data should look when sent via the API
class InventoryItem(BaseModel):
    item_id: int
    item_name: str
    stock: int
    reorder_level: int

# --- FastAPI App Initialization ---
app = FastAPI(
    title="SCM Inventory AI Backend",
    description="API for managing and analyzing inventory data."
)

# --- API Endpoints ---

@app.get("/", tags=["Root"])
async def read_root():
    """Basic endpoint to confirm the API is running."""
    return {"message": "Welcome to the SCM Inventory AI Backend!"}

@app.get("/inventory/", response_model=List[InventoryItem], tags=["Inventory"])
async def get_all_inventory():
    """
    Retrieves all items from the inventory dataset.
    Returns a list of InventoryItem objects.
    """
    if inventory_df.empty:
         # If data loading failed, return an error
         raise HTTPException(status_code=500, detail="Inventory data not loaded.")
    # Convert the pandas DataFrame to a list of dictionaries
    return inventory_df.to_dict(orient="records")

@app.get("/inventory/low-stock/", response_model=List[InventoryItem], tags=["Inventory"])
async def get_low_stock_items():
    """
    Retrieves items where the current stock is below the reorder level.
    This is our initial 'AI' logic - a simple rule-based check.
    Returns a list of InventoryItem objects that are low in stock.
    """
    if inventory_df.empty:
         # If data loading failed, return an error
         raise HTTPException(status_code=500, detail="Inventory data not loaded.")

    # Filter the DataFrame where 'stock' is less than 'reorder_level'
    low_stock_items = inventory_df[inventory_df['stock'] < inventory_df['reorder_level']]

    # Convert the filtered DataFrame to a list of dictionaries
    # If no items are low stock, this will return an empty list, which is fine
    return low_stock_items.to_dict(orient="records")

# Potential future endpoints could include:
# - /inventory/{item_id} - Get details for a specific item
# - /inventory/update-stock - Endpoint to update stock levels
# - /inventory/forecast - Endpoint to get demand forecasts (requires more data and a model)
