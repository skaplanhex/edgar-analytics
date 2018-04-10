from IPRecord import *
import datetime as dt
from dateutil import parser

col_order = []
def print_file(fname):
    for line in open(fname):
        print(line)

def get_column_order(line):
    return line.split(",")
    
def make_line_dict(line):
    s = line.split(",")
    d = {}
    for i,col in enumerate(col_order):
        d[col] = s[i]
    return d
def make_document_id(cik, accession, extention):
    return "%s___%s___%s"%(cik, accession, extention)
#def analyze_file(fname):
fname = "../input/log.csv"
inactive_period = 2  
lineNum = 0
iprecord_dict = {}
for line in open(fname):
    line = line.strip("\n")
    if lineNum == 0:
        col_order = get_column_order(line)
        lineNum += 1
        continue
    
    line_dict = make_line_dict(line)   
    #ip,date,time,zone,cik,accession,extention,code,size,idx,norefer,noagent,find,crawler,browser
    ip = line_dict["ip"]
    timestamp = parser.parse("%s %s"%(line_dict["date"], line_dict["time"]))
    doc_id = make_document_id(line_dict["cik"], line_dict["accession"], line_dict["extention"])
    if ip not in iprecord_dict:
        iprecord_dict[ip] = IPRecord(ip, timestamp)
    else:
        iprecord_dict[ip].add_request(timestamp)
    # now check to see if any sessions have ended
    to_clean = []
    print(ip,timestamp)
    for i in iprecord_dict:
        time_inactive = iprecord_dict[i].get_time_inactive(timestamp)
        # print(i,time_inactive)
        if time_inactive >= inactive_period:
            print(iprecord_dict[i].session_record())
            to_clean.append(i)
    for i in to_clean:
        iprecord_dict.pop(i)
    lineNum += 1
#for ip in iprecord_dict:
#   iprecord_dict[ip].print_record()

#if __name__ == "__main__":
#    analyze_file("../input/log.csv")