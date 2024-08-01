from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__)

patterns_responses = {
    r"my name is (.*)": ["Hello %s, How can I assist you with your financial needs today?"],
    r"(hi|hey|hello|good morning|good evening)": ["Hello! How can I help you today?"],
    r"stocks|stock(.*\b)?( market|invest in stocks)(\b.*)?": ["Stocks are shares of ownership in a company. They can be risky but offer high returns. Diversify your portfolio to manage risk. Risk Level: High Return. Potential risk- High. Example- Buying shares of Apple Inc. (AAPL)."],
    r"(.*\b)?(bonds|invest in bonds)(\b.*)?": ["Bonds are a type of loan to a company or government. They are generally safer than stocks but offer lower returns.Risk Level: Low to Medium Return Potential: Low to Medium Example: U.S. Treasury bonds, municipal bonds, corporate bonds."],
    r"(.*\b)?(mutual funds|invest in mutual funds)(\b.*)?": ["Mutual funds pool money from many investors to buy a diversified portfolio of stocks, bonds, or other securities, managed by professionals.Risk Level: Varies (depending on the underlying assets)Return Potential: Varies Example: Vanguard 500 Index Fund (VFIAX)."],
    r"(.*\b)?(ETFS|exchange-traded funds|invest in etfs)(\b.*)?": ["ETFs are similar to mutual funds but trade like stocks on an exchange. They offer diversification and are generally low-cost.Risk Level: Varies (depending on the underlying assets). Return Potential: Varies Example: SPDR S&P 500 ETF (SPY)."],
    r"(.*\b)?(real estate|invest in real estate)(\b.*)?": ["Real estate involves buying property to rent or sell. It can be profitable but requires significant capital and management.Risk Level: Medium to High Return Potential: Medium to High Example: Purchasing rental properties, investing in a REIT like Vanguard Real Estate ETF (VNQ)."],
    r"(.*\b)?(commodities|invest in commodities)(\b.*)?": ["Commodities are physical goods like gold, silver, and oil. They can be volatile but can act as a hedge against inflation.Risk Level: High Return Potential: High Example: Buying gold bars, investing in commodity ETFs like SPDR Gold Shares (GLD)."],
    r"(.*\b)?(cryptocurrency|invest in cryptocurrencies)(\b.*)?": ["Cryptocurrencies are digital assets using blockchain technology. They are highly volatile and speculative.Risk Level: Very High Return Potential: Very High Example: Bitcoin (BTC), Ethereum (ETH)"],
    r"(.*\b)?(CDS|certificates of deposit|invest in cds)(\b.*)?": ["CDs are low-risk savings products offered by banks with a fixed interest rate and maturity date.Risk Level: Low Return Potential: Low Example: A 1-year CD from a bank."],
    r"(.*\b)?(savings accounts|invest in savings accounts)(\b.*)?": ["Savings accounts offer low returns but are very safe and provide easy access to your money.Risk Level: Very Low Return Potential: Very Low Example: High-yield savings accoun"],
    r"quit": ["Thank you for using the financial advisor chatbot. Goodbye!"]
}

def match_pattern(input_text):
    for pattern, responses in patterns_responses.items():
        regex = re.compile(pattern, re.IGNORECASE)
        match = regex.match(input_text)
        if match:
            response = responses[0]
            if "%s" in response:
                response = response % match.groups()
            return response
    return "I'm sorry, I don't understand your question."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot_response', methods=['POST'])
def chatbot_response():
    user_input = request.json.get('user_input')
    response = match_pattern(user_input)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)
