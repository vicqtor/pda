import json
import datetime

with open('pa_cfgs.json', 'r') as reader:
	cfgs = reader.read()

def notify(info):
	notify2.init('new notif')
    notif = notify2.Notification('pa', info)
	# notif.set_urgency(notify2.URGENCY_CRITICAL)
    notif.show()
    notif.set_timeout(10)

routines = json.loads(cfgs)['routines']
for x in y:
	set times - info + time
	
while True:
	brk = '/'
    ctime = datetime.datetime.now()
	times = json.loads(cfgs)['times']

    for rtn_time in times:
		if rtn_time.startswith(brk):
			rtn = rtn_time[len(brk):]
			if ctime.hour == datetime.datetime.strptime(rtn, '%H%M').hour:
				info = json.loads(cfgs)['routines']
        
        elif brk in rtn_time:
            rtntimecount, rtntimetype = rtn_time.split(brk) 
			info = 'every ' + rtntimecount + ' ' + rtntimetype + '\n' + rtn_time[times.index(rtn_time)].split(':')[1]
        
		else:
            rtnjustdate, rtnjustinfo = routines[rtntimes.index(routine)].split(':')
            stime = datetime.datetime.strptime(routine, '%d.%m.%y.%H.%M')
			rtnjustdate = rtnjustdate.replace('active', '')     
            
			if ctime.year == stime.year and ctime.month == stime.month and ctime.day == stime.day and ctime.hour == stime.hour and ctime.minute == stime.minute:
                rtncap, rtninfo = 'schedule', str(rtnjustdate) + '\n' + str(rtnjustinfo)
                newrtnstatus = routines[rtntimes.index(str(routine))].replace('active', 'expired')
                routines[rtntimes.index(str(routine))] = newrtnstatus
			
			info = ''
		
		notify(info)
