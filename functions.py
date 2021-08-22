import yfinance as yf
import pandas as pd

def CalculateData(stockName, method):
    method = str(method).lower()

    stock = yf.Ticker(stockName)
    data = stock.history()
    _previousDay = data[-2:-1]

    if method == "floor":
        FloorCalculate(previousDay=_previousDay)
    elif method == "woodie":
        WoodieCalculate(previousDay=_previousDay)
    elif method == "fibonacci":
        FibonacciCalculate(previousDay=_previousDay)
    elif method == "demarks":
        DeMarkCalculate(previousDay=_previousDay)
    elif method == "camarilla":
        CamarillaCalculate(previousDay=_previousDay)
    else:
        return "Wrong Method Name! Try Again!"


def WoodieCalculate(previousDay):
    close = float(previousDay['Close'])
    low = float(previousDay['Low'])
    high = float(previousDay['High'])

    pivot = (high + low + (2 * close)) / 4

    resistance_1 = (2 * pivot) - low
    resistance_1 = format(resistance_1, ".2f")

    resistance_2 = pivot + high - low
    resistance_2 = format(resistance_2, ".2f")

    support_1 = (2 * pivot) - high
    support_1 = format(support_1, ".2f")

    support_2 = pivot - high + low
    support_2 = format(support_2, ".2f")

    pivot = format(pivot, "0.2f")

    data = [[support_2, support_1, pivot, resistance_1, resistance_2]]

    dataFrame = pd.DataFrame(data, index=['woodie'], columns=["support_2", "support_1", "pivot", "resistance_1", "resistance_2"])

    return dataFrame


def FloorCalculate(previousDay):
    close = float(previousDay['Close'])
    low = float(previousDay['Low'])
    high = float(previousDay['High'])

    pivot = (high + low + close) / 3

    resistance_1 = (2 * pivot) - low
    resistance_1 = format(resistance_1, ".2f")

    resistance_2 = pivot + high - low
    resistance_2 = format(resistance_2, ".2f")

    resistance_3 = high + (2 * (pivot - low))
    resistance_3 = format(resistance_3, ".2f")

    support_1 = (2 * pivot) - high
    support_1 = format(support_1, ".2f")

    support_2 = pivot - high + low
    support_2 = format(support_2, ".2f")

    support_3 = low - (2 * (high - pivot))
    support_3 = format(support_3, ".2f")

    pivot = format(pivot, "0.2f")

    data = [[support_3, support_2, support_1, pivot, resistance_1, resistance_2, resistance_3]]

    dataFrame = pd.DataFrame(data, index=['floor'], columns=["support_3", "support_2", "support_1", "pivot", "resistance_1", "resistance_2", "resistance_3"])

    return dataFrame


def FibonacciCalculate(previousDay):
    close = float(previousDay['Close'])
    low = float(previousDay['Low'])
    high = float(previousDay['High'])

    pivot = (high + low + close) / 3

    resistance_1 = pivot + ((high - low) * 0.382)
    resistance_1 = format(resistance_1, ".2f")

    resistance_2 = pivot + ((high - low) * 0.618)
    resistance_2 = format(resistance_2, ".2f")

    resistance_3 = pivot + ((high - low) * 1.000)
    resistance_3 = format(resistance_3, ".2f")

    support_1 = pivot - ((high - low) * 0.382)
    support_1 = format(support_1, ".2f")

    support_2 = pivot - ((high - low) * 0.618)
    support_2 = format(support_2, ".2f")

    support_3 = pivot - ((high - low) * 1.000)
    support_3 = format(support_3, ".2f")

    pivot = format(pivot, "0.2f")

    data = [[support_3, support_2, support_1, pivot, resistance_1, resistance_2, resistance_3]]

    dataFrame = pd.DataFrame(data, index=['fibonacci'], columns=["support_3", "support_2", "support_1", "pivot", "resistance_1", "resistance_2", "resistance_3"])

    return dataFrame


def DeMarkCalculate(previousDay):
    close = float(previousDay['Close'])
    low = float(previousDay['Low'])
    high = float(previousDay['High'])
    openValue = float(previousDay['Open'])

    if close < openValue:
        pivot = high + 2 * low + close
    elif close > openValue:
        pivot = 2 * high + low + close
    else:
        pivot = high + low + 2 * close

    resistance_1 = (pivot / 2) - low
    resistance_1 = format(resistance_1, ".2f")

    support_1 = (pivot / 2) - high
    support_1 = format(support_1, ".2f")

    pivot = format(pivot / 4, "0.2f")

    data = [[support_1, pivot, resistance_1]]

    dataFrame = pd.DataFrame(data, index=['demark'], columns=["support_1", "pivot", "resistance_1"])

    return dataFrame


def CamarillaCalculate(previousDay):
    close = float(previousDay['Close'])
    low = float(previousDay['Low'])
    high = float(previousDay['High'])

    pivot = (high + low + close) / 3

    resistance_1 = (high - low) * 1.1 / 12 + close
    resistance_1 = format(resistance_1, ".2f")

    resistance_2 = (high - low) * 1.1 / 6 + close
    resistance_2 = format(resistance_2, ".2f")

    resistance_3 = (high - low) * 1.1 / 4 + close
    resistance_3 = format(resistance_3, ".2f")

    resistance_4 = (high - low) * 1.1 / 2 + close
    resistance_4 = format(resistance_4, ".2f")

    support_1 = close - (high - low) * 1.1 / 12
    support_1 = format(support_1, ".2f")

    support_2 = close - (high - low) * 1.1 / 6
    support_2 = format(support_2, ".2f")

    support_3 = close - (high - low) * 1.1 / 4
    support_3 = format(support_3, ".2f")

    support_4 = close - (high - low) * 1.1 / 2
    support_4 = format(support_4, ".2f")

    pivot = format(pivot, "0.2f")

    data = [[support_4, support_3, support_2, support_1, pivot, resistance_1, resistance_2, resistance_3, resistance_4]]

    dataFrame = pd.DataFrame(data, index=['camarilla'], columns=["support_4", "support_3", "support_2", "support_1", "pivot", "resistance_1", "resistance_2", "resistance_3", "resistance_4"])

    return dataFrame
