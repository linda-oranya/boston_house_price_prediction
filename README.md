# Boston House Prediction Application

The Boston House Prediction Application is a Python application for predicting house prices with the load_boston data. The Application is also deployed on Heroku and can be accessed via https://boston-house-price-predictor.herokuapp.com/



## Usage

```import requests

url = "https://boston-house-price-predictor.herokuapp.com/predict"

json_input = {"inputs": [[1.1069e-01, 0.0000e+00, 1.3890e+01, 1.0000e+00, 5.5000e-01,
              5.9510e+00, 9.3800e+01, 2.8893e+00, 45.0000e+00, 2.7600e+02,
              1.6400e+01, 3.9690e+02, 1.7920e+01]]}

r = requests.post(url,json=json_input)

# returns price prediction
r.text

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)