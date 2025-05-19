import streamlit as st
import requests
import pandas as pd
import time # Import time for simulating AI response delay

# Define the URL of your backend API
# Assuming the backend is running locally on port 8000
BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(layout="wide") # Use wide layout for better table display

st.title("📈 Supply Chain Inventory Monitor & AI Chatbot")
st.markdown("Connects to a backend API to display inventory levels and low-stock items, and includes a simple chatbot.")

# --- Function to Fetch Data from Backend ---
# Using Streamlit's caching decorator to avoid refetching data unnecessarily
@st.cache_data(ttl=60) # Cache data for 60 seconds
def get_inventory_data(url):
    """Fetches data from the specified backend endpoint."""
    try:
        # Make a GET request to the backend API
        response = requests.get(url)
        # Raise an HTTPError for bad responses (4xx or 5xx status codes)
        response.raise_for_status()
        # Return the JSON response
        return response.json()
    except requests.exceptions.ConnectionError:
        # Handle cases where the backend is not reachable
        st.error(f"Could not connect to backend. Please ensure the backend is running at {BACKEND_URL}")
        return None
    except requests.exceptions.RequestException as e:
        # Handle other potential request errors
        st.error(f"Error fetching data from {url}: {e}")
        return None

# --- Display Inventory Data ---

# Fetch all inventory data
all_inventory_data = get_inventory_data(f"{BACKEND_URL}/inventory/")

# Fetch low stock data
low_stock_data = get_inventory_data(f"{BACKEND_URL}/inventory/low-stock/")

# Display the data if successfully fetched
if all_inventory_data is not None:
    st.header("📦 Full Inventory Overview")
    # Convert list of dictionaries to a pandas DataFrame for display
    inventory_df = pd.DataFrame(all_inventory_data)
    # Display the DataFrame using st.dataframe for an interactive table
    st.dataframe(inventory_df, use_container_width=True) # Use full container width

    st.header("🚨 Items Below Reorder Level")
    if low_stock_data:
        # Convert low stock data to DataFrame
        low_stock_df = pd.DataFrame(low_stock_data)
        # Display low stock items
        st.dataframe(low_stock_df, use_container_width=True)
    else:
        # Message to show if no items are low in stock
        if all_inventory_data: # Only show this message if the main data was loaded
            st.info("🎉 No items are currently below the reorder level. Inventory looks good!")

# Add a manual refresh button for the inventory data
if st.button("Manual Refresh Inventory Data"):
    st.experimental_rerun() # Rerun the app script from the top

# --- Chatbot Section ---

st.header("💬 SCM AI Chatbot (Simulated)")
st.markdown("Ask questions about inventory or SCM concepts.")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask me about inventory..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Simulate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            time.sleep(1) # Simulate processing time

            # Simple rule-based response simulation
            prompt_lower = prompt.lower()
            if "inventory" in prompt_lower or "stock" in prompt_lower:
                response = "I can show you the current inventory levels and items below the reorder point. Look at the tables above!"
            elif "reorder" in prompt_lower:
                 response = "Items below the reorder level need attention. You can see them in the 'Items Below Reorder Level' table."
            elif "scm" in prompt_lower or "supply chain" in prompt_lower:
                 response = "Supply Chain Management involves planning and managing all activities involved in sourcing, procurement, conversion, and all logistics management activities."
            elif "hello" in prompt_lower or "hi" in prompt_lower:
                response = "Hello! How can I help you with your inventory today?"
            else:
                response = "I'm a simple SCM chatbot right now. I can answer basic questions about inventory and reorder levels. For more complex questions, you would need to integrate me with a more powerful AI model."

            st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

st.markdown("---") # Separator
st.markdown("Note: The chatbot responses are simulated in this version.")
