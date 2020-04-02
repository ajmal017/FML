from models.backtest import Backtest
import datetime

def run_test():

    pf_value = 1000000
    start_date = datetime.datetime(2005, 1, 13)
    end_date = datetime.datetime(2019, 1, 13)

    b = Backtest(["AAPL", "AMZN", "BRK.B"], start_date, end_date, pf_value, False)

    after_value, positions = b.simulate({'lookback_period': 20, 'strategy_threshold': .055}, False)

    rtn = ((after_value - pf_value) / pf_value) * 100

    print(b.portfolio.positions)

    print(str(rtn) + "%")
    
    b.plot_value(pf_value, start_date, end_date)
