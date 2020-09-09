def update(configtoset, newvalue):
    try:
        if os.path.exists(datacore['jsonfilecap']) is False:writeconfigfile()
        currentdata = json.loads(readconfigfile())
        currentdata[str(configtoset)] = newvalue
        with open(datacore['jsonfilecap'], 'w') as modifyjfile:modifyjfile.write(json.dumps(currentdata, indent = 4))
    except:pass
