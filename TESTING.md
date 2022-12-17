## Testing 

### Automated Testing - Python
When I first ran my automated Python tests, there was one statement missing in views.py and one statement missing in models.py:

![98% coverage in views.py](static/readme/coverage-views-1.png)

![95% coverage in models.py](static/readme/coverage-models-1.png)

The final test coverage is at 100%:
![100% coverage in all tests](static/readme/coverage-final.png)


These tests can be found in my [planets app](https://github.com/StephHjar/me1-planet-tracker/tree/main/planets)

### Automated Testing - JavaScript
I also wrote automated tests using Jest for my JavaScript password validator, and all tests pass:

![All Jest tests passing in terminal](static/readme/jest-tests.png)

These tests can be found in my [js folder](https://github.com/StephHjar/me1-planet-tracker/tree/main/static/js/tests).

### Validator Testing - HTML
When I first ran my HTML code through the validator, an error was found on the home page: my ```<footer>``` tag was outside my ```<body>``` tag:
![HTML validator error](static/readme/html-validator-error.png)

- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2Fnu%2F%3Fdoc%3Dhttps%253A%252F%252Fcode-institute-org.github.io%252Flove-running-2.0%252Findex.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#css)

  ### Manual Testing