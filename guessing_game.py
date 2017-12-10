from flask import Flask, session, redirect, url_for, escape, request
from pandas import Series
from matplotlib import pyplot
from statsmodels.tsa.ar_model import AR
from sklearn.metrics import mean_squared_error
from flask import render_template
import numpy as np

app = Flask(__name__)

start_day = 1
end_day = 100
your_prediction = 1
train = 1
test = 1


series = Series.from_csv('daily_curren_new.csv', header=0)
# split dataset
X = series.values


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start_day = int(request.form['start'])
        end_day = int(request.form['end'])
        tr, te = X[start_day:end_day], X[end_day:end_day+1]
        return redirect(url_for('predict', train = tr, test = te))
    return '''
        <form method="post">
            <p>Please enter start day for prediction: 
            <p><input type=number name=start>
            <p>Please enter the day you want to predict:
            <p><input type=number name=end>
            <p><input type=submit value=Show>
        </form>
    '''

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    train = request.args.get('train')
    test = request.args.get('test')
    train = [float(i) for i in train[1:-1].split()]
    test = [float(i) for i in test[1:-1].split()]

    npa_train = np.asarray(train, dtype=np.float32)
    npa_test = np.asarray(test, dtype=np.float32)

    ai_predic, res = calc_prediction(npa_train,npa_test)
    
    if request.method == 'POST':
        your_prediction = request.form['your_prediction']
        return redirect(url_for('result', predict = your_prediction, ai_prediction = ai_predic, result = res))
    # plot results
    pyplot.plot(train)
    #pyplot.plot(predictions, color='red')
    pyplot.show()

    return render_template('your_view.html', your_list=train)
    
    #return '''
        #<form method="post">
            #<p>Please enter your prediction:
            #<p><input type=number name=your_prediction>
            #<p><input type=submit value=Predict>
        #</form>
    #'''

@app.route('/result', methods=['GET', 'POST'])
def result():
    your_prediction = float(request.args.get('predict'))
    ai_prediction = float(request.args.get('ai_prediction'))
    final_result = float(request.args.get('result'))
    
    #return your_prediction, ai_prediction, result

    print('You predict:', your_prediction)
    print('AI predict:', ai_prediction)
    print('Real result:', final_result)

    result_explanation = 'You predict: ' + str(your_prediction) + '</br>' + 'AI predict: ' + str(ai_prediction) + '</br>' +  'Real result:' + str(final_result) + '</br></br>'

    if(abs(your_prediction - final_result) < abs(ai_prediction-final_result)):
        return result_explanation + '**********YOU WIN!************'
    else:
        return result_explanation + '************LOSER!***********'


def calc_prediction(train,test):
    # train autoregression
    model = AR(train)
    model_fit = model.fit()
    print('Lag: %s' % model_fit.k_ar)
    print('Coefficients: %s' % model_fit.params)
    # make predictions
    predictions = model_fit.predict(start=len(train), end=len(train)+len(test)-1, dynamic=False)
    for i in range(len(predictions)):
            print('predicted=%f, expected=%f' % (predictions[i], test[i]))
    error = mean_squared_error(test, predictions)
    print('Test MSE: %.3f' % error)
    return predictions[0], test[0]
    

if __name__ == "__main__":
    app.run()
