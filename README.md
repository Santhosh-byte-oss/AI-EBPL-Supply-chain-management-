Supply Chain Inventory Monitor & AI ChatbotThis project is a basic application for monitoring inventory levels in a supply chain and includes a simple, simulated AI chatbot interface. It demonstrates a decoupled architecture using a FastAPI backend to serve data and a Streamlit frontend for the user interface.FeaturesInventory Overview: Displays all items from a dataset, including stock levels and reorder points.Low Stock Alert: Highlights items where the current stock is below the defined reorder level.Manual Data Refresh: Button to manually refresh the inventory data displayed in the frontend.Simulated AI Chatbot: A basic chat interface within the Streamlit app that provides simple, rule-based responses related to inventory and SCM concepts. (Note: This version uses simulated responses; integration with a real AI model requires further development).Project Structurescm_ai/

├── backend/
│   ├── __init__.py       # Marks backend as a Python package
│   ├── main.py           # FastAPI application code
│   └── data/
│       └── inventory.csv   # Your dataset file
├── frontend/
│   ├── __init__.py       # Marks frontend as a Python package
│   └── app.py            # Streamlit application code
├── requirements.txt      # Lists project dependencies
└── README.md             # Project description and instructions

Setup and InstallationClone or download the project files:Ensure you have the project structure and files (backend/main.py, backend/data/inventory.csv, frontend/app.py, requirements.txt) in a directory named scm_ai.Navigate to the project directory:cd scm_ai

Create a virtual environment (highly recommended):python -m venv venv

Activate the virtual environment:On Windows:venv\Scripts\activate

On macOS/Linux:source venv/bin/activate

Install dependencies:Make sure you have the requirements.txt file in the root directory (scm_ai/).pip install -r requirements.txt

Ensure your dataset is in place:Verify that your inventory.csv file is located at scm_ai/backend/data/inventory.csv.Running the ApplicationThis application requires both the backend and the frontend to be running simultaneously.Run the Backend (FastAPI with Uvicorn):Open your terminal, navigate to the scm_ai directory, activate your virtual environment, and run:uvicorn backend.main:app --reload

This will start the FastAPI server, typically on http://127.0.0.1:8000. The --reload flag allows the server to restart automatically when you make changes to the backend code. Keep this terminal window open.Run the Frontend (Streamlit):Open a new terminal window or tab, navigate to the scm_ai directory, activate your virtual environment, and run:streamlit run frontend/app.py

This will start the Streamlit application and open it in your web browser, typically at http://localhost:8501.You should now see the Streamlit application displaying the inventory data and the chatbot interface.Future EnhancementsIntegrate a Real AI Model: Connect the chatbot backend to a real Large Language Model (LLM) like Gemini, OpenAI's GPT, etc., to provide more intelligent and context-aware responses. This would likely involve adding API call logic to the FastAPI backend.Add More Data: Include historical sales data, lead times, supplier information, costs, etc., to enable more advanced SCM analysis.Implement Advanced SCM Logic:Demand Forecasting (using time series models).Optimal Reorder Quantity/Point calculations.Supplier Performance Monitoring.Inventory Optimization algorithms.Improve Frontend UI: Add charts, graphs, and more interactive elements using Streamlit or other frontend libraries.Authentication and Authorization: Secure the application if used in a multi-user environment.Deployment: Deploy the backend and frontend to cloud platforms (e.g., Heroku, AWS, Google Cloud) for wider access.
