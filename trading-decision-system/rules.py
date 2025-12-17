def trade_decision(trend, structure, momentum):
    """
    Determines whether to trade based on market conditions.
    """

    if trend == "bearish" and structure == "range":
        return "NO TRADE"

    if trend == "bullish" and momentum == "strong":
        return "TRADE"

    return "WAIT"
