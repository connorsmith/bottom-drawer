class TempTracker:
    ''' 
    Given incoming temperature data, provides statistical information
    
    Note: Should optimize for quick information retrieval.
    '''

    def __init__(self):
        # for the mean (could also keep track of sum, but that might overflow)
        self.number_of_data_points = 0
        self.mean = 0 # initial value will be erased, otherwise would be set to None
        
        # for max and min
        self.max_temp = None
        self.min_temp = None

        # for mode (could use an array as well, but this supports any temperature)
        self.temperature_dict = {}
        self.max_occurences = 0
        self.mode = None

    def insert(self,data):
        # adds a new integer temperature data point
        self.number_of_data_points += 1
        self.mean = float(((self.number_of_data_points-1) * self.mean + data)/self.number_of_data_points)
        
        if self.max_temp == None or data > self.max_temp:
            self.max_temp = data

        if self.min_temp == None or data < self.min_temp:
            self.min_temp = data

        if data not in self.temperature_dict:
            self.temperature_dict[data] = 1
        else:
            self.temperature_dict[data] += 1

        if self.temperature_dict[data] > self.max_occurences:
            self.max_occurences == self.temperature_dict[data]
            self.mode = data

    def get_max(self,):
        # returns the highest observed temperature
        return self.max_temp

    def get_min(self,):
        # returns the lowest observed temperature
        return self.min_temp

    def get_mean(self,):
        # returns the mean recorded temperature
        return self.mean

    def get_mode(self,):
        # returns a mode (if there are multiple) of the observed temperatures
        return self.mode

    def get_number_of_points(self):
        return self.number_of_data_points

def main():
    dataPoints = [10, 10, 11, 12, 13, 9, 8, 7]

    t = TempTracker()

    for dataPoint in dataPoints:
        t.insert(dataPoint)
        print('Data points (%s), mean (%s)'%(t.get_number_of_points(),t.get_mean()))

if __name__ == "__main__":
    main()