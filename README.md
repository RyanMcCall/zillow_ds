# What Drives Home Value

## Description
---

You are a junior data scientist on the Zillow data science team and recieve the following email in your inbox:

> We want to be able to predict the values of single unit properties that the tax district assesses using the property data from those whose last transaction was during the "hot months" (in terms of real estate demand) of May and June in 2017. We also need some additional information outside of the model.

> Zach lost the email that told us where these properties were located. Ugh, Zach :-/. Because property taxes are assessed at the county level, we would like to know what states and counties these are located in.

> We'd also like to know the distribution of tax rates for each county.

> The data should have the tax amounts and tax value of the home, so it shouldn't be too hard to calculate. Please include in your report to us the distribution of tax rates for each county so that we can see how much they vary within the properties in the county and the rates the bulk of the properties sit around.

> Note that this is separate from the model you will build, because if you use tax amount in your model, you would be using a future data point to predict a future data point, and that is cheating! In other words, for prediction purposes, we won't know tax amount until we know tax value.

> -- The Zillow Data Science Team

You wonder how you can recieve an email from the entire data science team at once, but figure it's best to get started on the project.

### Specification
#### Audience
Your customer is the zillow data science team. state your goals as if you were delivering this to zillow. They have asked for something from you and you are basically communicating in a more concise way, and very clearly, the goals as you understand them and as you have taken and acted upon through your research.

#### Deliverables
What should the zillow team expect to receive from you? Again, as you were communicating to them, not to your instructors.

1. A report (in the form of a presentation, both verbal and through a slides)

The report/presentation slides should summarize your findings about the drivers of the single unit property values. This will come from the analysis you do during the exploration phase of the pipeline. In the report, you should have visualizations that support your main points.

The presentation should be no longer than 5 minutes, and consist of 3-5 slides.

2. A github repository containing your work.

This repository should consist of at least 1 jupyter notebook that walks through the pipeline, but you may wish to split your work among 2 notebooks, one for exploration, and one for modeling.

Make sure your notebooks answer all the questions posed in the email from the Zillow data science team.

The repository should also contain the .py files necessary to reproduce your work, and your work must be reproducible by someone with their own env.py file.

## How to Reproduce
---

### First clone this repo

### Acquire 
* Must include `env.py` file in directory.
    * Contact [Codeup](https://codeup.com/contact/) to request access to the MySQL Server that the data is stored on.
    * `env.py` should include the following variables
        * `user`
        * `password`
        * `host`

* See the acquire walkthrough for the code to run to create a csv with the FIPS data and the zillow data.
    * This is necessary to run `get_data()`, as it will look for the files to join together.

### Preparation
* `get_and_clean_data()` will run the acquire function so you only need to run this one to get the data at further stages of the pipeline.