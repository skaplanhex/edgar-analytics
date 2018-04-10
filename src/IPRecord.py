import datetime as dt

def get_string(timestamp):
        return timestamp.strftime("%Y-%m-%d %H:%M:%S")

class IPRecord:
    def __init__(self, ip_address, first_request):
        self.ip = ip_address
        self.requests = [first_request,]
    def add_request(self,request):
        self.requests.append(request)
        return
    def get_first_request(self):
        return self.requests[0]
    def get_latest_request(self):
        return self.requests[-1]
    def get_session_time(self):
        return (self.requests[-1] - self.requests[0]).seconds
    def get_request_count(self):
        return len(self.requests)
    def get_time_inactive(self, current_time):
        return (current_time - self.requests[-1]).seconds
    def session_record(self):
        to_return = "%s,%s,%s,%i,%i"%(self.ip, get_string(self.requests[0]),
                    get_string(self.requests[-1]), self.get_session_time(), 
                    self.get_request_count())
        print(to_return)
    def print_record(self):
        print("ip =", self.ip)
        print("requests:")
        for r in self.requests:
            print(r)