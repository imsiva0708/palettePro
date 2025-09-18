# PalettePro

PalettePro is an intelligent recipe recommendation web application that helps users discover new dishes based on the ingredients they have on hand. By leveraging Google Gemini's generative AI and Google Custom Search, PalettePro provides curated recipe suggestions, complete with direct links and images, tailored to the user's available ingredients.

## Features

- **Ingredient-Based Recipe Generation:**

  - Users input a list of ingredients they have.
  - The app uses Google Gemini's generative AI to suggest a list of possible dishes that can be made with those ingredients.

- **Automated Recipe Search:**

  - For each suggested dish, the app performs a Google Custom Search to find the most relevant recipe link and its title.
  - The app scrapes the recipe page to extract a high-quality image of the dish.

- **Curated Recommendations:**

  - All results are presented as a list of recipe cards, each containing the recipe title, a direct link, and an image.

- **Modern Web Interface:**
  - Built with Flask and Jinja2 templates for a responsive, user-friendly experience.
  - Custom static assets and SVGs for a visually appealing UI.

## How It Works

1. **User Input:**
   - The user enters a list of ingredients on the web interface.
2. **AI Recipe Generation:**
   - The backend calls Gemini's generative AI to generate a list of possible dishes using those ingredients.
3. **Recipe Search & Scraping:**
   - For each dish, the app uses Google Custom Search API to find the best recipe link and title.
   - The app scrapes the recipe page to extract a main image.
4. **Display Results:**
   - The app displays a list of recipe cards, each with a title, link, and image, for the user to explore.

## File Structure

- `app.py` — Flask web server, handles routes and user interaction.
- `main.py` — Orchestrates the process: gets AI-generated recipes, searches Google, and formats results.
- `gemini.py` — Handles interaction with Google Gemini generative AI for recipe suggestions.
- `googlesearch.py` — Uses Google Custom Search API to find recipe links and titles.
- `scrap.py` — Scrapes recipe pages to extract main images using BeautifulSoup.
- `stringmaker.py` — Utility functions for formatting and dictionary creation.
- `templates/` — HTML templates for rendering the web interface.
- `static/` — Static assets (images, SVGs, CSS, etc.).
- `requirements.txt` — Python dependencies.

## Setup & Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/imsiva0708/palettePro.git
   cd palettePro
   ```

2. **Create and activate a virtual environment:**

   ```sh
   python -m venv env
   # On Windows:
   .\env\Scripts\activate
   # On Unix/Mac:
   source env/bin/activate
   ```

3. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   - Create a `.env` file in the project root with the following keys:
     ```env
     GEMINI_API_KEY=your_gemini_api_key
     GOOGLE_CUSTOM_SEARCH_API_KEY=your_google_custom_search_api_key
     GOOGLE_SEARCH_ENGINE_ID=your_search_engine_id
     ```

5. **Run the application:**
   ```sh
   python app.py
   ```
   - The app will be available at `http://127.0.0.1:5000/`

## Dependencies

- Flask
- requests
- beautifulsoup4
- python-dotenv
- google-api-python-client
- google-generativeai

## Example Usage

1. Open the app in your browser.
2. Enter a list of ingredients (e.g., `onion, tomato, potato`).
3. Submit to receive a curated list of recipes you can make, each with a title, image, and direct link.

## Customization

- **UI:**
  - Modify HTML templates in `templates/` and static assets in `static/` for branding or layout changes.
- **AI Prompt:**
  - Adjust the prompt in `gemini.py` to change the style or specificity of recipe suggestions.
- **Search Logic:**
  - Tweak `googlesearch.py` or `scrap.py` to refine how recipes are found and images are extracted.

## License

This project is for educational and personal use. For commercial use or redistribution, please contact the author.

---

**PalettePro** — Discover what you can cook, starting with what you have!
