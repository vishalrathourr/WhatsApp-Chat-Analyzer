# WhatsApp Chat Analysis Tool

This Python project allows you to analyze your WhatsApp group or individual chat by uploading a text file exported from WhatsApp. The tool provides various statistics and visualizations to help you understand your chat activity. You can also access these features through the [web application](https://whatsanalysis.streamlit.app/).


## Features

- **Total Messages:** Calculate the total number of messages in the chat.
- **Total Number of Words:** Count the total number of words in the chat.
- **Number of Media Shared:** Determine the number of media files (images, videos, etc.) shared in the chat.
- **Number of Links Shared:** Find out how many web links were shared in the chat.
- **Monthly and Daily Timeline:** Display graphs showing user activity over time, both on a monthly and daily basis.
- **Most Busy Months and Days:** Create bar plots to highlight the most active months and days.
- **Weekly Activity Heatmap:** Generate a heatmap to visualize weekly activity with time.
- **Word Cloud:** Create a word cloud to visualize the most frequently used words in the chat.
- **Bar Plot for Most Used Words:** Display a bar plot of the top 10 most used words in the chat.
- **Top 5 Busy Users:** Identify the top 5 most active users and their message percentage in the group.
- **Emoji Usage DataFrame:** Provide a DataFrame of used emojis in the group with their counts.


## Limitations

- **Date and Time Format**: This tool is designed to work with WhatsApp chat exports in which the date and time format follows this pattern: "dd/mm/yy, hh:mm a " eg. "26/02/23, 5:15 pm". If your chat export uses a different date and time format, the tool may not work as expected.

## Usage

1. Visit the [web application](https://whatsanalysis.streamlit.app/).

2. Upload your WhatsApp chat export text file (typically named `chat.txt`).

3. Select the *"All"* or *"Select any specific user"* and Click on the **Show Analysis** button you're interested in, and the tool will generate the corresponding statistics and visualizations.

4. Now you can see the generated visualizations and reports.


## Project Structure

- `app.py`: The main Python script for the Streamlit web application.
- `helper.py`: Contains functions and utilities used by the main application for data analysis and visualization.
- `preprocessor.py`: Contains functions for preprocessing the raw chat data.
- `requirements.txt`: A file listing the required Python libraries and their versions for this project.


## Feedback and Contributions

If you encounter any issues, have suggestions for improvements, or would like to contribute to this project, please feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/yourusername/whatsapp-chat-analysis).

## Disclaimer

This project is for educational and personal use only. Please respect privacy and confidentiality when analyzing chat data.


Enjoy analyzing your WhatsApp chat data with this tool! If you have any questions or need assistance, feel free to contact us.

Vishal Rathour
E-Mail: vishdsc@gmail.com
Github: https://github.com/vishalrathourr
