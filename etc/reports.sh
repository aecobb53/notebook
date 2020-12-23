

# task end.after:today-12h completed
# task end.after:today-12d all
# task burndown.daily
# task ghistory.monthly
# task history.monthly
# task timesheet
# export
# pdf from charts as a result of cmdline run?
# task calendar
# remove scheduled after now


# echo 12 hr completed
# task end.after:today-12h completed

# echo 12 hr all
# task end.after:today-12d all

# echo burndown daily
# task burndown.daily

# echo ghist monthly
# task ghistory.monthly

# echo history monthly
# task history.monthly

# echo timesheet
# task timesheet

# # echo 
# # export

# # pdf from charts as a result of cmdline run?

# # task calendar

# # remove scheduled after now

weekdays() {
    d1=$(date -d "$1" +%s)
    echo ${d1}
}

DATE=$(date)
result=$(weekdays "${DATE}")
# RESULT=$(weekdays "${DATE}")
echo $d1

# DATE=$(date +%s)
# START_S=$(date +%s -d "last Monday")
# END_S=$((START-(7*86400)))
# START=$((START_S))
# END=$((END_S))
# echo $((DATE/86400))
# echo $((START_S))
# echo $((END_S))

exit

echo Weekly reports
# task end.after:2020-10-20 and end.before:2020-11-01 created
task end.after:2020-10-25 and end.before:2020-11-01 completed

echo Monthly reports
task end.after:2020-10-01 and end.before:2020-11-01 completed
task calendar
task ghistory.monthly
task history.monthly

echo Yearly reports
task burndown.monthly