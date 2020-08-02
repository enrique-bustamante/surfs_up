# surfs_up

This challenge will be an exercise in using SQLite, where we'll be analyzing data for surfing and ice cream in Oahu.

### Methods

For this challenge we utilized the following packages:
* SQLAlchemy
* Pandas
* Numpy
* Flask

We utilized the following languages:
* Python
* HTML
* SQLite

To pull the data for the specific months in question, I utilized the extract
function calling on the specific month for both June and December. I then used
the describe method to get the data and used the to_html function to post the
table using Flask.

### June vs Dec Analysis

#### Temperatures
The average temperature for June is 74.9 degrees, while the average is 71.0
degrees in December. With an average difference of no more tha 4 degrees, the
temperature during the months of June and December do not differ by much.

The standard deviation of these two months also does show that there is more
variation in temperatures in December as opposed to June. The range from min
to max for June is  64 to 85 degrees, while for December, the range is 56 to
83 degrees.


#### Precipitation
The average precipiation for June is 0.14 inches per day,
while the average precipitation for December is 0.22 inches. There seems to be
more precipitation on a daily basis in December than in June.

The standard deviation of the two months shows that there is more variation in
daily precipitation in December than in June. The range of precipitation in
June is from 0 to 4.43 inches, while in December the range is 0 to 6.42
inches.

While the temperatures and precipitation are not as ideal in December as in
June, it appears that both months may be good to conduct business during.
However, if you had to choose one month over the other, June is the month to
go with.


### Future recommendations

We may want to look at other months in the data in addition to June and
December. We could create a similar page where you enter the month number and
the statistical summary will display on the page as opposed to making 12
different pages.

Instead of looking at just June and December individually, it would be better to see if the
other 10 months have similar statistics. It would be best to plot the
temperatures and precipitation as line plots, to compare them over the course
of the year. If all of the other months are between the statistical ranges of
June and December, it may be feasible to keep the business open year round.

Lastly, we haven't defined the parameters for what we deem to be ideal
weather. If we are clearer on what the minimum temperature or what the maximum
precipitation is acceptable for surfing, we would be able to determine if
other sites are as good or even better to open up shops in.
