from datetime import datetime

data_list = []

log = open("internet.txt", "r")
previous = None
previous_status = ''
for log_line in log:
  date = log_line.split(' - ')[0].strip()
  status = log_line.split(' - ')[1].strip()
  d = datetime.strptime(date, '%a %b %d %H:%M:%S %Z %Y')
  d3_date = d.strftime('%Y-%m-%d %H:%M:00')
  trunc_date = datetime.strptime(d3_date, '%Y-%m-%d %H:%M:%S')
  trunc_date_string = trunc_date.strftime('%Y-%m-%d %H:%M:%S')
  if previous is not None:
    previous_date_string = previous.strftime('%Y-%m-%d %H:%M:%S')
    interval = (trunc_date - previous).seconds
    if(interval > 60):
      data_list.append('["%s", "Missing", "%s"]' % (previous_date_string, trunc_date_string))
    elif(previous_status == 'Offline'):
      data_list.append('["%s", "Offline", "%s"]' % (previous_date_string, trunc_date_string))
    else:
      data_list.append('["%s", "Online", "%s"]' % (previous_date_string, trunc_date_string))
  previous = trunc_date
  previous_status = status

data = '[%s]' % ', '.join(map(str, data_list))

dataset = """[{
    "measure": "WIFI Availability",
    "categories": {
        "Online": { "color": "green" },
        "Offline": { "color": "red" },
        "Missing": { "color": "silver" }
        },
    "data": %s
}]""" % data

print(dataset)