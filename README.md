# travelapp
Travel app comparing Strava API and TFL api to demonstrate money saved!

# Main plan

* get strava journeys (time period)
    * plot strava journeys (all short journeys and commutes)
    * optional : focus on commutes
* cost calculation
    * get start and end points of joureny
    * run through journey planner options
    - HERE
    - GOOGLE
    - TFL
    - others - citymapper?
    * save route options to database
* for routes in database
    * calculate costs of journeys from TFL api
    * save costs of journeys in the database
* get TFL data from TFL api
    * full picture of travel
* get TFL travelcard costs (per zones)
* produce comparisons
    * direct estimations
    - TFL journeys v.s. TFL travel card costs - do you save money at the moment
    - TFL journeys + commutes v.s. TFL travel card costs
    - TFL journeys + commutes + additional journeys inside London v.s. travel card costs

# Comments
* need a client side database? (minimise multiple API calls)
* simplify routes from strava - start and end points must be similar (with 500m radius?)
* aggregate options from journey planner
    * does google or citymapper also give you costs?

# modelling and predictions
* number of commutes needed to save money
* estimated commutes per year?
    * seasonal effects of commutes? (estimated rainfall / wind)
* does this work for multiple people?
    * do you need a large population to model properly

