from termcolor import colored

class Display(object):
    
    #Display movie list and select movie
    def displayMovies(self, movieList):
        for movies in movieList:
            print "   "+str(movies)+" : "+str(movieList[movies])+"\n"
        
        #validation of movie id
        while True: 
            movie_id = int(raw_input("Please enter Movie id from above list:\n"))
            if (movie_id in movieList):
                print "\n selected "+movieList[movie_id]+" movie \n"
                return movie_id
            else:
                print("Invalid Movie id.")
                continue        
        
    
    #Display date list and select date
    def displayDates(self, movie_id, movieList, movieDates):
        for movieDate in movieDates:
            print "   "+str(movieDate)+" : "+str(movieDates[movieDate])+"\n"
        
        #validation of movie date
        while True: 
            movies_dates_id = int(raw_input("Please enter date id from above list:\n"))
            if (movies_dates_id in movieDates):
                print "\n selected "+movieList[movie_id]+" movie on "+str(movieDates[movies_dates_id])+" date \n"
                return movies_dates_id
            else:
                print("Invalid Date id.")
                continue 
         

    #Display time list and select time
    def displayTimes(self, movie_id, movies_dates_id, movieList, movieDates, movieTimes):
        for movieTime in movieTimes:
            print "   "+str(movieTime)+" : "+str(movieTimes[movieTime])+"\n"
        
        #validation of movie time
        while True: 
            movies_time_id = int(raw_input("Please enter time id from above list:\n"))
            if (movies_time_id in movieTimes):
                print "\n selected "+movieList[movie_id]+" movie on date "+str(movieDates[movies_dates_id])+" and time "+str(movieTimes[movies_time_id])+" \n"
                return movies_time_id
            else:
                print("Invalid Time id.")
                continue 
    
    #Display seat nos and select seat
    def displaySeats(self,bookedTicketNo):
        showtickets = '  ';
        seat_nos = [];
        for ticketno in range(1,51):
            if (ticketno in bookedTicketNo):
                showtickets += colored(str(ticketno).zfill(2) , 'red')+" "
            else:
                showtickets += colored(str(ticketno).zfill(2), 'blue')+" "
                
            if(ticketno%10 == 0):
                showtickets += "\n  "
        print "  ##############################\n  #           SCREEN           #\n  ##############################\n"    
        print showtickets
        print "\n  "+colored("*", 'blue')+" : Available Tickets"
        print "\n  "+colored("*", 'red')+" : Booked Tickets "
        
        #validation of movie seat no
        while True: 
            seat_no = int(raw_input("\nPlease enter available seat no to book:"))
            if (seat_no in bookedTicketNo or seat_no > 50 or seat_no < 1):
                print("Invalid Seat No.")
                continue
            else:
                print "\n selected Seat No:"+str(seat_no)+"\n "
                seat_nos.append(seat_no)
                decision = raw_input("Want to book another seat no type Y or N : ")
                if decision == 'Y':
                    continue
                return seat_nos