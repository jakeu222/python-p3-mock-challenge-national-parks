class NationalPark:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name
    def set_name(self,value):
        if type(value) is str and 3<=len(value) and not hasattr(self,"name"):
            self._name = value
        else:
            raise Exception("Not valid name")
    name = property(get_name,set_name)

    def trips(self):
        r_list = []
        for trip in Trip.all:
            if type(trip) is Trip and trip.national_park is self:
                r_list.append(trip)
        return r_list
    
    def visitors(self):
        r_list = []
        for trip in Trip.all:
            if type(trip) is Trip and trip.national_park is self and trip.visitor not in r_list:
                r_list.append(trip.visitor)
        return r_list
    
    def total_visits(self):
        visits = 0
        for trip in Trip.all:
            if type(trip) is Trip and trip.national_park is self:
                visits +=1
        return visits
    
    def best_visitor(self):
        current_best = None
        current_best_count = 0
        all_visitors = self.visitors()
        for visitor in all_visitors:
            count = visitor.total_visits_at_park(self)
            if count > current_best_count:
                current_best = visitor
                current_best_count = count
        return current_best

        


class Trip:
    valid_month = ("January", "February", "March", "April", "May", "June", "July", "August", "September","October","November","December")
    all = []
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    def get_start_date(self):
        return self._start_date
    def set_start_date(self,value):
        if type(value) is str and 7<=len(value):
            split_str = value.split()
            if split_str[0] in Trip.valid_month and 3<=len(split_str[1])<=4:
                self._start_date = value
            else:
                raise Exception("Not valid start date format")
        else:
            raise Exception("not valid start date")
    

    def get_end_date(self):
        return self._end_date
    def set_end_date(self,value):
        if type(value) is str and 7<=len(value):
            split_str = value.split()
            if split_str[0] in Trip.valid_month and 3<=len(split_str[1])<=4:
                self._end_date = value
            else:
                raise Exception("Not valid end date format")
        else:
            raise Exception("not valid end date")

    def get_visitor(self):
        return self._visitor
    def set_visitor(self,value):
        if type(value) is Visitor:
            self._visitor = value
        else:
            raise ValueError("Not valid visitor")

    def get_national_park(self):
        return self._national_park
    def set_national_park(self,value):
        if type(value) is NationalPark:
            self._national_park = value
        else:
            raise ValueError("Not valid national park")

    start_date = property(get_start_date,set_start_date)
    end_date = property(get_end_date,set_end_date)
    visitor = property(get_visitor,set_visitor)
    national_park = property(get_national_park,set_national_park)


class Visitor:
    
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self._name
    def set_name(self,value):
        if type(value) is str and 1<=len(value)<=15:
            self._name = value
        else:
            raise Exception("Not valid name")
    name = property(get_name,set_name)

    def trips(self):
        r_list = []
        for trip in Trip.all:
            if type(trip) is Trip and trip.visitor is self:
                r_list.append(trip)
        return r_list

    
    def national_parks(self):
        r_list = []
        for trip in Trip.all:
            if type(trip) is Trip and trip.visitor is self and trip.national_park not in r_list:
                r_list.append(trip.national_park)
        return r_list
    
    def total_visits_at_park(self, park):
        our_trips = self.trips()
        count = 0
        for trip in our_trips:
            if trip.national_park is park:
                count +=1
        return count


bob = Visitor("Bob")
bill = Visitor("Bill")
tom = Visitor("Tom")
yosemite = NationalPark("Yosemite")
rocky_mtns = NationalPark("Rocky Mountains")
Trip(bob,yosemite,"May 7th", "May 9th")
Trip(bob,rocky_mtns,"May 7th", "May 9th")
Trip(bob,yosemite,"May 7th", "May 9th")
Trip(bill,yosemite,"May 7th", "May 9th")
Trip(tom,rocky_mtns,"May 7th", "May 9th")
Trip(tom,rocky_mtns,"May 7th", "May 9th")
# print(tom.trips())
# print(bill.national_parks()[0] is yosemite)
# print(yosemite.visitors()[0] is bob)
# print(yosemite.total_visits())
# print(bob.total_visits_at_park(rocky_mtns))
print(yosemite.best_visitor().name)





















# class NationalPark:

#     def __init__(self, name):
#         self.name = name

#     def get_name(self):
#         return self._name
#     def set_name(self, name):
#         if isinstance(name, str) and len(name) >= 3 and not hasattr(self, "name"):
#             self._name = name
#     name = property(get_name, set_name)

    
        
#     def trips(self):
#         return [trip for trip in Trip.all if trip.park is self]
        
    
#     def visitors(self):
#         return list({result.visitor for result in self.visitors()})
    
#     def total_visits(self):

#         return len(self.trips())
    
#     def best_visitor(self):
#         visit_counts = {}  # Dictionary to store visit counts

#         # Count visits for each visitor
#         for trip in self.trips():
#             visitor = trip.visitor
#             if visitor in visit_counts:
#                 visit_counts[visitor] += 1
#             else:
#                 visit_counts[visitor] = 1

#         # Find the visitor with the highest visit count
#         if visit_counts:
#             best_visitor = max(visit_counts, key=visit_counts.get)
#             return best_visitor
#         else:
#             return None


# class Trip:
#     all =[]
    
#     def __init__(self, visitor, national_park, start_date, end_date):
#         self.visitor = visitor
#         self.national_park = national_park
#         self.start_date = start_date
#         self.end_date = end_date
#         type(self).all.append(self)

#     @property
#     def national_park(self):
#         return self._national_park
    
#     @national_park.setter
#     def national_park(self, national_park):
#         if isinstance(national_park,NationalPark):
#             self._national_park = national_park

#     @property
#     def visitor(self):
#         return self._visitor

#     @visitor.setter
#     def visitor(self, visitor):
#         if isinstance(visitor, Visitor):
#             self._visitor = visitor
    
#     def get_start_date(self):
#         return self._start_date

#     def set_start_date(self, new_date):
#         self._start_date = self.validate_start_date(new_date)

#     def validate_start_date(self, date_str):
#         if isinstance(date_str, str) and len(date_str) >= 7:
#             return date_str
#         else:
#             raise ValueError("Invalid start date format or length")

#     start_date = property(get_start_date, set_start_date)



#     def get_end_date(self):
#         return self._end_date

#     def set_end_date(self, new_date):
#         self._end_date = self.validate_end_date(new_date)

#     def validate_end_date(self, date_str):
#         if isinstance(date_str, str) and len(date_str) >= 7:
#             return date_str
#         else:
#             raise ValueError("Invalid end date format or length")

#     end_date = property(get_end_date, set_end_date)

# class Visitor:
#     all =[]

#     def __init__(self, name):
#         self.name = name
#         type(self).all.append(self)
        

    
#     def get_name(self):
#         return self.name
    
#     def set_name(self, name):
#         if isinstance(name, str) and 1 <= len(name) <= 15:
#             self._name = name
#         else:
#             print("Warning")


#     name = property(get_name, set_name)
    
        
#     def trips(self):
#         return [trip for trip in Trip.all if trip.visitor is self]
    
#     def national_parks(self):
#         return list({result.visitor for result in self.trips()})
        
    
#     def total_visits_at_park(self, park):
#         return len(self.trips())
        