# Loan Eligibility Prediction

## 💡 Inspiration

When you read the project's title, you're reminded of the same old type of rudimentary machine learning projects that can be found on YouTube Tutorials. But believe me when I say that this is a one-of-a-kind effort.
** What distinguishes it from the competition? ** I'm glad you asked.
- The dataset used in this project is a real one with over 250K data points.
- The dataset, like the actual world, is highly imbalanced.
- The initiative makes responsible use of artificial intelligence (it not only tells you if you are eligible for a loan, but in-case you are not, it tells you what exactly went wrong and how can you improve).

## 💻 What it does

Loan Eligibility Prediction uses Random Forest Classifier to predict whether a person is eligible for a loan or not. 

It uses the principle of **Responsible AI** and keeps the predictions transparent to the user.
Responsible AI is the practice of designing, developing, and deploying AI with good intention to empower employees and businesses, and fairly impact customers and society—allowing companies to engender trust and scale AI with confidence.

If the user is not eligible for a loan, the AI will tell you why.

Many banks have not been able to provide transparency into the process of their loan eligibility prediction systems, which can lead to some awkward conversations between clients and bank employees. Our app will help banks give a more appropriate answer to why an application was rejected, so that people are able to learn from mistakes and submit better applications next time.

## ⚙️ How it Works

- The user enters their details that include their
    - Income
    - Age
    - Experience
    - Marital Status
    - House Ownership
    - Number of Cars the person owns
    - Profession
    - State
    - Years in Current Job
    - Years in Current Address

- The app uses this data to predict whether the user is eligible for a loan or not.

- If the user is not eligible for a loan, the app will give you the option to gain insights into why.

## 🔨 How I built it
- ML: Python, Sklearn, Pandas, Numpy, Plotly, Imblearn
- UI & Backend: Streamlit

