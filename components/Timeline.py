from globals import fileHandler, timeline
from datetime import datetime


class Timeline:
    
    def current(self):
        now = datetime.now()
        timeNow = now.strftime(fileHandler.config["TIME_FORMATE"])
        
        if now.strftime("%m/%d/%y") != fileHandler.config["HACKATHON_DATE"] or self.compare2time(timeNow, fileHandler.config["HACKATHON_END"], ">="):
            return ["Finished", '0:00']
        else:
            
            if self.compare2time(timeNow, fileHandler.config["HACKATHON_START"], "<"):
                return ["Doesn't Start Yet", fileHandler.config["HACKATHON_START"][:-3]]

            else:
                for event in list(timeline.keys())[::-1]:
                    if self.compare2time(timeNow, timeline[event]["start"], '>='):
                        ret = [timeline[event]["name"]]

                        if event == list(timeline.keys())[-1]:
                            ret.append(fileHandler.config["HACKATHON_END"][:-3])
                        else:
                            ret.append(timeline[str(int(event)+1)]["start"])

                        return ret

    def compare2time(self, stime1, stime2, sign):
        if sign == '==':
            return datetime.strptime(stime1, fileHandler.config['TIME_FORMATE']) == datetime.strptime(stime2, fileHandler.config['TIME_FORMATE'])
        elif sign == '>':
            return datetime.strptime(stime1, fileHandler.config['TIME_FORMATE']) > datetime.strptime(stime2, fileHandler.config['TIME_FORMATE'])
        elif sign == '>=':
            return datetime.strptime(stime1, fileHandler.config['TIME_FORMATE']) >= datetime.strptime(stime2, fileHandler.config['TIME_FORMATE'])
        elif sign == '<':
            return datetime.strptime(stime1, fileHandler.config['TIME_FORMATE']) < datetime.strptime(stime2, fileHandler.config['TIME_FORMATE'])
        elif sign == '<=':
            return datetime.strptime(stime1, fileHandler.config['TIME_FORMATE']) <= datetime.strptime(stime2, fileHandler.config['TIME_FORMATE'])



time = Timeline()
print(time.current())
