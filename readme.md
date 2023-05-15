# Twitter Algorithm Chatbot

This is a simple chatbot that can answer questions about the [Twitter algorithm](https://github.com/twitter/the-algorithm). It is built using HTML, CSS, and JavaScript.

Please note that since we are using GPT-4, the response times will be higher and every query will cost more than GPT-3.5.

## Usage

To use the chatbot, first clone the repository to your local machine:

```bash
git clone https://github.com/prateekkeshari/GitGPT.git
```

```bash
pip install -r requirements.txt
```

Then, rename the .env-example to .env and add your openai and active loop keys. [Active Loop](https://app.activeloop.ai/login)

Then, navigate to the project directory and run the app with Python:

```bash
cd GitGPT
python app.py
```

The chatbot interface will appear, allowing you to ask questions about the Twitter algorithm.

Enter your question in the input field and click the "Send" button or press the "Enter" key to submit your query. The chatbot will display a "Thinking..." message while it processes your request, and then it will display the answer to your question.

## Sample Questions

Here are some sample questions that you can ask the chatbot:

-    What does favCountParams do?
-    Is it Likes + Bookmarks, or not clear from the code?
-    What are the major negative modifiers that lower your linear ranking parameters?
-    How do you get assigned to SimClusters?
-    What is needed to migrate from one SimClusters to another SimClusters?
-    How much do I get boosted within my cluster?
-    How does Heavy ranker work? What are its main inputs?
-    How can one influence Heavy ranker?
-    Why do threads and long tweets do so well on the platform?
-    Are thread and long tweet creators building a following that reacts to only threads?
-    Do you need to follow different strategies to get most followers vs to get most likes and bookmarks per tweet?
-    How does content meta data impact virality (e.g. ALT in images)?
-    What are some unexpected fingerprints for spam factors?
-    Is there any difference between company verified checkmarks and blue verified individual checkmarks?

## Features

The chatbot interface includes the following features:

-     A responsive design that works on desktop and mobile devices.
-     A chat history that displays all previous messages.
-     A "Thinking..." message that appears while the chatbot is processing your request.
-     Support for submitting queries by clicking the "Send" button or pressing the "Enter" key.

## Customization

You can customize the appearance and behavior of the chatbot by modifying the CSS and JavaScript code in the `index.html` file. For example, you can change the font family, font size, background color, and other properties to match your website's design.

## Disclaimer

This chatbot is for educational purposes only and should not be used as a substitute for professional advice. The information provided by the chatbot may not be accurate or up-to-date, and you should always verify any information before relying on it.
