from dbconnection import DBConnection


class Movies(DBConnection):

    # get movie list
    def getMovies(self):
        DBConnection.dictCursor.execute("SELECT * FROM movies")
        resultSet = DBConnection.dictCursor.fetchall()
        movie = {}
        for row in resultSet:
            movie[row['id']] = row['name']
        return movie

    # get dates of movie
    def getMovieDates(self, movies_id):
        DBConnection.dictCursor.execute(
            "SELECT id,date FROM movie_dates where movies_id="+str(movies_id))
        resultSet = DBConnection.dictCursor.fetchall()
        movieDates = {}
        for row in resultSet:
            movieDates[row['id']] = row['date']
        return movieDates

    # get time of movie on selected date
    def getMovieDateTimes(self, movies_id, movies_dates_id):
        DBConnection.dictCursor.execute(
                "SELECT id,time FROM movie_times "
                + "where movies_id="+str(movies_id)
                + " AND movies_dates_id ="+str(movies_dates_id)
            )
        resultSet = DBConnection.dictCursor.fetchall()
        movieDates = {}
        for row in resultSet:
            movieDates[row['id']] = row['time']
        return movieDates

    # book ticket
    def bookTicket(
            self, movies_id, movies_dates_id,
            movie_times_id, seat_no, user_id
    ):
        sql = "INSERT INTO tickets_booked (`movies_id`, `movies_dates_id`,"
        sql += " `movie_times_id`, `seat_no`, `user_id`)"
        sql += " VALUES (%s,%s,%s,%s,%s)"
        val = (movies_id, movies_dates_id, movie_times_id, seat_no, user_id)
        try:
            DBConnection.dictCursor.execute(sql, val)
            DBConnection.db.commit()
        except MySQLdb.error:
            DBConnection.db.rollback()

        # get time of movie on selected date
    def getBookedSeats(self, movies_id, movies_dates_id, movie_times_id):
        DBConnection.dictCursor.execute(
            "SELECT seat_no FROM tickets_booked where movies_id="
            + str(movies_id)+" AND movies_dates_id ="+str(movies_dates_id)
            + " AND movie_times_id ="+str(movie_times_id))
        resultSet = DBConnection.dictCursor.fetchall()
        bookedSeats = []
        for row in resultSet:
            bookedSeats.append(row['seat_no'])
        return bookedSeats
