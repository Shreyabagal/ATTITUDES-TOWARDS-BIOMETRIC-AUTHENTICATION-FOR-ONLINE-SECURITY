
# Attitudes Towards Biometric Authentication for Online Security

This project investigates user attitudes towards biometric authentication methods for online security. The primary data was collected through a Google Form, which was then analyzed using Python for insights into user preferences, concerns, and awareness.

## Project Structure

The repository contains the following files and folders:

- `Biometric Authentication (Responses).csv`: The raw data collected from the Google Form responses.
- `biometric_data_insights.py`: Python script that performs data analysis and visualizations on the CSV data.
- `requirements.txt`: A file containing all the Python dependencies required to run the analysis script.
- `Responses/`: Folder containing the images visualizing different sections of the survey responses.

## Files Description

### 1. `Biometric Authentication (Responses).csv`
This file contains raw data from the Google Form survey. It includes questions on user demographics, familiarity with biometric authentication, security perceptions, trust in biometric data handling, and more.

### 2. `biometric_data_insights.py`
This Python script analyzes the CSV data and generates various visualizations, such as histograms, bar plots, and correlation matrices, to uncover trends in the data. It also handles data cleaning, such as filling missing values, and outputs the results into a cleaned CSV file.

### 3. `requirements.txt`
This file contains a list of required Python libraries to run the script, including `pandas`, `matplotlib`, `seaborn`, and `numpy`.

### 4. `Responses/`
This folder contains 6 images summarizing the survey response data, divided by different question categories.

- **Image 1**: Age, Gender, Occupation
- **Image 2**: Familiarity and Usage of Biometric Methods
- **Image 3**: Experience, Security Perception, and Concerns
- **Image 4**: Trust, Willingness, and Future Use
- **Image 5**: Benefits, Preference, and Convenience
- **Image 6**: Reliability and Awareness of Regulations

## Installation and Setup

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/biometric-authentication-analysis.git
cd biometric-authentication-analysis
```

2. Install the necessary dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

3. Run the Python analysis script:

```bash
python biometric_data_insights.py
```

## Images from Survey Responses

Here are the visual summaries of the survey responses:

### Image 1: Age, Gender, Occupation  
[<img src="Responses/Image1.jpg" width="400"/>](Responses/Image1.jpg)

### Image 2: Familiarity and Usage of Biometric Methods  
[<img src="Responses/Image2.jpg" width="400"/>](Responses/Image2.jpg)

### Image 3: Experience, Security Perception, and Concerns  
[<img src="Responses/Image3.jpg" width="400"/>](Responses/Image3.jpg)

### Image 4: Trust, Willingness, and Future Use  
[<img src="Responses/Image4.jpg" width="400"/>](Responses/Image4.jpg)

### Image 5: Benefits, Preference, and Convenience  
[<img src="Responses/Image5.jpg" width="400"/>](Responses/Image5.jpg)

### Image 6: Reliability and Awareness of Regulations  
[<img src="Responses/Image6.jpg" width="400"/>](Responses/Image6.jpg)

## Analysis Overview

The analysis script `biometric_data_insights.py` covers the following key steps:

- Data Cleaning: Handle missing values and clean the dataset.
- Descriptive Statistics: Summarize and visualize basic statistics.
- Visualizations: Create various plots such as histograms, bar charts, and correlation heatmaps to analyze trends in the data.
- Data Export: Save cleaned data to a new CSV file.

## Contributors

- **Shreya Ramchandra Bagal** – Project development, data collection, and analysis.
