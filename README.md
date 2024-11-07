<h1> Financial advisor chatbot </h1>
<p> This is a financial advisor chatbot built using Flask as the backend framework. 
  The chatbot provides basic financial advice on stocks, bonds, mutual funds, ETFs, real estate, commodities, cryptocurrencies, and more.
  The chatbot can also greet users and handle simple queries.
  Additionally, the chatbot is integrated with the 
  <strong>OpenAI API</strong> 
  to provide more sophisticated and personalized financial advice based on natural language processing and advanced AI capabilities.
</p>
 <h2>Features</h2>
 <p>
    <ul>
        <li>Responds to user queries about various investment options (stocks, bonds, real estate, etc.).</li>
        <li>Uses regular expressions (regex) to match specific patterns in user input.</l
        <li>Optionally integrates with the OpenAI API to provide more sophisticated answers.</li>
        <li>Basic web UI where users can chat with the bot in real time.</li>
    </ul>
 </p>
 <h2>Tech Stack</h2>
    <ul>
        <li><strong>Backend:</strong> Flask (Python)</li>
        <li><strong>Frontend:</strong> HTML, CSS, JavaScript</li>
        <li><strong>API Integration</strong>: OpenAI API for advanced responses</li>
    </ul>
     <h2>Project Structure</h2>
    <pre>
.
├── app.py                   # Main Flask application
├── templates/
│   └── index.html           # HTML template for the chatbot UI
├── static/
│   └── styles.css           # CSS file for styling the chatbot interface
    </pre>
    <h2>Requirements</h2>
    <ul>
        <li>Python 3.x</li>
        <li>Flask (<code>pip install flask</code>)</li>
    </ul>
    <h2>Installation</h2>
    <ol>
        <li>Clone the repository:
            <pre>git clone https://github.com/yourusername/financial-advisor-chatbot.git
cd financial-advisor-chatbot</pre>
        </li>
        <li>Install Flask:
            <pre>pip install flask</pre>
        </li>
        <li>Run the application:
            <pre>python app.py</pre>
        </li>
        <li>Open your browser and navigate to <code>http://127.0.0.1:5000</code> to interact with the chatbot.</li>
    </ol>
    <h2>How It Works</h2>
    <p>The <code>patterns_responses</code> dictionary in <code>app.py</code> contains regex patterns mapped to predefined responses. The chatbot matches user inputs to these patterns and returns the appropriate response. If no pattern matches, the chatbot returns a default message indicating that it didn’t understand the query.</p>
    <h2>File Descriptions</h2>
    <ul>
        <li><strong>app.py</strong>: The main application file, handling routes and API endpoints for chatbot responses.</li>
        <li><strong>templates/index.html</strong>: The HTML file for the chatbot's web interface.</li>
        <li><strong>static/styles.css</strong>: The CSS file for styling the chatbot UI.</li>
    </ul>
    <h2>Usage</h2>
    <ol>
        <li>Start the Flask server by running:
            <pre>python app.py</pre>
        </li>
        <li>Open your browser and navigate to <code>http://127.0.0.1:5000</code>.</li>
        <li>Enter your financial questions in the chatbox, such as:
            <ul>
                <li>"Hi" or "Hello" — for a greeting.</li>
                <li>"Tell me about bonds" — for advice on bonds.</li>
                <li>"What are mutual funds?" — for information on mutual funds.</li>
                <li>"Quit" — to exit the chat.</li>
            </ul>
        </li>
    </ol>
    <h2>Example Queries</h2>
    <ul>
        <li>"What are stocks?" — Learn about stocks as an investment.</li>
        <li>"How do I invest in ETFs?" — Get advice on exchange-traded funds.</li>
        <li>"Tell me about cryptocurrency." — For details on cryptocurrency as an investment.</li>
    </ul>
    <h2>Additional Notes</h2>
    <p>This chatbot is intended for general financial information and educational purposes. For specific investment decisions, please consult a certified financial advisor.</p>

    

