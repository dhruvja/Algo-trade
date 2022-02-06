# Algorithmic trading
A python script which buys and sells stocks or cryptocurrencies automatically 

## How to use
- Open the indiannse.py for stock trading and enter the stock symbol to continue.
- Open the crypto.py for crypo trading and enter the crypto symbol to continue.

## Stock Data
- The script uses web scraping to get the price details from yahoo finance based on which the decisions are made.

## Disclaimer

This project is under development and is not fully completed. So it might have few errors which will be solved to improve the effectiveness of the algorithm.

## The Algorithm

The algorithm is based on a simple formula. The bot buys the stock as soon as the script starts running. When the price of stock drops below the threshold value, the bot sells the 
stock automatically. It wont buy the stock unless the value is above the threshold value. So the bot buys and sells the bot based on the threshold value. And the threshold value
changes every second.

## About the Threshold Value

Threshold limit is 0.04% of the price of stock at the time of buy/sell.

#### When the stock is sold

As the value of the stock increases, the threshold value is the threshold limit subtracted by the highest stock price.
If the highest stock price is suppose 50000 and threshold limit is 20
```
threshold value = highest value - threshold value
                = 50000 - 20
                = 49980
```
So if the stock price goes below the above value, the stock is sold automatically.


#### When the stock is bought

As the value of stock decreases, the threshold value is the sum of threshold limit and lowest stock price.
If the lowest price is suppose 40000 and threshold limit is 20 
```
threshold value = lowest value - threshold value
                = 40000 + 20
                = 40020
```
So if the stock price goes beyond the above value, the stock is bought automatically.



## SWOT Analysis

#### Strengths

- Protects you from heavy losses since before the your stocks dip further, they are sold automatically.
- Also gives you the extra gain when the price dips and rises again.
- No need to worry about the bear or bull run since the algo gets adjusted to the situation
- Gets more gain than the normal traders

#### Weakness

- When there is sudden dip and rise, there might be a slight loss.
- Sudden rise and dips would lead to buy/sell at the wrong time and could incur a slight loss

#### Opportunites

- Traders dont need to study the market and make decisions based on them since the bot does it automatically
- ML and AI could be implemented in tacking the weakness and improving the effectiveness of the bot.
- Using the previous data, the bot can make predictions on which future trades can be set
- Bot can guide us when and where to trade based on the previous information and experience(due to ML)

#### Threats

- Due to network error, some trades can fail to execute which can incur some losses.

## Basic Requirements

- A strong internet connection
- A PC or laptop which should run 24/7 and be able to run and process information all day
- A trading account

## Note
- Feel free to use the code and update it to improve the effectiveness and tackle the errors.

