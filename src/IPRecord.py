import datetime as dt

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
        return len(requests)
    def print_record(self):
        print("ip =", self.ip)
        print("requests:")
        for r in self.requests:
            print(r)