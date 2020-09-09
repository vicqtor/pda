def update(configtoset, newvalue):
    try:
        if os.path.exists(datacore['jsonfilecap']) is False:writeconfigfile()
        currentdata = json.loads(readconfigfile())
        currentdata[str(configtoset)] = newvalue
        with open(datacore['jsonfilecap'], 'w') as modifyjfile:modifyjfile.write(json.dumps(currentdata, indent = 4))
    except:pass

    with open('nr_cfgs.json', 'r') as reader:
	cfg = reader.read()
	
training_sets_inputs = array(json.loads(cfg)['training_sets_inputs'])

def notify(info):
	notify2.init('new notif')
        notif = notify2.Notification(str(title), str(info), icon = data('ntfyico')) # notif.set_urgency(notify2.URGENCY_CRITICAL)
        notif.show()
        notif.set_timeout(dur)#, time.sleep(60)

while True:
    ctime = datetimdatetime.now()
    routines = json.loads(cfg)['training_sets_inputs']   data('routines')
    rtntimes = json.loads(cfg)['training_sets_inputs']   data('routinestimes')
    rtntimebr = json.loads(cfg)['training_sets_inputs']   data('rtntimebreak')

    for routine in rtntimes:
        if rtntimebr in routine:
            rtntimecount, rtntimetype = routine.split(str(rtntimebr))
            rtncap, rtninfo = 'routine', 'every ' + str(rtntimecount) + ' ' + str(rtntimetype) + '\n' + str(routines[rtntimes.index(str(routine))].split(':')[1])
            update('ntfytt', rtncap), update('ntfyinfo', rtninfo), notify()
        elif routine.startswith(rtntimebr):
            if ctime.hour == datetime.datetime.strptime(str(routine[len(rtntimebr):]).strip(), '%H%M').hour:update('ntfytt', rtncap), update('ntfyinfo', rtninfo), notify()
        else:
            rtnjustdate, rtnjustinfo = routines[rtntimes.index(str(routine))].split(':')
            stime, rtnjustdate = datetime.datetime.strptime(routine, '%d.%m.%y.%H.%M'), rtnjustdate.replace('active', '')     
            if ctime.year == stime.year and ctime.month == stime.month and ctime.day == stime.day and ctime.hour == stime.hour and ctime.minute == stime.minute:
                rtncap, rtninfo = 'schedule', str(rtnjustdate) + '\n' + str(rtnjustinfo)
                newrtnstatus = routines[rtntimes.index(str(routine))].replace('active', 'expired')
                routines[rtntimes.index(str(routine))] = newrtnstatus

                update('routines', routines)
                update('ntfytt', rtncap)
                update('ntfyinfo', rtninfo)

                notify()
