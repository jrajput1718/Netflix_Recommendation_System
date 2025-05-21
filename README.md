 🎬 Netflix Movie Recommendation System

This project is a **Content-Based Movie Recommendation System** built using **Python, Django, TF-IDF, and Cosine Similarity**. It recommends similar movies based on user input, using a real-world Netflix dataset.

 🔍 Features

- 🔎 Search for any movie from the dataset.
- 🧠 Recommends top 5 similar movies using **TF-IDF vectorization** and **Cosine Similarity**.
- 🎨 Clean and responsive UI built with **Bootstrap**.
- ⚙️ Built with **Django** framework.
- 📂 Uses real **Netflix Movies and TV Shows dataset**.

---

🧑‍💻 Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap
- **Machine Learning:** TF-IDF Vectorizer, Cosine Similarity (from `sklearn`)
- **Data Handling:** Pandas
- **Dataset:** [Netflix Movies Dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows)

---

🛠 Installation Steps

1. Clone the Repository

```bash
git clone https://github.com/your-username/netflix-recommendation-system.git
cd netflix-recommendation-system
2.Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies

pip install -r requirements.txt
⚠️ If you face encoding issues, read the dataset using encoding='latin1'.

4. Add the Dataset
Download the dataset from Kaggle and place netflix_titles.csv inside your project folder.

5. Run the Server

python manage.py runserver
Go to http://127.0.0.1:8000 to use the app.

📁 Project Structure

netflix-recommendation-system/
├── manage.py
├── recommender/                  # Django app
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── recommender/
│   │       ├── index.html
│   │       └── recommend.html
├── netflix_titles.csv            # Dataset file
├── requirements.txt
└── README.md
📷 Screenshots
Home Page:

Recommendations:

✅ Future Improvements
Add genre filtering

Integrate TMDB API for dynamic movie posters

Deploy on Heroku or Render

🙌 Acknowledgements
Dataset: Netflix Shows - Kaggle

Built with using Django & Python
