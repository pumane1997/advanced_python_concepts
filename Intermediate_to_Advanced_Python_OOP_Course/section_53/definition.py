import pandas as pd

class Definition:
    ''' 
        This class represents the definition of a term returned by
        the dictonnary
    '''

    def __init__(self, term):
        self.term = term 

    def get(self):
        data = pd.read_csv('data.csv')
        data = tuple(data.loc[data['word'] == self.term]['definition']) 
        return data