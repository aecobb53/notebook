start_timer() {
    INTERNALTIMER=$(date)
}

time_diff() {
INTERNALSTARTTIME=$(date -d "${1}" +%s)
INTERNALENDTIME=$(date -d "${2}" +%s)

INTERNALRUNTIMES=$((INTERNALENDTIME-INTERNALSTARTTIME))
INTERNALRUNTIME=$(date -d @${INTERNALRUNTIMES} +"%H:%M:%S" -u)
}

end_timer() {
    ENDOFTIMER=$(date)
    echo $INTERNALTIMER
    echo $ENDOFTIMER
    time_diff "${INTERNALTIMER}" "${ENDOFTIMER}"
    echo $INTERNALRUNTIME
}
