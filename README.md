# Ride-with-me

[![Build Status](https://travis-ci.org/naibor/Ride-with-me.svg?branch=Develop)](https://travis-ci.org/naibor/Ride-with-me)[![Coverage Status](https://coveralls.io/repos/github/naibor/Ride-with-me/badge.svg?branch=Develop)](https://coveralls.io/github/naibor/Ride-with-me?branch=Develop)

A carpooling application that provides drivers with the ability to create ride offers and passengers to join available ride offers.

## The project contains designs for

 1. _**Landing page.**_
 2. _**User signup.**_
 3. _**User Login.**_
 4. _**Driver registration page**_
 5. _**Driver's dashboard.**_
 6. _**A Users dashboard.**_

### Installation

 ####To get the application:

- clone the repo

- cd into the repo

```$ /Ride-with-me/```

copy the link to a browser of your liking.

## Usage

 The application is usefull for regular commuters who need a ride home or to work.
 It offers a job opportunity to drivers, they can register as drivers and post offers.
 Passangers can request rides and view available rides.
 Drivers can post ride offers and view available requests.

## Demo

View demo: [click](https://naibor.github.io/Ride-with-me/)

### API

---------------------------------------------------------------------------------------------------------------

## ENDPOINTS

 **METHOD**| **Endpoints**                       |**Functionality**            |
- ---------|-------------------------------------|-----------------------------|
 GET       |/api/v1/users/rides/<int:id>/requests| Fetch all offer             |
 GET       |/api/v1/users/rides/<int:id>         | Fetch a single offer        |
 POST      |/api/v1/users/rides                  | create a ride offer         |
 POST      |/api/v1/users/request                | Request a ride offer        |
 POST      |/api/v1/auth/signup                  | Handles user signup         |
 POST      |/api/v1/auth/login                   | Handles users login         |
 POST      |/api/v1/auth/register                | Handles driver registration |

## Technologies and languages

1. python

2. flask framework

3. flask restful

### Run locally

create a virtual environment for the project:

```$ virtualenv --python=python3.6 virtualenv-name```

activate the virtual environment:

```$ source virtualenv-name/bin/activate```

use virtualenv-wrapper alternative:

```$ mkvirtualenv --python=python3.5 virtualenv-name```

to use it:

```$ workon virtualenv-name```

run ```$pip install -r requirements.txt``` to install libraries in requirements.txt

## Acknowledge

Leona Naibor