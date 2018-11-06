from display import Display
from movies import Movies

class BookMyShow(Display):
        
    def run(self):
        print("\n Welcome to BookMyShow \n \n Please select Movie from following list: \n\n")
        movie = Movies()
        
        #Display movie list and select movie
        movieList = movie.getMovies()
        movie_id = super(BookMyShow,self).displayMovies(movieList)
        
        #Display date list and select date
        movieDates = movie.getMovieDates(movie_id)
        movies_dates_id = super(BookMyShow,self).displayDates(movie_id,movieList, movieDates)
        
        #Display time list and select time
        movieTimes = movie.getMovieDateTimes(movie_id,movies_dates_id)
        movies_time_id = super(BookMyShow,self).displayTimes(movie_id, movies_dates_id, movieList, movieDates, movieTimes)
        
        #Display seat nos and select seat
        bookedTicketNo = movie.getBookedSeats(movie_id, movies_dates_id, movies_time_id)
        seat_nos = super(BookMyShow,self).displaySeats(bookedTicketNo)
        
        decision = input("Want to Book Ticket \n Plese enter Y or N:")
        if(decision == 'Y'):
            for seat_no in seat_nos:
                movie.bookTicket(movie_id,movies_dates_id,movies_time_id,seat_no,1)
                print("\n Booked seat no "+str(seat_no)+" for "+movieList[movie_id]+" movie on date "+str(movieDates[movies_dates_id])+" and time "+str(movieTimes[movies_time_id])+" Successfully ")
            
        

bookTicket = BookMyShow()
bookTicket.run()