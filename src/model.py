import pandas as pd

class TennisNaiveBayes:
    def __init__(self, csv_path="data/Tennis.csv"):
        self.csv_path = csv_path
        self.load_data()

    def load_data(self):
        self.df = pd.read_csv(self.csv_path)

    def cond_prob(self, feature, value, play_value):
        subset = self.df[self.df['Play'] == play_value]
        return len(subset[subset[feature] == value]) / len(subset)

    def predict(self, outlook, temp, humidity, wind):
        self.load_data()

        play_yes = len(self.df[self.df['Play'] == 'Yes']) / len(self.df)
        play_no = len(self.df[self.df['Play'] == 'No']) / len(self.df)

        likelihood_yes = (
            self.cond_prob('Outlook', outlook, 'Yes') *
            self.cond_prob('Temperature', temp, 'Yes') *
            self.cond_prob('Humidity', humidity, 'Yes') *
            self.cond_prob('Wind', wind, 'Yes') *
            play_yes
        )

        likelihood_no = (
            self.cond_prob('Outlook', outlook, 'No') *
            self.cond_prob('Temperature', temp, 'No') *
            self.cond_prob('Humidity', humidity, 'No') *
            self.cond_prob('Wind', wind, 'No') *
            play_no
        )

        return "Yes" if likelihood_yes > likelihood_no else "No"

    def add_data(self, outlook, temp, humidity, wind, play):
        self.load_data()

        new_row = {
            "Day": len(self.df) + 1,
            "Outlook": outlook,
            "Temperature": temp,
            "Humidity": humidity,
            "Wind": wind,
            "Play": play
        }

        self.df = self.df.append(new_row, ignore_index=True)
        self.df.to_csv(self.csv_path, index=False)
