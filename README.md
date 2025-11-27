# Medical-Tool-Interface-AF

![Example image](assets/example.png)

## Overview
This project provides a simple Dash-based graphical interface for generating medical predictions.  
Users can input patient data into the form and receive model outputs along with interactive visualizations.  
Currently, the tool supports **cardiovascular death prediction**.

The GUI communicates with a separate backend API. This separation allows you to update the interface, layout, or visualizations without altering the model logic.

## How to Run

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd <your-project-directory>
```

### 2. Start the backend API
```bash
univorn api:app -reload
```

### 3. Launch the GUI
On another terminal
```bash
python3 app_v1.py
```

### 4. Acess the app
Open your browser at:
```ccp
http://127.0.0.1:8051/
```

Enter patient data, submit the form, and view predictions and visualizations in real time.

Any questions contact the repository owner.