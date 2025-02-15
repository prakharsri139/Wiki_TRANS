# Wikipedia Search and Translation Web Application

This project is a Django-based web application that allows users to search for topics on Wikipedia and view their summaries. Additionally, the application supports the translation of these summaries into different languages. It is designed with a user-friendly interface, utilizing Django for backend functionality, and includes a translation feature powered by the `translate` library.

## Features

1. **Wikipedia Search**: 
   - Users can enter a search term, and the application will fetch the summary of the corresponding Wikipedia page.
   - The results are displayed on the same page for a seamless user experience.

2. **Language Translation**: 
   - After retrieving the summary, users have the option to translate the text into different languages.
   - Supported languages include English, Spanish, French, German, Chinese, and Hindi. More languages can be easily added by extending the dropdown list.

3. **Chunked Translation**: 
   - The application splits large text summaries into smaller chunks to ensure efficient and accurate translation without exceeding any API or library limits.

4. **Responsive Design**: 
   - The web application is designed to be fully responsive, providing an optimal user experience across desktop and mobile devices.

## Tech Stack

- **Backend**: Django 5.x
- **Frontend**: HTML, CSS (Tailwind for styling)
- **API Integration**: Wikipedia API for fetching data, `translate` library for language translation
- **Parser**: BeautifulSoup (with `lxml` for better HTML parsing)
- **Translation**: `translate` library for translating text

## Installation

Follow these steps to run the project locally on your machine:

### Prerequisites

- Python 3.8 or higher
- Django 5.x or higher

### Step-by-step Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/wiki-trans.git
   cd wiki-trans
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Run the Django development server**:
   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://127.0.0.1:8000/`.

## Project Structure

```
wiki-trans/
│
├── main/
│   ├── migrations/
│   ├── static/
│   │   └── styles.css
│   ├── templates/
│   │   └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── wiki_trans/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── requirements.txt
```

### Key Files:

- **`main/views.py`**: Contains the `wiki_search` view that handles both Wikipedia search and translation.
- **`main/templates/index.html`**: The HTML template responsible for rendering the search form and displaying results.
- **`main/static/styles.css`**: Custom CSS for styling the application.
- **`wiki_trans/settings.py`**: Django settings configuration for the project.
- **`wiki_trans/urls.py`**: URL routing configuration for the project.

## How It Works

### 1. **Search Functionality**:
   - When a user enters a topic in the search bar and clicks the "Search" button, the application queries the Wikipedia API for a summary of the given topic.
   - The summary is displayed on the webpage.

### 2. **Translation**:
   - After the search result is displayed, the user can choose a target language from a dropdown and click the "Translate" button.
   - The application translates the summary text into the selected language using the `translate` library, and the translated result is displayed below the original summary.

### 3. **Text Chunking for Translation**:
   - If the summary text is large, it is divided into smaller chunks to prevent exceeding the translation library’s limits. Each chunk is translated separately, and the results are combined.

### 4. **Responsive Design**:
   - The application is built with a responsive layout, ensuring that users have a seamless experience regardless of their device type (desktop, tablet, or mobile).

## Future Enhancements

- **Add more languages**: Extend the list of supported languages for translation.
- **Error Handling**: Improve error messages and handling (e.g., when Wikipedia pages are not found).
- **Additional API Integrations**: Integrate additional features such as displaying images or references related to the searched Wikipedia topic.
- **Improve User Interface**: Enhance the UI/UX with more modern design patterns, animations, and more intuitive interactions.

## Contributing

Contributions are welcome! If you have any suggestions or improvements for the project, feel free to fork the repository, make your changes, and submit a pull request.

### Steps to Contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request with a description of your changes.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgments

- **Django**: For providing a powerful framework for building web applications.
- **Wikipedia API**: For offering free access to Wikipedia data.
- **translate library**: For providing translation services.
- **BeautifulSoup**: For scraping and parsing HTML data.

---

This README file provides a comprehensive overview of the project, including setup instructions, functionality, and details about how the application works. Let me know if you need any further modifications!
