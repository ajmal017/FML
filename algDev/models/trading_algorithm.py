from models.equity import Equity
from algorithms.model_collection import ModelCollection
from algorithms.voter import Voter
from preprocessing import data_generator

class TradingAlgorithm:
    """ This is the main class. You would make a TradingAlgorithm 
    object to actually generate your predictions on and pass them into
    an AssetAllocationAlgorithm.
    
    Returns:
        TradingAlgorithm -- Object to be used to retrain and predict data points
    """
    self.algorithm_types = [
        'cnn',
        'svm'
    ]
    def __init__(self, tickers, features, type = 'svm', data_lookback_period = 10, label_threshold = 0.015, label_period = 10, data_splits = [0.8, 0.2], cnn_split=0):
        """Initialize the TradingAlgorithm Object
        
        Arguments:
            tickers {string array} -- tickers of the securities to include
            features {string array} -- indicators to include with parameters attached with underscores, more in README
        
        Keyword Arguments:
            type {str} -- [what type of algorithm the models will be] (default: {'svm'})
            data_lookback_period {int} -- [how long the input data should look back] (default: {10})
            label_threshold {float} -- [the amount the equity is expected to increase in order to be successful] (default: {0.015})
            label_period {int} -- [the length of time before the equity is exited] (default: {10})
            data_splits {list} -- [train,validation,test splits. can just be train,test] (default: {[0.8, 0.2]})
            cnn_split {int} -- [how many cnns we want (if necessary)] (default: {0})
        """
        super().__init__()
        assert type in self.algorithm_types
        self.type = type
        self.features = features
        self.eqs = [Equity(t) for t in tickers]
        self.params = {'length': data_lookback_period, 'threshold':label_threshold, 'period': label_period, 'cnn_split': cnn_split, 'data_splits': data_splits}
        self.voter = Voter()
        self.models = [ModelCollection(t, type, features, self.params) for t in tickers]

        self.initialize_models()

    def initialize_models(self):
        """Trains the model collections
        """
        for model in self.models:
            model.train_models()

    def predict(self, date):
        """ Generate a prediction for each equity for this algorithm
        
        Arguments:
            date {datetime} -- date to make the prediction on
        
        Returns:
            dictionary -- key - ticker, value - tuple of prediction (0 or 1) and model accuracy
        """
        start_index = self.eqs[0].get_index_from_date(date)
        end_index = start_index + self.params['length']
        predictions = {}
        for i, eq in enumerate(self.eqs):
            new_feature = data_generator.get_subset(eq, self.features, self.type, self.params['length'], self.params['threshold'], self.params['period'])
            predictions.update({eq.ticker: Voter.predict(self.models[i], new_feature)})
        
        return predictions