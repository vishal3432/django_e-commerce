# E-Commerce Platform

A high-performance Django e-commerce application featuring an AI-driven product recommendation system optimized with Cython. This project demonstrates the integration of web development, machine learning, and low-level performance tuning.

## 🚀 Live Demo
You can access the live application here: 
**[https://vishalsingh342.pythonanywhere.com/](https://vishalsingh342.pythonanywhere.com/)**

## ✨ Features
* **Product Management:** Dynamic product display with category filtering and tagging.
* **AI Recommendations:** Content-based filtering logic that analyzes user "likes" to suggest relevant products.
* **Performance Optimization:** Computation-heavy similarity scoring implemented in **Cython** for C-level execution speed.
* **User Interactions:** Functional "Like" system to train the recommendation engine in real-time.
* **Full E-commerce Flow:** Includes a session-based shopping cart and a complete checkout process.
* **Modern UI:** Responsive design using CSS Grid and Flexbox for a professional look and feel.

## 🛠️ Technology Stack
* **Backend:** Django (Python 3.10+)
* **Optimization:** Cython (C-Extensions)
* **Data Processing:** NumPy
* **Database:** SQLite3
* **Deployment:** PythonAnywhere

## ⚙️ Installation & Local Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/vishalsingh342/ecommerce_ai_project.git](https://github.com/vishalsingh342/ecommerce_ai_project.git)
    cd ecommerce_ai_project
    ```

2.  **Environment Setup:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Database Configuration:**
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```

4.  **Build Cython Modules:**
    *(Requires Microsoft C++ Build Tools)*
    ```bash
    python setup.py build_ext --inplace
    ```

5.  **Run Server:**
    ```bash
    python manage.py runserver
    ```

## 📊 Project Structure
* `core/`: Project settings and URL configurations.
* `shop/`: Main application logic, including models, views, and templates.
* `shop/recommender.pyx`: Cython source file for optimized recommendation inference.
* `setup.py`: Compilation script for Cython extensions.

---
**Developed by:** Vishal Singh  
**Date:** February 2026
