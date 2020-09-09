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

while True:
	brk = '/'
    ctime = datetimdatetime.now()
    routines = json.loads(cfgs)['routines']
	times = json.loads(cfgs)['times']

    for routine in times:
		if routine.startswith(brk):
			if ctime.hour == datetime.datetime.strptime(routine[len(brk):], '%H%M').hour:
				info = ''
        
        elif brk in routine:
            rtntimecount, rtntimetype = routine.split(brk) 
			info = 'every ' + rtntimecount + ' ' + rtntimetype + '\n' + routines[rtntimes.index(routine)].split(':')[1]
        
		else:
            rtnjustdate, rtnjustinfo = routines[rtntimes.index(routine)].split(':')
            stime = datetime.datetime.strptime(routine, '%d.%m.%y.%H.%M')
			rtnjustdate = rtnjustdate.replace('active', '')     
            
			if ctime.year == stime.year and ctime.month == stime.month and ctime.day == stime.day and ctime.hour == stime.hour and ctime.minute == stime.minute:
                rtncap, rtninfo = 'schedule', str(rtnjustdate) + '\n' + str(rtnjustinfo)
                newrtnstatus = routines[rtntimes.index(str(routine))].replace('active', 'expired')
                routines[rtntimes.index(str(routine))] = newrtnstatus

                update('routines', routines)
                update('ntfytt', rtncap)
                update('ntfyinfo', rtninfo)
			
			info = ''
		
		notify(info)
