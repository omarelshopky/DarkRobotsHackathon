from components.globals import fileHandler, timeline
from datetime import datetime


class Timeline:
    
    def current(self):
        now = datetime.now()
        timeNow = now.strftime(fileHandler.config["TIME_FORMATE"])
        
        if now.strftime("%m/%d/%y") != fileHandler.config["HACKATHON_DATE"] or self.compareWithCurrentTime(fileHandler.config["HACKATHON_END"], ">="):
            return ["Finished", '00:00']
        else:
            
            if self.compareWithCurrentTime(fileHandler.config["HACKATHON_START"], "<"):
                return ["Doesn't Started Yet", fileHandler.config["HACKATHON_START"]]

            else:
                for event in list(timeline.keys())[::-1]:
                    if self.compareWithCurrentTime(timeline[event]["start"], '>='):
                        ret = [timeline[event]["name"]]

                        if event == list(timeline.keys())[-1]:
                            ret.append(fileHandler.config["HACKATHON_END"])
                        else:
                            ret.append(timeline[str(int(event)+1)]["start"])

                        return ret

    def compareWithCurrentTime(self, stime, sign):
        timeNow = datetime.now().strftime(fileHandler.config["TIME_FORMATE"])
        
        if sign == '==':
            return datetime.strptime(timeNow, fileHandler.config['TIME_FORMATE']) == datetime.strptime(stime, fileHandler.config['TIME_FORMATE'])
        elif sign == '>':
            return datetime.strptime(timeNow, fileHandler.config['TIME_FORMATE']) > datetime.strptime(stime, fileHandler.config['TIME_FORMATE'])
        elif sign == '>=':
            return datetime.strptime(timeNow, fileHandler.config['TIME_FORMATE']) >= datetime.strptime(stime, fileHandler.config['TIME_FORMATE'])
        elif sign == '<':
            return datetime.strptime(timeNow, fileHandler.config['TIME_FORMATE']) < datetime.strptime(stime, fileHandler.config['TIME_FORMATE'])
        elif sign == '<=':
            return datetime.strptime(timeNow, fileHandler.config['TIME_FORMATE']) <= datetime.strptime(stime, fileHandler.config['TIME_FORMATE'])

